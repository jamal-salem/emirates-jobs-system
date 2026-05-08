import requests
from bs4 import BeautifulSoup

url = "https://ers.adpolice.gov.ae"

try:

    response = requests.get(url)

    print(f"\nStatus Code: {response.status_code}\n")

    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.prettify()[:5000])

except Exception as e:

    print("Error:")
    print(e)
