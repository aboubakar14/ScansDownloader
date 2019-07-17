#! /usr/bin/python3

import argparse
import importlib
import os
from selenium import webdriver
from selenium import common as selenium_common


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
    chrome_driver = os.getenv('CHROME_DRIVER')
    firefox_driver = os.getenv('FIREFOX_DRIVER')
    executable_path = chrome_driver or firefox_driver

    if executable_path:
        try:
            if firefox_driver:
                browser = webdriver.Firefox(executable_path=executable_path)
            if chrome_driver:
                browser = webdriver.Chrome(executable_path=executable_path)
            # all modules must be in 'modules' folder
            module = importlib.import_module("modules." + module)
            downloader = module.factory(browser, link, target, dest)
            downloader.download()
        except selenium_common.exceptions.InvalidArgumentException:
            print("The given url is not accessible.")
        except selenium_common.exceptions.WebDriverException:
            print("Browser driver is not correct.")
    else:
        print("Browser driver can not be None." +
              "Please define CHROME_DRIVER or FIREFOX_DRIVER")
