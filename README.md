# Pytest Practice

This repository is a practice project for learning and experimenting with the [pytest](https://docs.pytest.org/) testing framework in Python.

## Features

- Writing and running unit tests with pytest.
- Exploring pytest fixtures, markers, and plugins.
- Learning best practices for test organization and structure.

## Prerequisites

- Python 3.7 or higher
- `pip` package manager

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ernesthenry/pytest_practice.git
    cd pytest_practice
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

To run all tests, use the following command:
```bash
pytest
```

For more detailed output, use:
```bash
pytest -v
```

## Project Structure

```
pytest_practice/
├── tests/          # Test cases
├── src/            # Source code
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.