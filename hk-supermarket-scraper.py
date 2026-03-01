from bs4 import BeautifulSoup
import requests
import json

url  = "https://www.wellcome.com.hk/zh-hant/store_locator"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Successfully fetched the webpage. status code:", response.status_code)
elif response.status_code != 200:
    print("Failed to fetch the webpage. status code:", response.status_code)
    
htmltext = response.text
with open('response.html', 'w', encoding='utf-8') as f:
    f.write(htmltext)

print("HTML content saved to response.html")    
soup = BeautifulSoup(response.text, 'html.parser')
all_addresses = soup.find_all('div', attrs={'class': 'address'})
address_list = []
for address in all_addresses:
    if address.text.strip() not in address_list:
        address_list.append(address.text.strip())

print("successfully extracted all addresses of wellcome supermarket. total number of addresses:", len(address_list))
while True:
    user_input = input("Enter 'exit' to quit\nEnter NT to show supermarket addresses in New Territories\nEnter HK to show supermarket addresses in Hong Kong Island\nEnter KL to show supermarket addresses in Kowloon\nEnter all to show all supermarket addresses \n")
    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    elif user_input.lower() == 'nt':
        print("Supermarket addresses in New Territories:")
        for address in address_list:
            if "新界" in address:
                print(address)  
    elif user_input.lower() == 'hk':
        print("Supermarket addresses in Hong Kong Island:")
        for address in address_list:
            if "香港島" in address:
                print(address)
    elif user_input.lower() == 'kl':            
        print("Supermarket addresses in Kowloon:")
        for address in address_list:
            if "九龍" in address:
                print(address)
    elif user_input.lower() == 'all':            
        print("All supermarket addresses:")
        for address in address_list:
            print(address)