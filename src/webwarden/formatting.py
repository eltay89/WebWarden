"""
Output formatting functionality for WebWarden.
"""

import json
from typing import Any, Dict, List

from rich.console import Console


def format_output(results: Any, format_type: str, console: Console) -> str:
    """Format the scraped or crawled data."""
    if format_type == 'json':
        # Remove the 'mode' key for cleaner JSON output
        if isinstance(results, list):
            for r in results:
                r.pop('mode', None)
        else:
            results.pop('mode', None)
        return json.dumps(results, indent=2, ensure_ascii=False)

    output_parts = []
    if isinstance(results, list):  # Crawl results
        for result in results:
            output_parts.append(f"--- Scraped: {result['url']} ---")
            output_parts.append(format_single_result(result, format_type, console))
    else:  # Scrape result
        output_parts.append(format_single_result(results, format_type, console))

    return "\n\n".join(output_parts)


def format_single_result(result: Dict[str, Any], format_type: str, console: Console) -> str:
    """Format a single scrape result."""
    data = result['data']
    mode = result['mode']

    if mode == 'all':
        return format_all_mode(data, format_type)

    if mode == 'tables':
        if format_type == 'md':
            return '\n\n'.join(format_table_md(table) for table in data)
        return '\n\n'.join(format_table_txt(table) for table in data)
    
    if isinstance(data, list):
        if format_type == 'md':
            return '\n'.join(f"- {item}" for item in data)
        return '\n'.join(str(item) for item in data)

    return str(data)


def format_all_mode(data: Dict[str, Any], format_type: str) -> str:
    """Formats the output for the 'all' mode."""
    output_parts = []
    if format_type == 'md':
        if data.get('text'):
            output_parts.append('### Text\n\n> '.replace('\n', '\n> ') + data['text'])
        if data.get('links'):
            output_parts.append('### Links\n\n' + '\n'.join(f"- {item}" for item in data['links']))
        if data.get('images'):
            output_parts.append('### Images\n\n' + '\n'.join(f"- {item}" for item in data['images']))
        if data.get('tables'):
            output_parts.append('### Tables\n\n' + '\n\n'.join(format_table_md(table) for table in data['tables']))
    else:  # txt format
        if data.get('text'):
            output_parts.append('--- Text ---\n\n' + data['text'])
        if data.get('links'):
            output_parts.append('--- Links ---\n\n' + '\n'.join(str(item) for item in data['links']))
        if data.get('images'):
            output_parts.append('--- Images ---\n\n' + '\n'.join(str(item) for item in data['images']))
        if data.get('tables'):
            output_parts.append('--- Tables ---\n\n' + '\n\n'.join(format_table_txt(table) for table in data['tables']))
    return '\n\n'.join(output_parts)


def format_table_md(table_data: List[List[str]]) -> str:
    """Format a table as Markdown."""
    md_table = []
    if not table_data:
        return ""
    headers = table_data[0]
    md_table.append(f"| {' | '.join(headers)} |")
    md_table.append(f"| {' | '.join(['---'] * len(headers))} |")
    for row in table_data[1:]:
        # Ensure all cells are strings
        md_table.append(f"| {' | '.join(map(str, row))} |")
    return "\n".join(md_table)


def format_table_txt(table_data: List[List[str]]) -> str:
    """Format a table as a simple text table."""
    return "\n".join("\t".join(map(str, row)) for row in table_data)