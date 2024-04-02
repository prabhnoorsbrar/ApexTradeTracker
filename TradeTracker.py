from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DataInjector import inject_data
import datetime


def trade_tracker(PATH):
    service = Service(PATH)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)

    driver.get("https://apextraderfunding.com/member/member/")
    driver.maximize_window()

    user_name = driver.find_element(By.ID, "amember-login")
    user_name.send_keys("APEX Trading USERNAME")

    password = driver.find_element(By.ID, "amember-pass")
    password.send_keys("APEX TRADING PASSWORD HERE")

    login_button = driver.find_element(By.XPATH, "//input[@class='btn btn-primary dz-xs-flex m-r5']")
    login_button.click()

    account_summary = driver.find_element(By.ID, "menu-AccountSummary")
    account_summary.click()
    
    
    # 3rd ACCOUNT
    #####################################################################
    # POSSIBLE BALANCE: XPATH = /html/body/div[1]/div[4]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[7]
    act_balance_03 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//tr[@class='even am-grid-row']/td[7]"))).text
    # Wait for act_threshold to become visible
    act_threshold_03 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//tr[@class='even am-grid-row']/td[6]"))).text

    # Convert extracted text to float
    threshold_03 = float(act_threshold_03.replace('$', '').replace(',', ''))
    balance_03 = float(act_balance_03.replace('$', '').replace(',', ''))

    # 4th ACCOUNT
    #####################################################################
    # POSSIBLE BALANCE: XPATH = /html/body/div[1]/div[4]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[7]
    act_balance_04 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//tr[@class='odd am-grid-row']/td[7]"))).text
    # Wait for act_threshold to become visible
    act_threshold_04 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//tr[@class='odd am-grid-row']/td[6]"))).text

    threshold_04 = float(act_threshold_04.replace('$', '').replace(',', ''))
    balance_04 = float(act_balance_04.replace('$', '').replace(',', ''))    
    
    #####################################################################
    #print(threshold_03, balance_03, threshold_04, balance_04)
    inject_data(threshold_03, balance_03, threshold_04, balance_04)


def main():
    PATH = "c:\\Program Files (x86)\\chromedriver.exe"  # Note the double backslashes
    trade_tracker(PATH)
    file = open(r'YOUR PATH TO A TXT FILE WITHIN THE PROJECT FOLDER HERE< IDEAL FOR SCHEDULING VIA WINDOWS TASK SCHEDULER', 'a')
    file.write(f'{datetime.datetime.now()} - The script ran \n')


if __name__ == "__main__":
    main()
