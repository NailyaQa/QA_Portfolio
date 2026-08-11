
from selenium.webdriver.common.by import By


class MainPageLocators:

   

    # Кнопка «Личный кабинет»
    ACCOUNT_BUTTON = (
        By.CSS_SELECTOR,
        "a[href='/account']"
    )

    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (
        By.CSS_SELECTOR,
        "a[href='/']"
    )

    # Кнопка «Лента заказов»
    ORDER_FEED_BUTTON = (
        By.CSS_SELECTOR,
        "a[href='/feed']"
    )


    

    # Ингредиент: булка
    BUN_INGREDIENT = (
        By.XPATH,
        "//a[.//p[normalize-space()='Краторная булка N-200i']]"
    )

    # Ингредиент: соус «Традиционный галактический»
    SAUCE_INGREDIENT = (
        By.XPATH,
        "//a[.//p[normalize-space()='Соус традиционный галактический']]"
    )

    # Ингредиент: филе Люминесцентного тетраодонтимформа
    FILLING_INGREDIENT = (
        By.XPATH,
        "//a[.//p[normalize-space()='Филе Люминесцентного тетраодонтимформа']]"
    )


   

    # Заголовок окна с деталями ингредиента
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//h2[normalize-space()='Детали ингредиента']"
    )

    # Кнопка закрытия модального окна
    CLOSE_MODAL_BUTTON = (
    By.XPATH,
    "//div[contains(@class, 'Modal_modal__contentBox')]/preceding-sibling::button"
)
    INGREDIENT_MODAL_CLOSE_BUTTON = (
    By.XPATH,
    "//h2[normalize-space()='Детали ингредиента']"
    "/ancestor::section[1]"
    "//button"
)

    

    # Счётчик выбранного ингредиента
    INGREDIENT_COUNTER = (
    By.XPATH,
    "//a[.//p[normalize-space()='Филе Люминесцентного тетраодонтимформа']]"
    "//div[contains(@class, 'counter')]"
)


    

    # Кнопка «Оформить заказ»
    ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Оформить заказ']"
    )

    # Область выбранных ингредиентов
    SELECTED_INGREDIENTS = (
        By.CSS_SELECTOR,
        "ul[class*='BurgerConstructor_basket__list']"
    )

    # Заголовок «Соберите бургер»
    CONSTRUCTOR_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='Соберите бургер']"
    )


   

    # Номер заказа
    ORDER_NUMBER = (
        By.XPATH,
        "//p[normalize-space()='идентификатор заказа']"
        "/preceding-sibling::h2"
    )

    # Модальное окно заказа
    ORDER_MODAL = (
        By.XPATH,
        "//h2[following-sibling::p[normalize-space()='идентификатор заказа']]"
        "/ancestor::div[contains(@class, 'Modal_modal__contentBox')]"
    )

    # Кнопка закрытия окна с номером заказа
    ORDER_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//h2[following-sibling::p[normalize-space()='идентификатор заказа']]"
        "/ancestor::div[contains(@class, 'Modal_modal__contentBox')]"
        "/preceding-sibling::button"
    )

    # Затемнение за модальным окном
    MODAL_OVERLAY = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal_overlay')]"
    )

    INGREDIENT_MODAL = (
    By.CSS_SELECTOR,
    "div.Modal_modal__contentBox__sCy8X"
)
    INGREDIENT_MODAL = (
    By.XPATH,
    "//h2[normalize-space()='Детали ингредиента']"
    "/ancestor::div[contains(@class, 'Modal_modal__contentBox')]"
)

    
    CLOSE_INGREDIENT_MODAL_BUTTON = (
    By.XPATH,
    "//div[contains(@class, 'Modal_modal__contentBox')]"
    "/following-sibling::button"
)



