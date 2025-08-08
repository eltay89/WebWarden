"""
Core scraping and crawling functionality for WebWarden.
"""

import json
import sys
import time
from typing import List, Dict, Any, Optional, Tuple, Set
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, Page, Browser, Playwright


def get_page_html(p: Playwright, url: str) -> Optional[str]:
    """Launch a browser and retrieve the HTML content of a URL."""
    try:
        browser: Browser = p.chromium.launch(headless=True)
        page: Page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded")
        html: str = page.content()
        browser.close()
        return html
    except Exception as e:
        print(f"Error getting page HTML for {url}: {e}", file=sys.stderr)
        return None


def scrape_data(url: str, html: str, mode: str) -> Optional[Dict[str, Any]]:
    """Scrape data from HTML content based on the specified mode."""
    soup = BeautifulSoup(html, 'html.parser')
    data: Any = None

    try:
        if mode == 'text':
            data = soup.get_text(separator='\\n', strip=True)
        elif mode == 'links':
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            data = [urljoin(url, link) for link in links]
        elif mode == 'images':
            images = [img.get('src') for img in soup.find_all('img', src=True)]
            data = [urljoin(url, img) for img in images]
        elif mode == 'tables':
            tables_data = []
            tables = soup.find_all('table')
            for table in tables:
                rows = []
                for tr in table.find_all('tr'):
                    cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                    if cells:
                        rows.append(cells)
                if rows:
                    tables_data.append(rows)
            data = tables_data
        elif mode == 'all':
            all_data = {}
            # Scrape text
            all_data['text'] = soup.get_text(separator='\\n', strip=True)
            # Scrape links
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            all_data['links'] = [urljoin(url, link) for link in links]
            # Scrape images
            images = [img.get('src') for img in soup.find_all('img', src=True)]
            all_data['images'] = [urljoin(url, img) for img in images]
            # Scrape tables
            tables_data = []
            tables = soup.find_all('table')
            for table in tables:
                rows = []
                for tr in table.find_all('tr'):
                    cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                    if cells:
                        rows.append(cells)
                if rows:
                    tables_data.append(rows)
            all_data['tables'] = tables_data
            data = all_data
        else:
            raise ValueError(f"Unknown mode: {mode}")
        return {'url': url, 'data': data, 'mode': mode}
    except ValueError as e:
        print(e, file=sys.stderr)
        return None


def crawl_pages(start_url: str, depth: int, mode: str) -> List[Dict[str, Any]]:
    """Crawl pages starting from start_url up to a specified depth."""
    visited: Set[str] = set()
    to_visit: List[Tuple[str, int]] = [(start_url, 0)]
    results: List[Dict[str, Any]] = []
    domain = urlparse(start_url).netloc

    with sync_playwright() as p:
        while to_visit:
            url, current_depth = to_visit.pop(0)
            if url in visited or current_depth > depth:
                continue

            if urlparse(url).netloc != domain:
                continue

            print(f"Crawling: {url} at depth {current_depth}", file=sys.stderr)
            html = get_page_html(p, url)
            if not html:
                continue

            result = scrape_data(url, html, mode)
            if result:
                results.append(result)
                visited.add(url)

                if current_depth < depth:
                    soup = BeautifulSoup(html, 'html.parser')
                    links = [urljoin(url, a.get('href')) for a in soup.find_all('a', href=True)]
                    for link in links:
                        if link not in visited:
                            to_visit.append((link, current_depth + 1))

            time.sleep(1)  # Be polite to servers

    return results