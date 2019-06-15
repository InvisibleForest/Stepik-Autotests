from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(5)

#ниже блок для бронирования
button = browser.find_element_by_id("book")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
        )
button.click()

#ниже блок для получения числа и отправки ответа
y_input = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", y_input)
x = browser.find_element_by_id("input_value").text
y = calc(x)
y_input.send_keys(y)
browser.find_element_by_id('solve').click()
