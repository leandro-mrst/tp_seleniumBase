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

    def login(self):
        #abre a URL do site
        self.open(self.URL)
        #realiza o login
        self.wait_for_element('#user-name')
        self.send_keys('#user-name', self.USERNAME)
        self.click('#login-button')
        #aguarda a lista de produtos para garantir que o login foi bem sucedido
        self.wait_for_element('.inventory_list')
