"""
NoSuchElementException - элемент не найден по заданному локатору
TimeoutException - Ожидание завершилось, но элемент так и не нашли
ElementNotInteractableException - Элемент был найден, но с ним нельзя взаимодействовать
StaleElementReferenceException - Элемент устарел, DOM дерево обновлено и нижно выполнить поиск элемента еще раз
ElementClickInterceptedException - Невозможно нажать на элемент по какой-то причине (например, перекрыт другим элементом)
InvalidSelectorException - неверный локатор XPATH, CSS и т.д
WebDriverException - ошибка драйвера
SessionNotCreatedException - Сессия с браузером не была создана
NoSuchWindowException - Попытка обратиться к окну браузера, которое уже было закрыто
NoSuchFrameException - Попытка обратиться к фрейму которого не существует
UnexpectedAlertPresentException - Ловится в случае если какой-то алерт мешает выполнению нашего действия
NoAlertPresentException - Если хотим взаимодействовать с алертом но его не существует
MoveTargetOutOfBoundsException - Попытка вывести курсор за пределы за пределы окна браузера 
"""