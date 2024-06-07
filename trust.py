import time
from random import random

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


random_time_seed = random()


def check_tg2(valid_phones: list, driver):
    count = 0
    list_valid = []
    list_phones = valid_phones
    # --------------------------------------------------------------------
    driver.get("https://web.telegram.org/a/")
    time.sleep(3)
    #  Находим кнопку открывания меню
    WebDriverWait(driver, 15).until(ec.presence_of_element_located(
                                                        (By.CLASS_NAME, "ripple-container"))).click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[text()="Contacts"]').click()
    for phone in list_phones:
        time.sleep(random_time_seed + 1)
        #  Кликаем кнопку добавления контакта
        driver.find_element("css selector", 'button[title="Create New Contact"]').click()
        time.sleep(random_time_seed + 1)
        #  Кликаем кнопку, где вводится телефон
        phone_input = driver.find_element(By.XPATH, '//input[@aria-label="Phone Number"]')
        phone_input.click()
        phone_input.clear()
        phone_input.send_keys(phone)
        time.sleep(random_time_seed)
        #  Кликаем кнопку ввода имени
        name_input = driver.find_element(By.XPATH, '//input[@aria-label="First name (required)"]')
        name_input.click()
        name_input.clear()
        name_input.send_keys(phone)
        time.sleep(random_time_seed)
        #  Кликаем кнопку "Продолжить"
        driver.find_element(By.XPATH, '//button[text()="Done"]').click()

        #  Проверка на вывод сообщения: Такого контакта нет в телеграм
        try:
            WebDriverWait(driver, 4).until(ec.presence_of_element_located(
                (By.CLASS_NAME, 'Notification-container')))
            driver.find_element(By.XPATH, '//button[text()="Cancel"]').click()
            list_valid.append(phone)
            print(f"Нет контакта {phone}")
        except TimeoutException:
            pass

    time.sleep(2)
    return list_valid