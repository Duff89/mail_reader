import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_chrome import ChromeBrowser
from mail_service import MailRead


class LebedevRegister:
    def __init__(self, mail:str, password:str):
        self.mail = mail
        self.password = password
        self.driver = ChromeBrowser().get_driver()

    def register(self):
        self.driver.get('https://www.artlebedev.ru/')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".als-header-2021-buttons-login"))).click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".als-login__auth-link")))
        self.driver.find_elements(By.CSS_SELECTOR, ".als-login__auth-link")[1].click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".als-login__form-field_last")))
        self.driver.find_element(By.CSS_SELECTOR, ".als-login__form-field_last").send_keys(self.mail)

        time.sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR, ".als-login__form-button").click()
        time.sleep(5)
        password_from_mail = MailRead(self.mail, self.password).get_password()
        print(f"Почта: {self.mail}"
              f"Пароль: {password_from_mail}")


if __name__ == '__main__':
    LebedevRegister(mail='*@rambler.ru', password='Test12345').register()




