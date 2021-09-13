from e2e.utils.definition import BasePage
from selenium.webdriver.common.by import By
from e2e.page_factory.page_locator import LoginPageLocator

class LoginPage(BasePage):

    def validar_pagina_login(self):
        pagina_login = self.driver.find_element(By.XPATH, LoginPageLocator.IMG_ROBO)
        return pagina_login

    def autenticacao(self, str_username, str_password):
        self.driver.find_element(By.XPATH, LoginPageLocator.USERNAME_CAMPO).send_keys(str_username)
        self.driver.find_element(By.XPATH, LoginPageLocator.PASSWORD_CAMPO).send_keys(str_password)
        self.driver.find_element(By.XPATH, LoginPageLocator.LOGIN_BOTAO).click()

    def validar_mensagem_erro(self):
        msg_erro = self.driver.find_element(By.XPATH, LoginPageLocator.MSG_ERRO).text
        return msg_erro