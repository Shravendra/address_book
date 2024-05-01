# FastAPI Address Book

This is a simple FastAPI application for managing addresses. It allows you to add addresses to a SQLite database and retrieve addresses within a certain distance of a given location.

## Features

- Add addresses with street, city, state, country, latitude, and longitude.
- Retrieve addresses within a specified distance from a given latitude and longitude.

## Requirements

- Python 3.x
- FastAPI
- SQLite
- Geopy
- Tenacity

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Shravendra/address_book.git

2. Navigate to the project directory:

   cd address_book


3. create virtual environment:

   python -m venv myenv

4. activate virtual environment:

   myenv\Scripts\activate 
   
5. Install the required dependencies:

   pip install -r requirements.txt

6. Start the FastAPI server

   uvicorn address_app:app --reload


## API Endpoints 

POST /addresses/: Add a new address.

GET /addresses/: Retrieve addresses within a specified distance from a given latitude and longitude.

PUT /addresses/{address_id}: Update an existing address.

DELETE /addresses/{address_id}: Delete an existing address.

   
## Steps to Perform CRUD Operations

# 1. Create Address:
   
 Send a POST request to /addresses/ endpoint with the following JSON data:

   Example: http://localhost:8000/addresses/

   {
    "street": "1600 Pennsylvania Ave NW",
    "city": "Washington",
    "state": "DC",
    "country": "United States",
    "latitude": 38.8977,
    "longitude": -77.0365
}


## 2. Retrieve Addresses:

   Send a GET request to /addresses/ endpoint with query parameters for latitude, longitude, and distance.

   Example: http://localhost:8000/addresses/?latitude=38.8977&longitude=-77.0365&distance=10

   This will retrieve addresses within 10 kilometers from the specified latitude and longitude.



## 3. Update Address:

Send a PUT request to /addresses/{address_id} endpoint with the address ID and the updated address details.

Example: /addresses/1

Provide the updated address data in the request body.

This will update the address with the specified ID.


## 4. Delete Address:
   
Send a DELETE request to /addresses/{address_id} endpoint with the address ID to delete.

Example: /addresses/1

This will delete the address with the specified ID from the database.



## Configuration

The SQLite database file address_book.db is used to store address data. Ensure that the database file is accessible and writable by the application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.




   
