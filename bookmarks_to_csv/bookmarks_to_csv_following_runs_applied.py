import sys
import csv
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from dateutil.relativedelta import relativedelta
from datetime import datetime

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
jobs_header = soup.find('h3', string='Jobs applied for')

if jobs_header:
    # Find bookmarks under the 'Jobs applied for' folder
    job_bookmarks = jobs_header.find_next('dl').find_all('a')
   

    # List to hold new job details
    new_jobs = []
    print("New Jobs:")
    print()

    # Extract and filter job details
    for bookmark in job_bookmarks:
        bookmark_title = bookmark.text  # Bookmark title (job title)
        bookmark_url = bookmark['href']  # Bookmark URL (job URL)

        # Extract company name from URL and capitalize it
        parsed_url = urlparse(bookmark_url)
        netloc_parts = parsed_url.netloc.split('.')
        domain_parts = [part for part in netloc_parts if part not in ['www', 'http', 'https']]
        company_name = domain_parts[0].capitalize() if domain_parts else "Company name not found"

        # Set the close date to 1 month from today
        today = datetime.now()
        close_date = today + relativedelta(months=1)
        close_date_str = close_date.strftime("%Y-%m-%d")

        # Check for unique URL in the existing CSV
        with open(output_csv_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            existing_urls = {row[2] for row in reader}
            if bookmark_url not in existing_urls:
                new_jobs.append([company_name, bookmark_title, bookmark_url, close_date_str, "Applied"])
                print([company_name, bookmark_title, bookmark_url, close_date_str, "Applied"])
                print()

    # Append new job details to the CSV
    with open(output_csv_path, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([])
        for job in new_jobs:
            csv_writer.writerow(job)
    print("CSV updated.")
else:
    print("Folder 'Jobs applied for' not found or structure doesn't match.")
