from selenium import webdriver
import time

def products_by_category():
    print("Insert a name to search for: ")
    name = input()
    print("Loading...")
    browser = webdriver.Chrome()
    browser.get('https://www.toys-shop.gr/')

    # Search for a company e.x Playmobil
    search_icon = browser.find_element_by_xpath('//*[@id="header-search-btn-drop"]')
    search_icon.click()
    time.sleep(1)
    search_input = browser.find_element_by_xpath('//*[@id="search_widget"]/form/div[1]/input')
    search_input.send_keys(f'{name}')
    button = browser.find_element_by_xpath('//*[@id="search_widget"]/form/div[1]/button')
    button.click()

    # Short the prices in ascending order
    dropdown = browser.find_element_by_xpath('//*[@id="js-product-list-top"]/div/div[3]/div[1]/a')
    dropdown.click()
    time.sleep(5)
    sort_price = browser.find_element_by_xpath('//*[@id="js-product-list-top"]/div/div[3]/div[1]/div/a[5]')
    sort_price.click()

    # Create a dictionary with all products in the searched company e.x Playmobil
    # dictionary format: 'product_name' -> price
    d = {

    }
    time.sleep(5)
    while True:
        products = browser.find_elements_by_class_name('product-description')
        for i in range(len(products)):
            description = products[i].text.rsplit('\n')
            d[f'{description[3]}'] = f'{description[4]}' #change the format of the dict

        try:
            next_page = browser.find_element_by_id('infinity-url')
        except:
            print("No more pages")
            break
        next_page.click()
        time.sleep(5)
    return d

catalogue = products_by_category()

print(catalogue)






