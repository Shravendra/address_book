from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import geopy.distance
from geopy.geocoders import Nominatim
import logging
from tenacity import retry, stop_after_attempt, wait_exponential

app = FastAPI()
geolocator = Nominatim(user_agent="address-book")
logger = logging.getLogger(__name__)

class Address(BaseModel):
    street: str
    city: str
    state: str
    country: str
    latitude: float
    longitude: float

def create_address_table():
    try:
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS addresses
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     street TEXT NOT NULL,
                     city TEXT NOT NULL,
                     state TEXT NOT NULL,
                     country TEXT NOT NULL,
                     latitude REAL NOT NULL,
                     longitude REAL NOT NULL)''')
        conn.commit()
    except sqlite3.Error as e:
        logger.error(f"Error creating address table: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        conn.close()

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def geocode_address(address: str):
    return geolocator.geocode(address)

def add_address(address: Address):
    conn = None
    try:
        location = geocode_address(f"{address.street}, {address.city}, {address.state}, {address.country}")
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")
        
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()
        c.execute('''INSERT INTO addresses (street, city, state, country, latitude, longitude)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                     (address.street, address.city, address.state, address.country, address.latitude, address.longitude))
        conn.commit()
    except sqlite3.Error as e:
        logger.error(f"Error adding address to database: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        if conn:
            conn.close()

def get_addresses_within_distance(latitude: float, longitude: float, distance: float):
    try:
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()
        c.execute('''SELECT id, street, city, state, country, latitude, longitude FROM addresses''')
        addresses = c.fetchall()
        filtered_addresses = []
        for addr in addresses:
            addr_coords = (addr[5], addr[6])
            given_coords = (latitude, longitude)
            if geopy.distance.geodesic(given_coords, addr_coords).kilometers <= distance:
                filtered_addresses.append(addr)
    except sqlite3.Error as e:
        logger.error(f"Error retrieving addresses from database: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        conn.close()
    
    return filtered_addresses

create_address_table()

@app.post("/addresses/")
async def create_address(address: Address):
    add_address(address)
    return {"message": "Address created successfully"}

@app.get("/addresses/")
async def get_addresses(latitude: float, longitude: float, distance: float):
    addresses = get_addresses_within_distance(latitude, longitude, distance)
    if not addresses:
        raise HTTPException(status_code=404, detail="No addresses found within the given distance")
    return addresses
