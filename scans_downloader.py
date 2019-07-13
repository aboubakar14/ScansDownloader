import fanfox
from selenium import webdriver

if __name__ == "__main__":
    browser = webdriver.Chrome(executable_path=r"/home/aboubakar/Bureau/Projects/ScansDownloader/chromedriver")
    fanfox = fanfox.Fanfox(browser, "http://fanfox.net/manga/one_piece/vTBD/c947/1.html")

    fanfox.download()
