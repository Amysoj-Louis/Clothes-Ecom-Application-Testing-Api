# Clothes Ecom Application Testing Api

This is a Flask REST API that serves the data in a JSON file. The data is about Women's Sarees and their prices and URLs.

## Features

- The API allows GET requests and returns data in JSON format.
- The API allows fetching data for a specific category by passing the category name in the URL query string.
- If the category name is not specified or incorrect, the API returns an error message.
- If the category name is specified and correct, the API returns the data for that category.

## Prerequisites

- Flask library should be installed.
- The data.json file should be available in the same directory as the code.

## Usage

- The code can be run using python filename.py.
- The API will be accessible at http://localhost:5000/.
  The category data can be fetched by passing the category name in the URL query string, e.g., http://localhost:5000/?category=Women's Sarees.

## Code Walkthrough

- Import the necessary libraries.
- Initialize Flask application.
  Define the API endpoint for the GET request.
- In the API endpoint, get the category name from the URL query string.
- Open the data.json file and load the data into a Python dictionary.
- If the category name is not None or empty, try to return the data for that category.
- If the category name is incorrect, return an error message.
- If the category name is None or empty, return all the data.
- The main function runs the Flask application in debug mode.
