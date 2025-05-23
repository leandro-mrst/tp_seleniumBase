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

    #função para extrair nome, descrição e preço dos produtos e armazenar em uma lista
    def extract_products(self):
        products = self.find_element('.inventory_item')
        extracted = [] 
        #loop para pegar os dados de todos os produtos
        for item in products:
            name = item.find_element('.inventory_item_name').text
            description = item.find_element('.inventory_item_desc').text
            price = item.find_element('.inventory_item_price').text
            #adição dos dados na lista
            extracted.append({
                'nome': name,
                'descrição': description,
                'preço': price,
            })
        return extracted
        
    #função pra salvar dados em um arquivo .csv    
    def save_to_csv(self, products):
        if not products:
            print("Nenhum dado para salvar.")
            return
        
        with open(self.CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'description', 'price'])
            writer.writeheader()
            #loop para escrever linha no CSV com valores daquele produto, seguindo as colunas
            for prod in products:
                writer.writerow(prod)
        print(f"Dados salvos em {self.CSV_FILE}")
        
    #função para adicionar todos os produtos ao carrinho
    def add_all_to_cart(self):
        buttons = self.find_elements('.inventory_item button')
        #loop para clicar em cada botão encontrado na lista .inventory_item button
        for bot in buttons:
            bot.click()
        self.click('.shopping_cart_link')
        self.wait_for_element('.cart_list')

