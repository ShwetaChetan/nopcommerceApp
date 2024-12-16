
from selenium import webdriver
import pytest

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome import service
from webdriver_manager.opera import OperaDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("--browser").lower()
    if browser == "chrome":
       driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
       print("launching chrome")
    elif browser == "Edge":
       driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
       print("launching edge")
    elif browser == "Opera":
         webdriver_service = service.Service(OperaDriverManager().install())
         webdriver_service.start()

         options = webdriver.ChromeOptions()
         options.add_experimental_option('w3c', True)

         driver = webdriver.Remote(webdriver_service.service_url, options=options)

         print("launching opera")
    elif browser == "Firefox":
         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
         print("launching Firefox")

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(60)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config._metadata = {
        'Project Name': 'nop Commerce',
        'Module Name': 'Customers',
        'Tester': 'Shweta'
    }

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        '<p><strong>Project Name:</strong> nop Commerce</p>',
        '<p><strong>Module Name:</strong> Customers</p>',
        '<p><strong>Tester:</strong> Shweta</p>'
    ])



#     return driver
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# def pytest_configure(config):
#     config._metadata['Project name'] = 'nop Commerce'
#     config._metadata['Module name'] = 'Customers'
#     config._metadata['Tester'] = 'Shweta'
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

# from selenium import webdriver
# import pytest
#
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
#
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# from selenium.webdriver.chrome import service
# from webdriver_manager.opera import OperaDriverManager
#
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# # Fixture to set up the browser
# @pytest.fixture()
# def setup(request):
#     browser = request.config.getoption("--browser")
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#         print("Launching Chrome")
#     elif browser == "edge":
#         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#         print("Launching Edge")
#     elif browser == "opera":
#         webdriver_service = service.Service(OperaDriverManager().install())
#         webdriver_service.start()
#
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option('w3c', True)
#
#         driver = webdriver.Remote(webdriver_service.service_url, options=options)
#         print("Launching Opera")
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#         print("Launching Firefox")
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#
#     yield driver
#     driver.quit()
#
#
# # Add a command-line option for selecting the browser
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests")
#
#
# # Set custom metadata for the report
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config._metadata = {
#         'Project Name': 'nop Commerce',
#         'Module Name': 'Customers',
#         'Tester': 'Shweta'
#     }
#
#
# # Customize the HTML report
# @pytest.hookimpl(tryfirst=True)
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([
#         '<p><strong>Project Name:</strong> nop Commerce</p>',
#         '<p><strong>Module Name:</strong> Customers</p>',
#         '<p><strong>Tester:</strong> Shweta</p>'
#     ])
