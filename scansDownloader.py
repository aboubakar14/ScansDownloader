import subprocess
from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"/home/aboubakar/Bureau/Projects/scansDownloader/chromedriver")

link = 'http://fanfox.net/manga/one_piece/v01/c001/1.html'

browser.get(link)
pager_list_left = browser.find_element_by_class_name("pager-list-left")
active_page = browser.find_elements_by_xpath('.//a[@class="active"]')
print("++++++++++++++++ " + str(active_page[0].get_attribute("innerHTML")))
image = browser.find_element_by_class_name("reader-main-img")
new_image_name = active_page[0].get_attribute("innerHTML") + ".jpg"
subprocess.run(["curl", image.get_attribute("src"), "-o", new_image_name])
image.click()
