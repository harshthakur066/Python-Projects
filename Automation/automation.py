from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

show_button_text = chrome_browser.find_element_by_class_name('btn-default')
print(show_button_text.get_attribute('innerHTML'))

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Typing throug code')
show_button_text.click()

output_msg = chrome_browser.find_element_by_id('display')
assert 'Typing throug code' in output_msg.text

chrome_browser.close()
