import datetime
import random
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scraper:
    def __init__(self, data, result,driver):
        self.data = data
        self.result = result
        self.driver = driver

    def run(self):
        date = str(datetime.datetime.now().date())
        if date not in self.result.keys():



            try:
                login_url = "https://ng.ezxearn.com/sign/up?invite_code=6591249"
                self.driver.get(login_url)


                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']")))


                phone_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='number']")
                phone_input.send_keys(self.data["phone"])


                password_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
                password_input.send_keys(self.data["password"])


                confirm_password_input = self.driver.find_elements(By.CSS_SELECTOR, "input[type='password']")[1]
                confirm_password_input.send_keys(self.data["password"])



                submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                submit_button.click()


                time.sleep(5)


            except Exception as e:
                print(str(e))
            finally:

                print("end")
        else:
            print("Not run")


if __name__ == '__main__':
    result = {}
    sequence_precise = '997'
    options = Options()
    # options.add_argument('--headless')
    driver = Chrome(options=options)
    # Generate 20 sets of data
    for _ in range(100):
        phone_number = '9745'.join([str(random.randint(10, 20))]).join([str(random.randint(100, 200))])
        chiffres_restants = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        phone_number = sequence_precise + chiffres_restants
        data = {
            "phone": phone_number,
            "password": phone_number,
        }
        scraper = Scraper(data, result,driver)
        scraper.run()
        driver.delete_all_cookies()
    driver.quit()
