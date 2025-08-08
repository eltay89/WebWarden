# WebWarden: Your All-in-One Web Scraper

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)

Welcome to **WebWarden**, a powerful and easy-to-use command-line tool for scraping and crawling websites. Whether you need to extract text, find all the links on a page, download images, or pull data from tables, WebWarden has you covered. It even includes an **`all`** mode to get everything at once!

Built with Python, Playwright, and BeautifulSoup, WebWarden can handle both simple static pages and complex, dynamic websites that rely on JavaScript.

## Table of Contents

- [What is Web Scraping?](#what-is-web-scraping)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Commands](#commands)
  - [Scrape](#scrape)
  - [Crawl](#crawl)
- [Modes](#modes)
- [Output Formats](#output-formats)
- [Examples](#examples)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## What is Web Scraping?

Web scraping is the process of automatically extracting information from websites. Instead of manually copying and pasting data, you can use a tool like WebWarden to do it for you, saving you time and effort.

Web scraping is useful for:

- **Market Research**: Collecting product prices, reviews, or competitor data
- **Content Aggregation**: Gathering news articles or blog posts from multiple sources
- **Data Analysis**: Extracting structured data from unstructured web content
- **SEO Monitoring**: Tracking website rankings, backlinks, or keyword positions
- **Lead Generation**: Finding contact information or business details

## Key Features

- **Five Scraping Modes**: Choose from `text`, `links`, `images`, `tables`, or `all` to get the exact data you need
- **Deep Crawling**: Start at one page and let WebWarden follow links to scrape multiple pages automatically
- **Handles Modern Websites**: Renders JavaScript to ensure all content is loaded before scraping
- **Flexible Output**: Save your data in `TXT`, `JSON`, or `Markdown` format
- **User-Friendly CLI**: Clean, intuitive command-line interface with helpful examples
- **Polite Crawling**: Built-in delays to avoid overwhelming servers
- **Domain Restriction**: Crawls stay within the same domain to prevent unintended scraping
- **Error Handling**: Graceful handling of network errors and parsing issues
- **Rich Output**: Beautifully formatted console output using the Rich library

## Installation

Getting started with WebWarden is easy. Just follow these steps:

### Prerequisites

- Python 3.8 or newer
- pip (Python package installer)

### Installation Steps

1. **Clone this Project**:
   ```bash
   git clone https://github.com/your-username/WebWarden.git
   cd WebWarden
   ```

2. **Install Dependencies**:
   Run the following command to install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Web Browsers**:
   WebWarden uses Playwright to control a headless browser. Install the required browsers with this command:
   ```bash
   playwright install
   ```

### Alternative Installation (Development Mode)

To install WebWarden in development mode (editable install):
```bash
pip install -e .
```

This allows you to modify the code and see the changes immediately without reinstalling.

## Quick Start

Here are some quick examples to get you started:

1. **Get all the text from a blog post**:
   ```bash
   webwarden scrape text "https://example.com/blog/my-post"
   ```

2. **Find all images on a page and save them to a JSON file**:
   ```bash
   webwarden scrape images "https://example.com/gallery" --format json --output images.json
   ```

3. **Scrape all tables from a Wikipedia page as a Markdown file**:
   ```bash
   webwarden scrape tables "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)" --format md --output population_tables.md
   ```

4. **Crawl a news website for headlines (text) up to 2 levels deep**:
   ```bash
   webwarden crawl text "https://news.example.com" 2
   ```

5. **Scrape everything from a single page and save it to a JSON file**:
   ```bash
   webwarden scrape all "https://example.com" --format json --output everything.json
   ```

## Commands

WebWarden has two main commands: `scrape` and `crawl`.

### Scrape

The `scrape` command is used to extract data from a single URL.

**Syntax**:
```bash
webwarden scrape <mode> <url> [--format <format>] [--output <file>]
```

**Arguments**:
- `<mode>`: What type of data to scrape (text, links, images, tables, all)
- `<url>`: The URL of the page to scrape

**Options**:
- `--format`: Output format (txt, json, md)
- `--output`: File to save output to (default: stdout)

### Crawl

The `crawl` command starts at a given URL and follows links to other pages on the same website, scraping data as it goes.

**Syntax**:
```bash
webwarden crawl <mode> <url> [<depth>] [--format <format>] [--output <file>]
```

**Arguments**:
- `<mode>`: What type of data to scrape (text, links, images, tables, all)
- `<url>`: Starting URL for crawling
- `<depth>`: How many levels deep to crawl (default: 1)

**Options**:
- `--format`: Output format (txt, json, md)
- `--output`: File to save output to (default: stdout)

## Modes

WebWarden supports five different scraping modes:

### `text`

Extracts all the plain text from the page, removing HTML tags and formatting. This is useful for:
- Getting article content
- Extracting blog posts
- Collecting textual information

### `links`

Finds all the hyperlinks (URLs) on the page. This is useful for:
- Building sitemaps
- Finding related pages
- Discovering navigation structures

### `images`

Finds all the image sources (URLs) on the page. This is useful for:
- Collecting image galleries
- Finding product images
- Building image datasets

### `tables`

Pulls data from all the HTML tables on the page. This is useful for:
- Extracting structured data
- Collecting financial information
- Getting statistical data

### `all`

Scrapes everything—text, links, images, and tables—all at once. This is useful for:
- Comprehensive page analysis
- Archiving web content
- Complete data extraction

## Output Formats

WebWarden supports three output formats:

### `txt` (Plain Text)

Simple, human-readable format. This is the default for most modes.

### `json` (JavaScript Object Notation)

Structured format that's great for use in other programs. This is the default for the `all` mode.

### `md` (Markdown)

Formatted text that can be used in documentation or converted to other formats.

## Examples

### Basic Scraping

1. **Extract all text from a webpage**:
   ```bash
   webwarden scrape text "https://example.com"
   ```

2. **Get all links from a webpage**:
   ```bash
   webwarden scrape links "https://example.com"
   ```

3. **Find all images on a webpage**:
   ```bash
   webwarden scrape images "https://example.com"
   ```

4. **Extract all tables from a webpage**:
   ```bash
   webwarden scrape tables "https://example.com"
   ```

### Advanced Scraping

1. **Save scraped data to a file**:
   ```bash
   webwarden scrape text "https://example.com" --output webpage_text.txt
   ```

2. **Scrape in JSON format**:
   ```bash
   webwarden scrape links "https://example.com" --format json
   ```

3. **Scrape in Markdown format**:
   ```bash
   webwarden scrape tables "https://example.com" --format md --output tables.md
   ```

### Crawling

1. **Crawl a website to depth 2**:
   ```bash
   webwarden crawl text "https://example.com" 2
   ```

2. **Crawl for images and save to JSON**:
   ```bash
   webwarden crawl images "https://example.com" 3 --format json --output crawled_images.json
   ```

### Comprehensive Scraping

1. **Get everything from a page**:
   ```bash
   webwarden scrape all "https://example.com"
   ```

2. **Get everything and save to a structured JSON file**:
   ```bash
   webwarden scrape all "https://example.com" --format json --output complete_scrape.json
   ```

## Configuration

WebWarden currently doesn't require a configuration file, but you can customize its behavior through command-line options.

### Environment Variables

None currently required.

### Configuration Files

None currently required.

## Dependencies

WebWarden depends on the following Python packages:

- **`playwright`**: For automating web browsers and rendering JavaScript-heavy pages
- **`beautifulsoup4`**: For parsing HTML and extracting data with ease
- **`rich`**: For creating beautiful and informative console output

These dependencies are automatically installed when you run `pip install -r requirements.txt`.

## Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: If you find a bug, please open an issue with a detailed description
2. **Suggest Features**: Have an idea for a new feature? Open an issue to discuss it
3. **Submit Pull Requests**: Feel free to fix bugs or implement new features

### Development Setup

1. Fork the repository
2. Clone your fork
3. Create a virtual environment
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
5. Make your changes
6. Test your changes
7. Submit a pull request

### Code Style

Follow PEP 8 guidelines for Python code. Use descriptive variable names and write clear docstrings for functions.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you see fit.

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```