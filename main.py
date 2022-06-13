import selenium
import info
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
username = ""
suffix = ""
gcredentials = []


def generateLogin():
    global username
    global suffix
    global gcredentials

    random.seed(time.time())
    letters = string.ascii_letters
    temp = random.randint(123456, 999999)
    suffix = str(temp)
    username = info.ACCOUNT_NAME + suffix
    temp = random.choices(letters, k=16)
    stringPassword = ""
    gcredentials = [username, stringPassword.join(temp)]
    return gcredentials


def connectBattlenet():
    driver.get("https://www.twitch.tv/settings/connections")
    connectButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/button"))).click()


def registerAccount(credentials):
    driver.get("https:/www.twitch.tv/login")

    # Username Field:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div/ul/li[2]/button/div/div[1]/p"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[1]/div/div[2]/input"))).send_keys(credentials[0])

    # Password Fields:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[2]/div[1]/div[2]/div[1]/input"))).send_keys(credentials[1])
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[2]/div[2]/div/div[2]/div[1]/input"))).send_keys(credentials[1])

    # Birthday Fields:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/div/div[2]/div[1]/select"))).send_keys("A", Keys.ENTER, Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/div/div[2]/div[2]/div/input"))).send_keys("19")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/div/div[2]/div[3]/div/input"))).send_keys("2002")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[4]/div/div[2]/button/div/div[2]"))).click()

    # Email:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[4]/div/div[1]/div[2]/input"))).send_keys(info.EMAIL + "+" + str(suffix) + info.DOMAIN)

    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[5]/button/div/div"))).click()
    print("==================================================================================================")
    input("Press ENTER to continue after the captcha is solved..\n"
          "==================================================================================================")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[3]/div[2]/button/div/div"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div[3]/div[2]/button/div/div"))).click()
    time.sleep(2)
    driver.get("https://twitch.tv/")

    # Log out:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/nav/div/div[3]/div[6]/div/div/div/div/button"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/div[5]/button"))).click()

    print("Account created!\n\tUsername: " + gcredentials[0] + " Password: " + gcredentials[1])
    accounts = open("accounts.txt", 'a')
    accounts.write("Email: " + info.EMAIL + "+" + suffix + info.DOMAIN + " | " + " Username: " + gcredentials[0] + " | Password: " + gcredentials[1] + "\n")
    accounts.close()


if __name__ == '__main__':
    numAccounts = 0
    try:
        numAccounts = int(input("Number of accounts to create: "))
        for x in range(numAccounts + 1):
            registerAccount(generateLogin())
    except ValueError:
        print("Please enter an integer.")
        quit()
