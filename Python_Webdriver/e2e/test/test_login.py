from selenium import webdriver
from e2e.page_object.login_page import LoginPage
from e2e.page_object.product_page import ProductsPage
import unittest


class Autenticacao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../driver/chromedriver")
        self.driver.maximize_window()
        self.driver.get("http://www.saucedemo.com/")
        self.driver.implicitly_wait(30)

    def test_login_sucesso(self):
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        self.assertTrue(login_page.validar_pagina_login())
        login_page.autenticacao("standard_user","secret_sauce")
        self.assertTrue(products_page.validar_carrinho_compra())

    def test_login_password_vazio(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.validar_pagina_login())
        login_page.autenticacao("standard_user", "")
        self.assertEqual("Epic sadface: Password is required", login_page.validar_mensagem_erro())


    def test_login_password_incorreto(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.validar_pagina_login())
        login_page.autenticacao("standard_user", "usuario06")
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", login_page.validar_mensagem_erro())


    def test_login_username_invalido(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.validar_pagina_login())
        login_page.autenticacao("Antonio", "secret_sauce")
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", login_page.validar_mensagem_erro())

    def test_login_username_locked(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.validar_pagina_login())
        login_page.autenticacao("locked_out_user", "secret_sauce")
        self.assertEqual("Epic sadface: Sorry, this user has been locked out.", login_page.validar_mensagem_erro())

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
