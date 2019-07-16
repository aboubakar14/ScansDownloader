================
ScansDownloader
================

This project goal is to download easily scans of manga from web sites.
For instance, it will download each scan from a given url and put them correctly in the right folder.

# Requirements

You will need python3, pipenv as well as a browser driver to use ScansDownloader

# ScanDownloader

ScanDownloader is a command line project.
It uses Selenium for browsing on the web, and thats why you will need drivers
It works with modules, each module correspond to the way of downloading scans from a specific web site.

## Modules
Currently there is only one module avalaible:
   - fanfox (http://fanfox.net)

## Drivers

Drivers are used to navigate through the web site.
In the project, there is a default browser driver which is for Chrome v75
If you are using another version or another browser, you will need to download its driver.

You can add drivers in the drivers folder and uses the -dn option to indicate which driver you want to use  (cf: Driver Usage).

### Links

Chrome drivers: https://sites.google.com/a/chromium.org/chromedriver/downloads
Firefox drivers: https://github.com/mozilla/geckodriver/releases

# Installation

1) Make sur you have python3.
2) Download pipenv if you dont have it (https://docs.pipenv.org/en/latest/install/#installing-pipenv)
3) Go in the ScansDownloader directory and run the command: `pipenv install`
4) Now you have your virtual env, you can either do:
   - `pipenv shell` to activate the virtual env
   - `pipenv run ${COMMAND}` to run command inside the vitual env
5) You are now ready to use ScansDownloader

# Usage

All the following commands are done after a `pipenv shell` or while using `pipenv run ${COMMAND}`.

## Basic usage

- `python3 scansdownloader.py -h` print the help

- `python3 scansdownloader.py MODULE START` will download scans from the web site associated to the module
  and will begin the downloading from START until there is nothing more to download

## Options usage

Well just launch `python3 scansdownloader.py -h` and read :)

## Drivers

There are several ways to define which driver to use:
- The default (if nothing is specified) will take the Chrome driver that is in the drivers folder
- The command line option (-dn, --driver_name, DRIVER_NAME) search the given driver in the drivers folder
  so you will have to put your driver in this folder.
- You can also define the driver by setting the environment variable named `BROWSER_PATH .
  This way, it will take the driver located in the environment variable.
  ex 1: `BROWSER_PATH=/tmp/tests/firefoxV42 python3 scans_downloader.py MODULE START`
  ex 2: do `export BROWSER_PATH=/tmp/tests/firefoxV42` then `python3 scans_downloader.py MODULE START`

## Modules usage

### fanfox
`python3 scans_downloader.py fanfox http://fanfox.net/manga/one_piece/vTBD/c947/1.html`

# For developpers

If you are contributing, thanks !

## Modules

If you want to develop your own module, please follow the several rules:
- Make your module inherit from the base class (you will have to write the download() method)
- Make sure your class handles the TARGET and the DESTINATION options, in the same way as fanfox
- Define the factory() method (outside the class), it is useful for the main for instantiating your module dynamically.

Basically if you create your own module, you just have to create your_module.py in the modules folder.
Then if you want to test, it will be `̀python3 scans_downloader.py your_module START

Please look at the fanfox module if you want an example.

## Other stuff

Feel free to add others features, improve the code etc ...

# Tests

Yeah sure bro, fully tested and CI is perfect.
