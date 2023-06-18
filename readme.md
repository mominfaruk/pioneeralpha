# TODO App API

This is a TODO app API built using Django Rest Framework. It allows you to manage directories and tasks with various functionalities.

## Getting Started

To get started with the TODO app API, follow the instructions below.


### Installation

1. Clone the repository:


2. Change to the project directory:


3. Create and activate a virtual environment:

4. Install the project dependencies:
-pip install -r requirements.txt

5. Run the development server:
-python manage.py runserver


6. Access the API at `http://localhost:8000/`.

## API Endpoints

The following API endpoints are available:

- `GET /directories/`: Retrieves all directories.
- `POST /directories/`: Creates a new directory.
- `GET /directories/<directory_id>/`: Retrieves a specific directory.
- `PUT /directories/<directory_id>/`: Updates a specific directory.
- `DELETE /directories/<directory_id>/`: Deletes a specific directory.

- `GET /todotasks/`: Retrieves all tasks.
- `POST /todotasks/`: Creates a new task.
- `GET /todotasks/<task_id>/`: Retrieves a specific task.
- `PUT /todotasks/<task_id>/`: Updates a specific task.
- `DELETE /todotasks/<task_id>/`: Deletes a specific task.

## API Payload

When creating or updating a directory or task, you can use the following payload structure:

{
"name": "Directory or task name",
"date": "2023-06-17",
"description": "Task description",
"directory": 1,
"is_important": true,
"is_completed": false,
"is_favorite": true
}


Make sure to replace the values with your own data.

## Clearing Data

To clear all data from the database, you can use the following command:

hit on cleardata/ url. It will clear all the data from the database.