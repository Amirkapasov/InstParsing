from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

service = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

name = input("nickname inst: ")

driver.get("https://instashadow.com/ru/followed")

search_input = wait.until(EC.presence_of_element_located((By.ID, "search-input")))
search_input.send_keys(f"https://www.instagram.com/{name}/")

wait.until(EC.element_to_be_clickable((By.ID, "download-btn"))).click()

# Кликаем following
wait.until(EC.element_to_be_clickable((By.ID, "following"))).click()

follow_list = wait.until(
    EC.presence_of_element_located((By.ID, "follow-list"))
)

# Скролл
for _ in range(5):
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight",
        follow_list
    )
    time.sleep(2)

items = follow_list.find_elements(By.CLASS_NAME, "follow-item")

usernames = []

for item in items:
    try:
        username = item.find_element(By.CLASS_NAME, "follow-username").text.strip()
        if username:
            usernames.append(username)
    except:
        pass

print("Найдено подписок:", len(usernames))
day = input("День просмотра:")


# Сохраняем
with open(f"following{day}.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["username"])
    for u in usernames:
        writer.writerow([u])

print("Файл following.csv сохранён")

driver.quit()
