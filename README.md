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

   uvicorn main:app --reload


## Create addresses 

1. Open Postman or Built-in FastAPI’s Swagger Doc:

   a. Select post option

   b. use api endpoint to post/create the addresses - 

        http://localhost:8000/addresses

   c. use api endpoint to get the addresses




   
