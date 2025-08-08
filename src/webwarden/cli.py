"""
Command-line interface for WebWarden.
"""

import argparse
import sys
from typing import Any

from rich.console import Console

from .core import get_page_html, scrape_data, crawl_pages, sync_playwright
from .formatting import format_output


def main():
    """Main function to handle command-line arguments and execution."""
    parser = argparse.ArgumentParser(
        description="WebWarden: A CLI tool for web scraping and crawling.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scrape all text from a webpage
  webwarden scrape text https://example.com

  # Scrape all images and save to JSON file
  webwarden scrape images https://example.com --format json --output images.json

  # Crawl a website for links up to depth 2
  webwarden crawl links https://example.com 2

  # Scrape everything from a page and save to markdown
  webwarden scrape all https://example.com --format md --output everything.md
        """
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Scrape command
    scrape_parser = subparsers.add_parser('scrape', help='Scrape data from a single page')
    scrape_parser.add_argument('mode', choices=['text', 'links', 'images', 'tables', 'all'], help='Data type to extract')
    scrape_parser.add_argument('url', help='URL of the page to scrape')
    scrape_parser.add_argument('--format', choices=['txt', 'json', 'md'], default=None, help='Output format')
    scrape_parser.add_argument('--output', help='File to save output (default: stdout)')

    # Crawl command
    crawl_parser = subparsers.add_parser('crawl', help='Crawl multiple pages starting from a URL')
    crawl_parser.add_argument('mode', choices=['text', 'links', 'images', 'tables', 'all'], help='Data type to extract')
    crawl_parser.add_argument('url', help='Starting URL for crawling')
    crawl_parser.add_argument('depth', type=int, nargs='?', default=1, help='Crawling depth (default: 1)')
    crawl_parser.add_argument('--format', choices=['txt', 'json', 'md'], default=None, help='Output format')
    crawl_parser.add_argument('--output', help='File to save output (default: stdout)')

    args = parser.parse_args()
    console = Console()

    format_type = args.format if args.format else ('json' if args.mode == 'all' else 'txt')

    output = ""
    if args.command == 'scrape':
        with sync_playwright() as p:
            html = get_page_html(p, args.url)
            if not html:
                sys.exit(1)
            result = scrape_data(args.url, html, args.mode)
            if result:
                output = format_output(result, format_type, console)
    else:  # crawl
        results = crawl_pages(args.url, args.depth, args.mode)
        if results:
            output = format_output(results, format_type, console)
        else:
            print("No data collected during crawl.", file=sys.stderr)
            sys.exit(1)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        console.print(f"[bold green]Output successfully saved to {args.output}[/bold green]")
    else:
        console.print(output)


if __name__ == "__main__":
    main()