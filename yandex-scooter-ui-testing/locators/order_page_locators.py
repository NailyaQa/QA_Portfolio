from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Заголовок формы
    ORDER_HEADER = (By.XPATH,"//div[text()='Для кого самокат']")

    # Поля формы
    NAME_FIELD = (By.XPATH,"//input[@placeholder='* Имя']")

    SURNAME_FIELD = (By.XPATH,"//input[@placeholder='* Фамилия']")

    ADDRESS_FIELD = (By.XPATH,"//input[@placeholder='* Адрес: куда привезти заказ']")

    METRO_FIELD = (By.XPATH,"//input[@placeholder='* Станция метро']")

    PHONE_FIELD = (By.XPATH,"//input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH,"//button[text()='Далее']")

    # Поле "Когда привезти самокат"
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    # День в календаре
    ACTIVE_DAY = (By.XPATH,"//div[contains(@class,'react-datepicker__day') and @aria-disabled='false']")

    # Выпадающий список "Срок аренды"
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-control")

    # Вариант "трое суток"
    THREE_DAYS_OPTION = (By.XPATH,"//div[contains(@class,'Dropdown-option') and text()='трое суток']")

    # Чекбокс "серая безысходность"
    GREY_CHECKBOX = (By.ID, "grey")

    # Поле комментария
    COMMENT_FIELD = (By.XPATH,"//input[@placeholder='Комментарий для курьера']")

    ORDER_BUTTON = (
    By.XPATH,
    "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']"
)

    # Модальное окно подтверждения заказа
    CONFIRM_ORDER_MODAL = (By.XPATH,"//div[contains(@class,'Order_Modal')]")

    # Кнопка "Да"
    CONFIRM_YES_BUTTON = (By.XPATH,"//button[text()='Да']")

    # Кнопка "Нет"
    CONFIRM_NO_BUTTON = (By.XPATH,"//button[text()='Нет']")

    # Окно успешного оформления заказа
    SUCCESS_MODAL = (By.XPATH,"//div[contains(@class,'Order_Modal')]")

    # Заголовок "Заказ оформлен"
    SUCCESS_MODAL_HEADER = (By.XPATH,"//div[contains(@class,'Order_ModalHeader')]")

    # Кнопка "Посмотреть статус"
    VIEW_STATUS_BUTTON = (By.XPATH,"//button[text()='Посмотреть статус']")

    @staticmethod
    def metro_station(station_name):
        return (By.XPATH,f"//*[text()='{station_name}']")
    
    METRO_FIELD = (By.CSS_SELECTOR, ".select-search__input")