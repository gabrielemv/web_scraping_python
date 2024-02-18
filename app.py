'''
A ideia desse projeto é pegar informações de uma página web e alimentar uma planilha Excel
Neste exemplo, vamos acessar um site de uma loja de informática e extrair os dados (Títulos, preços)

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import pip 

driver = webdriver.Chrome()
driver.get("https://www.novaliderinformatica.com.br/computadores")

#extrair titulos
titulos = driver.find_elements(By.XPATH, "//a[@class='nome-produto']")
#extrair preços
precos = driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")

#criando a planilha
workbook = openpyxl.Workbook()
#criando a pág produtos
workbook.create_sheet('produtos')
#selecionar a pág produtos
sheet_produtos = workbook['produtos']

sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preços'


#inserir dados na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, preco.text])
workbook.save('produtos.xlsx')