from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import inspect
import time

#Packages Requirements for headless unix testing:
#sudo apt-get install libxss1 libappindicator1 libindicator7
#wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

#sudo dpkg -i google-chrome*.deb
#sudo apt-get install -f
#sudo apt-get install xvfb
#sudo apt-get install unzip

#wget -N http://chromedriver.storage.googleapis.com/2.20/chromedriver_linux64.zip
#unzip chromedriver_linux64.zip
#chmod +x chromedriver

#sudo mv -f chromedriver /usr/local/share/chromedriver
#sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
#sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

#Python library requirements
#pip install pyvirtualdisplay
#pip install selenium
#NOTE: If pip is not installed, run apt-get install python-pip OR:
#curl --silent --show-error --retry 5 https://raw.github.com/pypa/pip/master/contrib/get-pip.py | sudo python

def create_driver():
    try:
        #For headless Unix Testing, will not work on Windows as XVFB is not supported
        #global display
        #display.start()
        global driver
        driver = webdriver.Chrome()
    except Exception,e:
        print("Error produced when setting webdriver and/or XVFB display.")
        print(e)

def close_driver_and_display():
    try:
        driver.quit()
        display.stop()
    except Exception,e:
        print("Error produced when closing driver and display.")
        print(e)


def wp_login():
    try:
        create_driver() #creates the driver so we can use it
        driver.get(wordpress_url)
        driver.find_element_by_id("user_login").send_keys(username)
        driver.find_element_by_id("user_pass").send_keys(password)
        driver.find_element_by_id("wp-submit").click()
        print("Login completed successfully")
    except Exception,e:
        print("Exception produced when logging into wp-admin. Error is: ")
        print(e)


def wp_add_page():
    try:
        wp_login()
        driver.find_element_by_xpath("//*[@id='menu-pages']/a/div[3]").click()
        driver.find_element_by_xpath("//*[@id='menu-pages']/ul/li[3]/a").click()
        driver.find_element_by_id("insert-drs").click()
    except Exception,e:
        print("Exception produced when creating new page. Error is: ")
        print(e)


def test1():
    print("Clicking on gmail icon on google.com based on xpath")
    try:
        create_driver()
        driver.get("https://google.com")
        driver.find_element_by_xpath("//*[@id='gbw']/div/div/div[1]/div[1]/a").click()
        time.sleep(5)
        close_driver_and_display()
    except Exception,e:
        print inspect.stack()[0][3] + " Failed with the following message:"
        print(e)

def test2():
    print("Searching for keyword: NEU on google.com")
    try:
        create_driver()
        driver.get("https://google.com")
        driver.find_element_by_xpath("//*[@id='lst-ib']").send_keys("NEU")
        driver.find_element_by_xpath("//*[@id='lst-ib']").send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='rso']/div/div[1]/div/h3").click()
        time.sleep(5)
        close_driver_and_display()
    except Exception, e:
        print inspect.stack()[0][3] + " Failed with the following message:"
        print(e)

def test3():
    print("Intentionally causing an error to show error log for debugging.")
    try:
        create_driver()
        driver.get("https://google.com")
        driver.find_element_by_xpath("//*[@id='doesnotexist']").send_keys("NEU")
        close_driver_and_display()
    except Exception, e:
        print inspect.stack()[0][3] + " Failed with the following message:"
        print(e)


def testsuite_sprint1(): #all tests should go here
    test1()
    test2()
    test3()

testsuite_sprint1()
