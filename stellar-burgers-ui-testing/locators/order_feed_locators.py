from selenium.webdriver.common.by import By


class OrderFeedLocators:

    

    # Счётчик «Выполнено за всё время»
     
    TOTAL_ORDERS_COUNT = (
        By.XPATH,
        "(//p[contains(@class, 'OrderFeed_number')])[1]"
    )

    # Счётчик «Выполнено за сегодня»
    TODAY_ORDERS_COUNT = (
        By.XPATH,
        "(//p[contains(@class, 'OrderFeed_number')])[2]"
    )

    # Раздел «В работе»
    ORDERS_IN_PROGRESS = (
        By.XPATH,
        "//p[text()='В работе:']/following-sibling::ul[1]"
    )

    # Номера заказов в разделе «В работе»
    ORDER_NUMBERS_IN_PROGRESS = (
        By.XPATH,
        "//p[text()='В работе:']/following-sibling::ul[1]/li"
    )
   
    
