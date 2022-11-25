import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from webdrivermanager.chrome import ChromeDriverManager



def get_data():
    return[
        ('anis','aouadi'),
        ('anis1', 'aouadi1'),
        ('anis2', 'aouadi2'),
        ('anis3', 'aouadi3'),
        ('Admin', 'admin123')

    ]
def setup_function():
    global driver
    # service_obj = Service("C:\\Users\\anisa\\OneDrive\\Bureau\\drivers\\chromedriver.exe")
    # driver = webdriver.Chrome(service=service_obj)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

def teardown_function():
    time.sleep(3)
    driver.quit()

@pytest.mark.parametrize('username, password',get_data())
def test_login(username,password):
    #print(username, '-------' , password,'------')

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
