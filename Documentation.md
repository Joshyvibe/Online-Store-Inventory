Documentation for Online Store Inventory and Supplier Management API

Greetings and welcome to the Online Store Inventory and Supplier Management API documentation. 
You can effectively manage suppliers and inventory items for an online store with the help of this API.

Table of Contents

1. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Running the Server](#running-the-server)
2. [API Endpoints](#api-endpoints)
   - [Suppliers](#suppliers)
   - [Inventory Items](#inventory-items)
3. [Authentication](#authentication)
4. [Response Format](#response-format)
5. [Error Handling](#error-handling)

## Getting Started {#getting-started}

## Prerequisites {#prerequisites}

Before you begin, ensure you have the following prerequisites installed:

- Python (version 3.x)
- Django
- Django REST Framework

## Installation {#installation}

1. First, clone the repository:

  
   git clone <repository-url>
   

2. Next, install dependencies:

   pip install -r requirements.txt
   

## Running the Server {#running-the-server}

1. Locate/navigate to the project directory:

   Then do:
   cd <project-directory>
 

2. Run the Django development server:

   python manage.py runserver
   

3. The server should now be running locally at `http://127.0.0.1:8000/`.

## API Endpoints {#api-endpoints}


Suppliers:-

- GET /api/supplier/: Get a list of every supplier.
- POST /api/supplier/: Add a new supplier.
- GET /api/supplier/{id}/: Retrieve information about a particular supplier.
- PUT /api/supplier/{id}/: Update the details of a specific supplier.
- DELETE /api/supplier/{id}/: Delete a specific supplier.

Retrieve current items supplied by a supplier
- GET /api/suppliers/{id}/items_supplied/: Delete a specific supplier.


Inventory Items:-

- GET /api/item/: Retrieve a list of all inventory items.
- POST /api/item/: Create a new inventory item.
- GET /api/item/{id}/: Retrieve details of a specific inventory item.
- PUT /api/item/{id}/: Update details of a specific inventory item.
- DELETE /api/item/{id}/: Delete a specific inventory item.

Store Inventory Items:-

- GET /api/storeinventory/: Retrieve a list of all store inventory items.
- POST /api/storeinventory/: Create a new store inventory item.
- GET /api/storeinventory/{id}/: Retrieve details of a specific store inventory item.
- PUT /api/storeinventory/{id}/: Update details of a specific store inventory item.
- DELETE /api/item/{id}/: Delete a specific store inventory item.


## Authentication {#authentication}

Access to public endpoints via this API does not require authentication. Nevertheless, you are free to include authorization and authentication systems as your application requires them.

## Response Format {#response-format}

All responses from the API are in JSON format.

Example Response:

```json
{
    "id": 4,
    "supplier": {
        "id": 1,
        "supplier_name": "Mr X",
        "contact_information": "15 Ajah Road",
        "items_they_supply": [
            1,
            2,
            3
        ]
    },
    "inventory_item": {
        "id": 1,
        "name": "mouse"
    },
    "description": "The best mouse we got",
    "price": "1000.00",
    "quantity": 128,
    "date_added": "2024-06-12T01:11:47Z"
}

```

## Error Handling {#error-handling}

Errors are returned with appropriate HTTP status codes and error messages in the response body.

Example Error Response:

```json
{
    "detail": "Not found."
}

```


This documentation provides basic information for setting up and interacting with the API. For more detailed usage instructions and examples, refer to the API endpoints section. If you encounter any issues or have questions, please feel free to reach out to the development team.

