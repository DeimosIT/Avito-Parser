import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

print ('Welcome back, Master <3')

print('some changes')


def get_page():
    
    options = webdriver.ChromeOptions()
    options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.660 YaBrowser/23.9.5.660 Yowser/2.5 Safari/537.36"')
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.avito.ru/yuzhno-sahalinsk/kvartiry/prodam-ASgBAgICAUSSA8YQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&f=ASgBAQICAUSSA8YQAUDKCCSAWYJZ')
        time.sleep(10)
        with open ('Source_selenium.html', 'w', encoding='UTF-8') as file:
            file.write(driver.page_source)
            file.close()
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

# Вывод стоимости квартир на первой странице
def get_data():

    with open('Source_selenium.html', encoding='UTF-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    price_all = soup.find_all('div', class_ = 'iva-item-priceStep-uq2CQ')
    for el in price_all:
        el = el.find('strong', class_ = 'styles-module-root-LIAav')
        print(el.text)


   

def main():
    #get_page()
    get_data()

if __name__ == '__main__':
    main()