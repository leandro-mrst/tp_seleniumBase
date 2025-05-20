from seleniumbase import BaseCase
import csv

class SauceDemoScraper(BaseCase):
    URL = 'https://www.saucedemo.com/'
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'
    FIRST_NAME = 'Trainee'
    LAST_NAME = 'PiJunior'
    ZIP_CODE = '31270-901'
    CSV_FILE = 'products.csv'

    #função para realizar o login
    def login(self): 
        #abre a URL do site
        self.open(self.URL)
        #realiza o login
        self.wait_for_element('#user-name')
        self.send_keys('#user-name', self.USERNAME)
        self.click('#login-button')
        #aguarda a lista de produtos para garantir que o login foi bem sucedido
        self.wait_for_element('.inventory_list')

    def extract_products(self): #função para extrair nome, descrição e preço dos produtos disponíveis
        products = self.find_element('.inventory_item')
        extracted = [] 
        for item in products:
            name = item.find_element('.inventory_item_name').text
            description = item.find_element('.inventory_item_desc').text
            price = item.find_element('.inventory_item_price').text
            extracted.append({
                'nome': name,
                'descrição': description,
                'preço': price,
            })
        return extracted

