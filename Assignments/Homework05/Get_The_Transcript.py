import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.presidency.ucsb.edu/documents/presidential-debate-philadelphia-pennsylvania"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all paragraph tags
    paragraphs = soup.find_all('p')
    
    # Extract and print the text from each paragraph
    for p in paragraphs:
        print(p.get_text())
else:
    print("Failed to retrieve the page. Status code:", response.status_code)

# Save the transcript to a text file
with open("transcript.txt", "w") as file:
    for p in paragraphs:
        file.write(p.get_text() + "\n")


