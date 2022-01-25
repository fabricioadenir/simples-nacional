from RPA.Browser.Selenium import Selenium
from app import config


def abrir_navegador(url) -> Selenium:

    browser = Selenium()
    if config.DOCKER_EXECUTION:
        browser.open_browser(url, browser=config.TYPE_BROWSER,
                             remote_url=config.CONTAINER_SELENIUM)
    else:
        browser.open_browser(url, browser=config.TYPE_BROWSER,
                             executable_path=config.EXECUTABLE_PATH)
    browser.set_selenium_timeout(f"{config.TIMEOUT} seconds")
    browser.set_window_size(1920, 1080)
    browser.maximize_browser_window()

    return browser
