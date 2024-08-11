from datetime import datetime
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        print("Launching Firefox browser.........")
    else:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print("Launching Chrome browser.........")

    yield driver
    driver.quit()  # Ensure the browser is closed after the test


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser", default="chrome", help="Browser to use for tests")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

def pytest_configure(config):
    print("pytest_configure hook called")
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'


# It is hook for delete/Moclsdify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"