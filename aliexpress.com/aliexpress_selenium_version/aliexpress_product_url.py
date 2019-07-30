import time
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from spiders.settings import *


def open_first_munu_page(browser, urls):
    """
    打开首页的起始分类按钮页面
    :param browser:
    :param url:
    :return:
    """
    for url in urls:
        browser.switch_to.window(browser.window_handles[0])
        browser.get(url)
        while True:
            fp = open("page.json", "w")
            for product_detail_url in get_first_munu_info(browser):
                product_detail = get_product_detail(browser, product_detail_url)
                json.dump(product_detail, fp)
                json.dump("/n", fp)


def get_first_munu_info(browser):
    """
    传入初始URL，爬取页面内容,获取产品详情的URL
    :param page_num:
    :param browser:
    :param url:
    :return:
    """
    for i in range(0, 7):
        browser.execute_script("window.scrollBy(0, 700)")
        time.sleep(0.5)
    items = browser.find_elements_by_xpath("//div[@class='place-container']/a")
    for item in items:
        browser.switch_to.window(browser.window_handles[0])
        page_product_url = item.get_attribute('href')
        yield page_product_url
    open_next_page(browser)


def open_next_page(browser):
    """
    爬取当前页面成功之后，向下再次滑动点击下一页的按钮
    :param browser:
    :return:
    """
    browser.execute_script("window.scrollBy(0, 250)")
    element = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='next-btn next-medium "
                                              "next-btn-normal next-pagination-item "
                                              "next-next']")))
    browser.execute_script("arguments[0].click();", element)


def get_product_detail(browser, url):
    """
    去产品详情页爬需要的数据
    :param browser:
    :param url:
    :return:
    """
    browser.execute_script("window.open()")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(url)
    browser.execute_script("window.scrollBy(0, 500)")
    time.sleep(1)
    try:
        store_name = browser.find_element_by_xpath('//*[@id="store-info-wrap"]/div[1]/h3/a').text
    except NoSuchElementException:
        store_name = None
    try:
        Positive_feedback = browser.find_element_by_xpath('//*[@id="store-info-wrap"]/div[1]/div/span/i').text
    except NoSuchElementException:
        Positive_feedback = None
    follows = browser.find_element_by_xpath('//*[@id="store-info-wrap"]/div[2]/p/i').text
    product_name = browser.find_element_by_xpath('//div[@class="product-title"]').text
    product_image_url = browser.find_element_by_xpath("//div[@class='img-view-wrap']//li/div/img").get_attribute("src")
    product_value = browser.find_element_by_xpath("//span[@class='product-price-value']").text
    try:
        product_score = browser.find_element_by_xpath("//span[@class='overview-rating-average']").text
    except NoSuchElementException:
        product_score = None
    try:
        pieces_available = browser.find_element_by_xpath("//div[@class='product-quantity-tip']/span").text
    except NoSuchElementException:
        pieces_available = None
    try:
        product_reviews = browser.find_element_by_xpath("//span[@class='product-reviewer-reviews black-link']").text
    except NoSuchElementException:
        product_reviews = None
    try:
        product_orders = browser.find_element_by_xpath("//span[@class='product-reviewer-sold']").text
    except NoSuchElementException:
        product_orders = None
    try:
        add_wishlist_num = browser.find_element_by_xpath("//span[@class='add-wishlist-num']").text
    except NoSuchElementException:
        add_wishlist_num = None

    product_detail_data = {
        "store_name ": store_name,
        "Positive_feedback": Positive_feedback,
        "follows": follows,
        "product_name": product_name,
        "product_image_url": product_image_url,
        "product_value": product_value,
        "product_score": product_score,
        "pieces_available": pieces_available,
        "product_reviews ": product_reviews,
        "product_orders": product_orders,
        "add_wishlist_num": add_wishlist_num
    }
    browser.close()
    print(product_detail_data)
    return product_detail_data


def main():
    myBrowser = webdriver.Chrome()
    myBrowser.maximize_window()
    open_first_munu_page(myBrowser, first_munu_urls)


if __name__ == '__main__':
    main()
