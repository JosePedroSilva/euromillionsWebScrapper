import requests
from bs4 import BeautifulSoup


URL = 'https://www.jogossantacasa.pt/web/SCCartazResult/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

# Requests the numbers to URL and returns raw HTML
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Find the winning numbers and convert them into a list
result = soup.find(attrs="colums").get_text()
r = (result.replace('+', '').strip())

try:
    result_comp = list(map(int, r.split()))
    result_comp = result_comp[0:7]
    numbers = result_comp[0:5]
    stars = result_comp[5:]
except ValueError:
    print('Unble to convert into list.')

print(numbers)
print(stars)
