# JSON Data Processor

A beginner-friendly Python project that reads employee data from a JSON file, processes it, and generates a structured output file.

## Features

* Reads employee records from a JSON file.
* Filters employees based on salary.
* Calculates average salary.
* Generates a new JSON file containing processed results.
* Displays a summary in the terminal.

## Project Structure

```text
json-data-processor/
├── main.py
├── employees.json
├── output.json
└── README.md
```

## Requirements

* Python 3.x
* No external libraries required.

## How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run the following command:

```bash
python3 main.py
```

The script will read `employees.json` and generate `output.json`.

## Concepts Practiced

* Python file handling
* JSON serialization and deserialization
* Lists and dictionaries
* Loops and conditional statements
* Data filtering and aggregation
* Reading and writing files

## Future Improvements

* Add error handling for missing or invalid JSON files.
* Allow users to specify the salary threshold.
* Support CSV input and output.
* Add unit tests using pytest.

## Author

Vartika Nanda
