import requests
from bs4 import BeautifulSoup

# Fetch webpage content
url = 'http://books.toscrape.com/'
response = requests.get(url)

# Check if request was successful
if response.status_code != 200:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
    exit()

# Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract book names
book_names = []
for book in soup.find_all('article', class_='product_pod'):
    # The book name is in the alt attribute of the image
    img_tag = book.find('img')
    if img_tag and 'alt' in img_tag.attrs:
        book_names.append(img_tag['alt'])
    
    # Alternative: Get from the title attribute of the <a> tag
    # link = book.find('a')
    # if link and 'title' in link.attrs:
    #     book_names.append(link['title'])

# Print book names
print("Book Names Found:")
print("-" * 50)
for i, name in enumerate(book_names, 1):
    print(f"{i}. {name}")
print("-" * 50)
print(f"Total books found: {len(book_names)}")