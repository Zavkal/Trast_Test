import time
import config
from trust import check_tg2

from selenium import webdriver

# Создаем экземпляр опций Chromium
chrome_options = webdriver.ChromeOptions()

# Указываем путь к исполняемому файлу ChromeDriver
if len(config.path_chrome) > 0:
    chrome_options.binary_location = config.path_chrome


print("Программа запущена.")
list_contact = []
with open("contacts.txt", "r") as f:
    numbers = f.readlines()
    for i in numbers:
        list_contact.append(i.strip())

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/live/snap/chromium/common/chromium")
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(options=options)
print("Начало работы.")
check_tg2(valid_phones=list_contact, driver=driver)
driver.quit()
driver.close()
print("Работа завершена.")
print("Окно закроется через 2 секунды.")
time.sleep(2)
