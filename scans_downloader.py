#! /usr/bin/python3

import argparse
import importlib
import os
from selenium import webdriver


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
    parser.add_argument("-dn", "--driver_name", required=False,
                        help="Browser driver name. If not set it will be " +
                        "'chromedriver' which is in the drivers folder.")

    return parser


if __name__ == "__main__":
    parser = parser()
    args = parser.parse_args()
    module = args.module
    link = args.start
    target = args.target
    dest = args.dest
    driver_name = args.driver_name or 'chromedriver'
    # 1) env var, 2) opt param, 3) default value
    executable_path = os.getenv('BROWSER_PATH',
                                os.path.join(
                                    os.path.dirname(os.path.abspath(__file__)),
                                    "drivers", driver_name))
    print(executable_path)
    browser = webdriver.Chrome(executable_path=executable_path)
    # all modules must be in 'modules' folder
    module = importlib.import_module("modules." + module)
    downloader = module.factory(browser, link, target, dest)
    downloader.download()
