#! /usr/bin/python3

import argparse
import importlib
import os
from selenium import webdriver
from selenium import common as selenium_common
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("module", help="Module to use")
    parser.add_argument("start", help="Url to start downloading")
    parser.add_argument("-t", "--target", required=False,
                        help="Url to stop downloading (url not included). " +
                        "If not defined, it will stop when it can not download anymore.")
    parser.add_argument("-d", "--dest", required=False,
                        help="Destination folder. If not set it will " +
                        "store downloads in the current directory.")

    return parser


if __name__ == "__main__":
    parser = parser()
    args = parser.parse_args()
    module = args.module
    link = args.start
    target = args.target
    dest = args.dest
    driver = os.getenv('DRIVER')

    if driver in ['firefox', 'chrome']:
        try:
            if driver == 'firefox':
                browser = webdriver.Firefox()
            else:
                browser = webdriver.Chrome()
            # all modules must be in 'modules' folder
            module = importlib.import_module("modules." + module)
            downloader = module.factory(browser, link, target, dest)
            downloader.download()
        except selenium_common.exceptions.InvalidArgumentException:
            print("The given url is not accessible.")
        except selenium_common.exceptions.WebDriverException as e:
            print(e)
    else:
        print("Browser driver should be 'chrome' or 'firefox' " +
              "Please define DRIVER correctly.")
