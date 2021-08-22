from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get(url="https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22paginatio"
                            "n%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3"
                            "A%7B%22west%22%3A-122.47263945532227%2C%22east%22%3A-122.3670677084961%2C%22south%22%3A37."
                            "75710750070999%2C%22north%22%3A37.86587309671784%7D%2C%22regionSelection%22%3A%5B%7B%22re"
                            "gionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterSta"
                            "te%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%"
                            "22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22valu"
                            "e%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afa"
                            "lse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%"
                            "2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%"
                            "3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D", headers=header)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

links_object = soup.select(".list-card-top a")

links = []
for n in links_object:
    link = n.get("href")
    if 'http' not in link:
        links.append(f"https://www.zillow.com{link}")
    else:
        links.append(link)
print(links)

prices_object = soup.select(".list-card-price")
prices = []
for n in prices_object:
    price = n.text.split()[0][1:6]
    prices.append(price)
print(prices)

adress_object = soup.select(".list-card-addr")
adresses = [n.text for n in adress_object]
print(adresses)

chrome_driver_path = "YOUR DRIVER PATH"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

for n in range(0, len(adresses)):
    driver.get("PUT GOOGLE FORM ADRESS HERE")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(adresses[n])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(prices[n])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links[n])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()
    time.sleep(1)

