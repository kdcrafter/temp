from selenium.webdriver.chrome.options import Options

def pytest_setup_options():
    options = Options()
    options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return options