# Blog Post Scraper

This Python script scrapes blog posts from a specified blog page and saves them into a single `.txt` file. It extracts both the titles and content of the posts and writes them sequentially to the output file with a clear separator between each post.

## Features

- **Single Output File**: All posts are saved into one `all_posts.txt` file.
- **Automatic Post Scraping**: The script automatically finds and scrapes all the post links from the provided blog page.
- **Error Handling**: The script skips any post links that are invalid or cannot be fetched.
  
## Prerequisites

Make sure to have the following installed:

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries with the following commands:

```bash
pip install requests beautifulsoup4
```

## Setup and Usage

1. **Download/Clone this repository**.

2. **Update the `base_url`** in the script to point to the blog page you want to scrape:

    ```python
    base_url = 'https://akansya.blogspot.com/p/blog-page_5877.html'
    ```

3. **Run the script**:

    ```bash
    python blog_scraper.py
    ```
