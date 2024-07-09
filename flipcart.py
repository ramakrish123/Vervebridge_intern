import requests
from bs4 import BeautifulSoup
import pandas as pd

product_name = []
product_rating = []
product_reviews = []
product_prices = []

num_pages = 5  
for page in range(1, num_pages + 1):
    url = f"https://www.flipkart.com/search?q=mobiles&page={page}"
    r = requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    titles=soup.find_all('div',class_='KzDlHZ')
    ratings=soup.find_all('div',class_='XQDdHH')
    reviews=soup.find_all('span',class_='Wphh3N')
    prices=soup.find_all('div',class_='Nx9bqj _4b5DiR')
   
    for title in titles:
        product_name.append(title.text)

    for rating in ratings:
        product_rating.append(rating.text)

    for review in reviews:
        product_reviews.append(review.text.split('&')[0])

    for price in prices:
        product_prices.append(price.text)

    print(f"Page {page} scraped successfully.")


print(f"Titles: {len(product_name)}")
print(f"Ratings: {len(product_rating)}")
print(f"Reviews: {len(product_reviews)}")
print(f"Prices: {len(product_prices)}")

min_length = min(len(product_prices), len(product_name), len(product_rating), len(product_reviews))
product_name = product_name[:min_length]
product_rating = product_rating[:min_length]
product_reviews = product_reviews[:min_length]
product_prices = product_prices[:min_length]

data = {
    'Product Name': product_name,
    'Rating': product_rating,
    'Reviews': product_reviews,
    'Price': product_prices
}

model = pd.DataFrame(data)

model.to_csv("scrapedData.csv")

print("Data has been successfully scraped and saved to scrapedData.csv")
