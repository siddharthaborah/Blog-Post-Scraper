import requests
from bs4 import BeautifulSoup

# URL of the blog page you want to scrape
base_url = 'https://akansya.blogspot.com/p/blog-page_5877.html'

# Send a GET request to fetch the main page content
response = requests.get(base_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the main page HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Open a single file to save all posts
    with open('all_posts.txt', 'w', encoding='utf-8') as file:

        # Find all the post links (adjust the tag and class based on the website structure)
        post_links = soup.find_all('a')  # Adjust this part according to the structure (look for specific class or container)

        for idx, link in enumerate(post_links, 1):
            post_url = link.get('href')  # Get the post link
            post_title = link.get_text()  # Get the post title

            # Skip links that are not actual post links
            if not post_url or 'http' not in post_url:
                continue

            print(f"Scraping Post {idx}: {post_title}")
            
            # Fetch the content of each post
            post_response = requests.get(post_url)
            if post_response.status_code == 200:
                post_soup = BeautifulSoup(post_response.content, 'html.parser')
                
                # Extract the post text (adjust the tag/class based on post structure)
                post_content = post_soup.get_text(separator='\n')  # Adjust this to get the main content of the post
                
                # Write the title and content of each post to the single file
                file.write(f"Post {idx}: {post_title}\n")
                file.write(post_content)
                file.write("\n" + "-"*50 + "\n")  # Separator between posts
                
            else:
                print(f"Failed to fetch post {idx}")

else:
    print(f"Failed to retrieve the main blog page. Status code: {response.status_code}")
