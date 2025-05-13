from selenium.webdriver.common.by import By
from components import BaseComponent



def test_footer_text(driver):
    driver.get("https://demoqa.com/")
    footer_locator = (By.CSS_SELECTOR, "footer span")
    footer = BaseComponent(driver, footer_locator)
    assert footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."


def test_elements_page_center_text(driver):
    driver.get("https://demoqa.com/")


    elements_card = driver.find_element(By.CSS_SELECTOR, ".card-body h5")
    if elements_card.text.strip().lower() == "elements":
        elements_card.click()
    else:
        raise Exception("Не найдена карточка Elements")


    center_text_locator = (By.CSS_SELECTOR, ".col-12.mt-4.col-md-6")
    center_text = BaseComponent(driver, center_text_locator)
    assert center_text.get_text() == "Please select an item from left to start practice."
