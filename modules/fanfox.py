import os
import subprocess


class Fanfox():
    """ Fanfox scan downloader. """

    def __init__(self, browser, starting_url, target_url=None, dest=None):
        self.browser = browser
        # the path to save the downloaded scan
        self.current_path = starting_url
        self.current_url = browser.current_url
        self.previous_url = None
        # the target url is set, the downloader
        # will download from starting_url url to target url
        self.target = target_url
        # destination folder
        self.dest = dest

    def create_folder(self, link):
        """ This method creates a folder (if not exist) with the given Fanfox url.
        All fanfox url are like this 'fanfox.net/manga/.../1.html'
        So we keep everything between 'manga' and '1.html'
        to create the correct path.

        If the link is: 'fanfox.net/manga/manga_name/chapter_num/1.html'
       `path` with be `manga_name/chapter_num`

        If the link is: 'fanfox.net/manga/manga_name/volume/chapter_num/1.html'
       `path` with be `manga_name/volume/chapter_num`

        """
        self.current_path = os.path.join(*(link.split("manga")[1].split('/')[1:-1]))
        if self.dest:
            self.current_path = os.path.join(self.dest, self.current_path)
        if not os.path.exists(self.current_path):
            os.makedirs(self.current_path)
        return self.current_path

    def download(self):
        """ Download scans from the given url. """
        self.browser.get(self.current_path)

        # Create root folder if necessary
        self.current_path = self.create_folder(self.current_path)

        # If self.current_url == self.previous_url -> its the last page
        # If self.current_url == target -> target url reached so we stop
        while self.current_url != self.previous_url and self.current_url != self.target:
            active_page = self.browser.find_elements_by_xpath('.//a[@class="active"]')
            # get the image
            image = self.browser.find_element_by_class_name("reader-main-img")
            new_image_name = active_page[0].get_attribute("innerHTML") + ".jpg"
            downloaded = os.path.join(self.current_path, new_image_name)
            # download the image
            subprocess.run(["curl",
                            "--silent",
                            image.get_attribute("src"),
                            "-o",
                            downloaded])

            print("Downloaded: " + downloaded)
            self.previous_url = self.browser.current_url
            # click on the image to go to the next page
            image.click()
            self.current_url = self.browser.current_url
            self.current_path = self.create_folder(self.browser.current_url)


def factory(browser, starting_url, target_url=None, dest=None):
    return Fanfox(browser, starting_url, target_url, dest)
