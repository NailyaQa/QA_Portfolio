import pytest

from selenium import webdriver
from helpers.data_generator import generate_user_data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from constants import BASE_URL





@pytest.fixture(
    params=["chrome", "firefox"]
)
def driver(request):

    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def authorized_user(driver):

    user_data = generate_user_data()

    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    # 1. Переход в личный кабинет
    main_page.click_account()

    # 2. Переход на страницу регистрации
    login_page.click_register_link()

    # 3. Регистрация
    login_page.register(
        user_data["name"],
        user_data["email"],
        user_data["password"]
    )

    # 4. Переход на страницу входа
    login_page.click_login_link()

    # 5. Авторизация теми же данными
    login_page.login(
        user_data["email"],
        user_data["password"]
    )


    return user_data
