import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920x1080')
    download_path = '/tmp'

    prefs = {
        'download.prompt_for_download': False,
        'profile.default_content_settings.popups': 0,
        'download.directory_upgrade': True
    }

    options.add_experimental_option('prefs', prefs)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bin_path = os.path.join(base_dir, 'bin')
    chromedriver_path = os.path.join(bin_path, 'chromedriver')
    options.binary_location = os.path.join(bin_path, 'headless-chromium')
    driver = webdriver.Chrome(chromedriver_path, options=options)
    
    driver.command_executor._commands["send_command"] = (
        'POST',
        '/session/$sessionId/chromium/send_command'
    )

    driver.execute(
        "send_command",
        params={
            'cmd': 'Page.setDownloadBehavior',
            'params': { 'behavior': 'allow', 'downloadPath': download_path }
        }
    )
    
    return driver
