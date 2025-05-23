# GRUPO PYTHON 5, TRAINEE PIJR;
# LEANDRO, LUANA e RAPHAEL;

from seleniumbase import BaseCase
import csv

class RaspaProdutos(BaseCase):
    SITE = 'https://www.saucedemo.com/'
    USUARIO = 'standard_user'
    SENHA = 'secret_sauce'
    NOME = 'Trainee'
    SOBRENOME = 'PiJunior'
    CEP = '31270-901'
    ARQUIVO_CSV = 'produtos.csv'

    def fazer_login(self):
        self.open(self.SITE)
        self.driver.maximize_window()
        self.open(self.SITE)
        self.wait_for_element('#user-name')
        self.send_keys('#user-name', self.USUARIO)
        self.send_keys('#password', self.SENHA)
        self.click('#login-button')
        self.wait_for_element('.inventory_list')

    def extrair_produtos(self):
        lista = []
        itens = self.find_elements('.inventory_item')
        for item in itens:
            nome = item.find_element("css selector", '.inventory_item_name').text
            descricao = item.find_element("css selector", '.inventory_item_desc').text
            preco = item.find_element("css selector", '.inventory_item_price').text
            lista.append({
                'nome': nome,
                'descricao': descricao,
                'preco': preco
            })
        return lista

    def salvar_csv(self, produtos):
        with open(self.ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=['nome', 'descricao', 'preco'])
            escritor.writeheader()
            for produto in produtos:
                escritor.writerow(produto)
        print(f"Dados salvos em {self.ARQUIVO_CSV}")

    def adicionar_ao_carrinho(self):
        botoes = self.find_elements('.inventory_item button')
        for botao in botoes:
            botao.click()
        self.click('.shopping_cart_link')
        self.wait_for_element('.cart_list')

    def preencher_checkout(self):
        self.click('#checkout')
        self.wait_for_element('#first-name')
        self.send_keys('#first-name', self.NOME)
        self.send_keys('#last-name', self.SOBRENOME)
        self.send_keys('#postal-code', self.CEP)
        self.click('#continue')
        self.wait_for_element('.summary_info')

    def raspar_resumo(self):
        pagamento = self.find_element('xpath', "(//div[@class='summary_value_label'])[1]").text
        entrega = self.find_element('xpath', "(//div[@class='summary_value_label'])[2]").text
        total = self.find_element('.summary_total_label').text
        print('=== Resumo do Pedido ===')
        print(f'Meio de pagamento: {pagamento}')
        print(f'Forma de entrega: {entrega}')
        print(f'{total}')

    def finalizar_pedido(self):
        self.click('#finish')
        self.wait_for_element('.complete-header')
        mensagem = self.find_element('.complete-header').text
        print(f'Mensagem de confirmação: {mensagem}')

    def test_fluxo_completo(self):
        self.fazer_login()
        produtos = self.extrair_produtos()
        self.salvar_csv(produtos)
        self.adicionar_ao_carrinho()
        self.preencher_checkout()
        self.raspar_resumo()
        self.finalizar_pedido()