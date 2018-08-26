import time
import re
from selenium import webdriver

#create URL as domain extract patterns.
pat = r"https?://(www.)?([\w-]+).[\w.]"

#write site urls down list.txt.
f = open('list.txt')
#read line from list.txt, and remove space.
URLS = list(map(str.strip,(f.read().split("\n"))))

#start browser.
driver = webdriver.Chrome()

#execute urls from "URLS".
for url in URLS:
    #set file name as a part of domain.
    site_name = re.search(pat, url)
    file_name = "{0}.png".format(site_name.group(2))
    #open urls.
    driver.get(url)
    #set windows size and zoom.
    driver.set_window_size(1250, 1036)
    driver.execute_script("document.body.style.zoom='90%'")

    time.sleep(2)

    driver.save_screenshot("./images/" + file_name)

driver.quit()
