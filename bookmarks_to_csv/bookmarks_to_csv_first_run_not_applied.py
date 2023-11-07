import csv
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from dateutil.relativedelta import relativedelta
from datetime import datetime

import sys

if len(sys.argv) != 3:
    print("Usage: python script_name.py input_html_path output_csv_path")
    sys.exit(1)

html_file_path = sys.argv[1]
output_csv_path = sys.argv[2]

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the element using the provided XPath
jobs_header = soup.find('h3', string='Jobs to look at')

if jobs_header:
    # Find bookmarks under the 'Jobs applied for' folder
    job_bookmarks = jobs_header.find_next('dl').find_all('a')

    # Create or open a CSV file to write data
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header row including the new column
        csv_writer.writerow(['Company Name', 'Job Title', 'Job URL', 'Stage'])

        # Extract and write job details to CSV
        for bookmark in job_bookmarks:
            bookmark_title = bookmark.text  # Bookmark title (job title)
            bookmark_url = bookmark['href']  # Bookmark URL (job URL)

            # Extract company name from URL and capitalize it
            parsed_url = urlparse(bookmark_url)
            netloc_parts = parsed_url.netloc.split('.')
            domain_parts = [part for part in netloc_parts if part not in ['www', 'http', 'https']]
            company_name = domain_parts[0].capitalize() if domain_parts else "Company name not found"

            # Set the Stage as "Open - Not Yet Applied"
            stage = "Open - Not Yet Applied"

            # Write job details to CSV along with the Closed Date and Stage
            csv_writer.writerow([company_name, bookmark_title, bookmark_url, stage])
    print("CSV created.")
else:
    print("Folder 'Jobs to look at' not found or structure doesn't match.")
