# WebWarden Project Structure

This document explains the organization of the WebWarden project.

## Directory Structure

```
WebWarden/
├── src/
│   └── webwarden/
│       ├── __init__.py          # Package initialization
│       ├── cli.py               # Command-line interface
│       ├── core.py              # Core scraping and crawling logic
│       └── formatting.py        # Output formatting functions
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup configuration
├── pyproject.toml               # Modern Python packaging configuration
├── webwarden.py                 # Main entry point
├── test_installation.py         # Installation verification script
└── examples/                    # Example usage scripts (to be created)
```

## Module Descriptions

### `src/webwarden/__init__.py`

Package initialization file that makes the directory a Python package.

### `src/webwarden/cli.py`

Contains the command-line interface logic using argparse. This module handles:
- Parsing command-line arguments
- Calling the appropriate functions from core.py
- Formatting and displaying output

### `src/webwarden/core.py`

Contains the core scraping and crawling logic:
- `get_page_html()`: Retrieves HTML content using Playwright
- `scrape_data()`: Extracts specific data types from HTML
- `crawl_pages()`: Implements the crawling algorithm

### `src/webwarden/formatting.py`

Handles formatting of scraped data for different output formats:
- `format_output()`: Main formatting dispatcher
- `format_single_result()`: Formats a single scraping result
- `format_all_mode()`: Special formatting for 'all' mode
- `format_table_md()`: Formats tables as Markdown
- `format_table_txt()`: Formats tables as plain text

### `webwarden.py`

Main entry point for the application. Simply imports and calls the main function from cli.py.

### `setup.py` and `pyproject.toml`

Package configuration files that define dependencies, entry points, and metadata for distribution.

### `requirements.txt`

Lists all Python dependencies with minimum versions.

### `README.md`

Comprehensive documentation for users.

### `test_installation.py`

Script to verify that the installation is working correctly.

## Entry Points

The application can be run in two ways:

1. Directly with Python:
   ```bash
   python webwarden.py [arguments]
   ```

2. After installation as a package:
   ```bash
   webwarden [arguments]
   ```

## Development Workflow

1. Make changes to the appropriate files in `src/webwarden/`
2. Test changes by running:
   ```bash
   python webwarden.py [test arguments]
   ```
3. For distribution, package the application using:
   ```bash
   python -m build
   ```