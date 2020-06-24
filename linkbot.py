from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import time

def home(usuario,senha,tag,mensagem):
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    user = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    user.send_keys(usuario)
    password.send_keys(senha)
    password.send_keys(Keys.RETURN)
    time.sleep(10)
    contador = 1
    while contador < 5:
        search = "https://www.linkedin.com/search/results/people/?keywords={}&origin=GLOBAL_SEARCH_HEADER&page={}".format(tag, contador)
        driver.get(search)
        resultado = driver.find_elements_by_class_name('search-result__wrapper')
        time.sleep(5)

        for i in resultado:
            with open('perfis.txt', 'a') as arquivo:
                time.sleep(5)
                conteudo = i.find_element_by_class_name('ember-view').get_attribute("href")
                arquivo.writelines("{} \n".format(conteudo))
            arquivo = open('perfis.txt').read().splitlines()
        contador = contador + 1
    else:

        for perfilador in arquivo:
            driver.get(perfilador)
            conexion2 = driver.find_elements_by_xpath("//span[text()='Conectar']")

            if conexion2:
                conexion2 = driver.find_elements_by_xpath("//span[text()='Conectar']")[0].click()
                ember = driver.find_elements_by_xpath("//span[text()='Adicionar nota']")[0].click()
                message = driver.find_element_by_id("custom-message")
                message.send_keys(mensagem)
                ember = driver.find_elements_by_xpath("//span[text()='Concluído']")[0].click()
            else:
                continue

######################################################################################################################

usuario = input("Insira seu email: ")
senha = input("Insira sua senha: ")
tag = input("Insira a skill do profissional: ")
mensagem = input("Envie a mensagem de convite: ")


home(usuario,senha,tag,mensagem)
