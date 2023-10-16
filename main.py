from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client
import os

url = 'https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6'

chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get(url)


def send_sms():
    account_sid = os.environ['AcSID']
    auth_token = os.environ['AuTOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        from_='+12563056710',
        body= f'Hi! The stock trend is {PERCENTAGE}%!',
        to= os.environ['RCV_NO']
    )
    print(message.status)


def getting_percentage():

    wait = WebDriverWait(chrome, 20)
    percentage = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]'))).text
    percentage = percentage.strip(' %')

    return percentage

getting_percentage()

PERCENTAGE = getting_percentage()

if float(PERCENTAGE) < -0.10:
    send_sms()

