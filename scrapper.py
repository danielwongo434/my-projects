# Scrape inspirational quotes using python
from bs4 import BeautifulSoup
import requests

# Create lists to store the scrape data
authors = []
quotes = []

URL = 'https://www.goodreads.com/quotes?page=2'
webpage = requests.get(URL)  # make a request from the website
soup = BeautifulSoup(webpage.text, 'html.parser')  # Parse the text from the website
quoteText = soup.find_all('div', attrs={'class': 'quoteText'})

# Show quoteText

for i in quoteText:
    quote = (i.text.strip().split('\n')[0])  # Print all of the quotes on this webpage
    #print(quote)
    author = i.find('span', attrs={'class': 'authorOrTitle'}).text.strip()
    #print(author)


# Create a function to scrape the website
def scrape_website(page_number):
    page_num = str(page_number)
    URL = 'https://www.goodreads.com/quotes?page=' + page_num
    webpage = requests.get(URL)  # make a request from the website
    soup = BeautifulSoup(webpage.text, 'html.parser')  # Parse the text from the website
    quoteText = soup.find_all('div', attrs={'class': 'quoteText'})

    for i in quoteText:
        quote = (i.text.strip().split('\n')[0])  # Print all of the quotes on this webpage
        author = i.find('span', attrs={'class': 'authorOrTitle'}).text.strip()
        quotes.append(quote)
        authors.append(author)


# loop and scrape the website
n = 10
for num in range(0, n):
    scrape_website(num)
combined_list = []
for i in range(len(quotes)):
    combined_list.append(quotes[i] + '-' + authors[i])

print(combined_list)
