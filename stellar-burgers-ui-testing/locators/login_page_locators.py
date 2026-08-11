from selenium.webdriver.common.by import By


class LoginPageLocators:



    # Поле Email при авторизации
    LOGIN_EMAIL_FIELD = (
        By.CSS_SELECTOR,
        "form input[type='text']"
    )

    # Поле пароля при авторизации
    LOGIN_PASSWORD_FIELD = (
        By.NAME,
        "Пароль"
    )

    # Кнопка «Войти»
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )

    # Ссылка «Зарегистрироваться»
    REGISTER_LINK = (
        By.LINK_TEXT,
        "Зарегистрироваться"
    )

    # Поле имени при регистрации
    NAME_FIELD = (
        By.XPATH,
        "//fieldset[.//label[text()='Имя']]//input"
    )

    # Поле Email при регистрации
    REGISTER_EMAIL_FIELD = (
        By.XPATH,
        "//fieldset[.//label[text()='Email']]//input"
    )

    # Поле пароля при регистрации
    REGISTER_PASSWORD_FIELD = (
        By.NAME,
        "Пароль"
    )

    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (
        By.XPATH,
        "//button[text()='Зарегистрироваться']"
    )

    # Ссылка «Войти»
    LOGIN_LINK = (
        By.LINK_TEXT,
        "Войти"
    )