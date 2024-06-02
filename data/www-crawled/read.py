

import requests
from bs4 import BeautifulSoup
from readability.readability import Document
import html2text
import time
import random
from fake_useragent import UserAgent

# Generate a random user agent
ua = UserAgent()

# Define the URL of the website to scrape
url = 'https://www.yogapedia.com/yoga-poses/dragonfly-pose'
# Define headers to mimic a real browser request
headers = {
    'User-Agent': ua.random,
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# Send a GET request to the website with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Introduce a random delay to mimic human behavior
    time.sleep(random.uniform(1, 3))

    # Parse the HTML content of the page
    html_content = response.content

    # Use Readability to extract the main content
    doc = Document(html_content)
    main_content_html = doc.summary()
    title = doc.title()

    # Use html2text to convert the extracted main content to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False  # Set to True if you want to ignore links
    main_content_markdown = h.handle(main_content_html)

    # Print the title and the main content in Markdown format
    print("# " + title)
    print(main_content_markdown)
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')