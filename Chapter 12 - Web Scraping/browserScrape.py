from selenium import webdriver
browser = webdriver.Chrome(
    executable_path=r"C:\Users\NeilM\Downloads\chromedriver.exe")

browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name(' cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
