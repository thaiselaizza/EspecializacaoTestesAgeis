from e2e.utils.definition import BasePage
from selenium.webdriver.common.by import By
from e2e.page_factory.page_locator import ProductPageLocator

class ProductsPage(BasePage):

    def validar_carrinho_compra(self):
        carrinho = self.driver.find_element(By.ID, ProductPageLocator.CARRINHO)
        #self.driver.find_element(By.ID, ProductPageLocator.CARRINHO)
        return carrinho

