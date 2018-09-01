"""
--------------------------------------------------------------------
Python webcrawling spider app for downloading input and output cases 
from competitive programming servers, saving more time 
--------------------------------------------------------------------
AUTHOR : Sayan Bhattacharjee (aerosayan)
EMAIL  : aero.sayan@gmail.com
LICENSE : DEFAULT 
DATE : 01-SEP-2018
--------------------------------------------------------------------
PREREQUISITES : 
    + Python 3.0+
    + BeautifulSoup library
    + selenium library and chrome webdriver
--------------------------------------------------------------------
"""

# help info defined again to allow printing to screen
info = """
--------------------------------------------------------------------
Python webcrawling spider app for downloading input and output cases 
from competitive programming servers, saving more time 
--------------------------------------------------------------------
AUTHOR : Sayan Bhattacharjee (aerosayan)
EMAIL  : aero.sayan@gmail.com
LICENSE : DEFAULT 
DATE : 01-SEP-2018
--------------------------------------------------------------------
PREREQUISITES : 
    + Python 3.0+
    + BeautifulSoup library
    + selenium library and chrome webdriver
--------------------------------------------------------------------
"""

# The standard library modules
import os
import sys

# The BeautifulSoup module
from bs4 import BeautifulSoup

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def hr():
    print("--------------------------------------------------------------------")

def scrape_google_codejam(dashboard_url,delay=8):
    """ Scrape google codejam dashboard for input and output test cases """
    #--------------------------------------------------------------------------
    # start selenium chrome webdriver
    # NOTE : chrome webdriver was required to be downloaded and installed first
    driver = webdriver.Chrome()
    driver.get(dashboard_url)
    wait_for_class ="problem-io-wrapper"
    print("INF :: SPIDER WAITING FOR LOADING CLASS : " + wait_for_class)
    hr()
    #--------------------------------------------------------------------------
    # wait for page to load , if unsuccessfull then exit
    try:
        elem = WebDriverWait(driver, int(delay)).until(EC.presence_of_element_located((By.CLASS_NAME, wait_for_class)))
        print("INF :: WEBPAGE IS READY TO BE SCRAPED!")
        # page source
        src = driver.page_source
        hr()
    except TimeoutException:
        print("ERR :: LOADING TOOK TOO MUCH TIME!...")
        print("ERR :: EXITING...")
        hr()
        exit()
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    # parse selenium page source using beautiful soup
    soup = BeautifulSoup(src,"html.parser")
    # find all the input and output cases descrived in pre tags by Google
    io_tags = soup.findAll("pre")
    # to store string form of the input and output cases 
    io = []
    # file counter
    count = 0;
    # problem number
    prob  = 1;
    # input file prefix
    ip_prefix = "in-"
    # input file postfix
    ip_postfix = ".in"

    # output file prefix
    op_prefix = "out-"
    # output file postfix
    op_postfix = ".out"
    

    print("INF :: WRITING TO FILES...")
    #--------------------------------------------------------------------------
    # write to file
    for i in io_tags :
        count += 1
        io.append(i.string)
        #write input file
        if(count == 1):
            # open and write to input file
            file = open(ip_prefix + str(prob) + ip_postfix,"w")
            file.write("%s" % i.string)
            file.close()
        if(count == 2):
            # open and write to output file
            file = open(op_prefix + str(prob) + op_postfix,"w")
            file.write("%s" % i.string)
            file.close()
            # reset  count to zero 
            count = 0
            # increment problem number by one
            prob += 1
    #--------------------------------------------------------------------------
    print("INF :: SUCCESSFULLY CREATED ALL INPUT AND OUTPUT FILES...")
    hr()
    #print the test case inputs and outputs if debugging
    #print(io)
#------------------------------------------------------------------------------

# driver function
if __name__ == "__main__":
    #--------------------------------------------------------------------------
    #print banner
    print(info)
    hr()
    print("          ONLY GOOGLE CODEJAM IS SUPPORTED FOR NOW")
    hr()
    #--------------------------------------------------------------------------
    # get problem dashboard url
    # example : https://codejam.withgoogle.com/codejam/contest/5304486/dashboard
    url   = input("IO :: PLEASE ENTER PROBLEM DASHBOARD URL         : ")
    delay = input("IO :: PLEASE ENTER DELAY TIME (SECS) TO LOAD URL : ")
    # call google codejam scraper
    scrape_google_codejam(url,delay)
    print("INF :: EXITING...")
    hr()
    exit()

