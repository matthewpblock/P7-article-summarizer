import requests
from bs4 import BeautifulSoup
import time
import os

# Define the URL of the main collection page
COLLECTION_URL = "https://nickkuchar.com/collections/oahu"
BASE_URL = "https://nickkuchar.com"
OUTPUT_FILENAME = "nlp_analysis_data.html"

def scrape_product_links(url):
    """
    Fetches the collection page and extracts the URLs for each product.
    
    Args:
        url (str): The URL of the collection page.

    Returns:
        list: A list of full URLs for each product.
    """
    print(f"Fetching product links from: {url}")
    product_links = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all product cards. The previous selector was incorrect.
        # This has been updated based on the user's feedback.
        product_card_elements = soup.find_all('a', class_='product-card__title')
        
        # Extract the href attribute from each card element
        for link in product_card_elements:
            href = link.get('href')
            if href:
                # Ensure the link is a full URL
                full_url = BASE_URL + href
                product_links.append(full_url)
                
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the collection page: {e}")
    
    print(f"Found {len(product_links)} product links.")
    return product_links

def scrape_product_details(url):
    """
    Fetches a single product page and extracts the title and description.
    
    Args:
        url (str): The URL of the product page.

    Returns:
        tuple: A tuple containing the title (str) and description (str).
               Returns (None, None) if scraping fails.
    """
    print(f"  Scraping details from: {url}")
    title = "N/A"
    description = "N/A"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the product title.
        title_element = soup.find('h1', class_='product__title')
        if title_element:
            title = title_element.get_text(strip=True)
            
        # Find the product description. The user specified "tab__content rte".
        description_element = soup.find('div', class_='tab__content rte')
        if description_element:
            # We want the text content for NLP, not the HTML tags.
            description = description_element.get_text(strip=True, separator='\n')
            
    except requests.exceptions.RequestException as e:
        print(f"  Error scraping details from {url}: {e}")
        
    return title, description

def save_to_html(data, filename):
    """
    Saves the scraped data to a single HTML file.
    
    Args:
        data (list): A list of dictionaries, where each dict contains 'title' and 'description'.
        filename (str): The name of the output HTML file.
    """
    print(f"\nWriting scraped data to {filename}...")
    
    # Simple HTML structure to hold the data
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nick Kuchar - Oahu Collection Data for NLP</title>
    <style>
        body { font-family: sans-serif; line-height: 1.6; padding: 20px; }
        .product-entry { border-bottom: 1px solid #ccc; margin-bottom: 20px; padding-bottom: 20px; }
        h2 { color: #333; }
        p { color: #666; }
    </style>
</head>
<body>
    <h1>Nick Kuchar - Oahu Collection Data for NLP</h1>
"""
    
    for item in data:
        html_content += f"""
    <div class="product-entry">
        <h2>{item['title']}</h2>
        <p>{item['description']}</p>
    </div>
"""
    
    html_content += """
</body>
</html>
"""
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Successfully saved data to {os.path.abspath(filename)}")
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    """Main function to run the web scraping process."""
    
    # Scrape all product links from the collection page
    product_links = scrape_product_links(COLLECTION_URL)
    
    scraped_data = []
    
    # Scrape details for each product link
    for link in product_links:
        title, description = scrape_product_details(link)
        if title != "N/A" and description != "N/A":
            scraped_data.append({
                'title': title,
                'description': description
            })
        
        # Add a small delay to be polite to the server
        time.sleep(1)
        
    # Save the combined data to an HTML file
    if scraped_data:
        save_to_html(scraped_data, OUTPUT_FILENAME)
    else:
        print("No data was scraped. The output file will not be created.")

if __name__ == "__main__":
    main()
