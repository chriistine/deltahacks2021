from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def searchForNews(topic, driver):

    searchBtn = driver.find_element_by_class_name("top-menu-search__button")
    searchBtn.click()

    inputElement = driver.find_element_by_css_selector('input[name=search_text]')

    inputElement.send_keys(topic)
    inputElement.send_keys(Keys.ENTER)

    # return list of articles on the first page
    articleHeaders = []
    time.sleep(2)

    # gets the link

    articleHeaders = driver.find_elements_by_class_name("article-card__link")
    links = [articleHeader.get_attribute('href') for articleHeader in articleHeaders]
    for link in links:
        print(link)

    # gets the title

    articleTitles = []
    articleTitles = driver.find_elements_by_class_name("article-card__headline-clamp")

    title = [articleTitle.text for articleTitle in articleTitles]
    title = str(title).replace("[", "").replace("]", "")


    for article in articleHeaders:
        print(title)


# def selectNews()


def main():
    driver = webdriver.Chrome(r'C:\Users\Andy\deltahacks2021-main\chromedriver.exe')

    driver.get('https://nationalpost.com/')
    searchForNews("education", driver)


if __name__ == "__main__":
    main()
