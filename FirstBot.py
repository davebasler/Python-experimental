from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
driver.get("https://imdb.com")
#sleep(2)
#driver.find_element_by_xpath("//*[@placeholder='Search IMDb']")\
 #   .send_keys("Jurassic Park")
#sleep(1)
#driver.find_element_by_xpath("//*[@id='suggestion-search-button']").click()
sleep(1)
driver.find_element_by_xpath("//*[@id='imdbHeader-navDrawerOpen--desktop']")\
    .click()
sleep(1)
driver.find_element_by_xpath("//*[@class='ipc-list__item mdc-list-item nav-link sc-jTzLTM fjLstn ipc-list__item--indent-one']")\
    .click()
sleep(2)

topfilms=[]

topList = driver.find_element_by_xpath("//*[@class='lister-list']")
films = topList.find_elements_by_tag_name('a')
years = topList.find_elements_by_xpath("//*[@class='secondaryInfo']")
for film in films:
    title = film.text
    print(title)
    topfilms.append(title)

for year in years:
    temp = year.text
    print(temp)

#print(topfilms)

driver.find_element_by_xpath("//*[@class='lister-sort-by']").click()
driver.find_element_by_xpath("//*[@value='us:descending']").click()
driver.close()