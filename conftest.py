import pytest
from pages.base_page import BasePage
from pages.sale_page import SalePage
from pages.create_account_page import CreateAccount
from pages.collections_eco_friendly_page import CollectionsEcoFriendly

base = BasePage


@pytest.fixture()
def create_account_page(page, context):
    # Создаем объект страницы
    account_page = CreateAccount(page, context)
    yield account_page
    # Получаем активную страницу и делаем скриншот
    base.take_screenshot_and_close(context)


@pytest.fixture()
def collections_eco_friendly_page(page, context):
    # Создаем объект страницы
    eco_friendly_page = CollectionsEcoFriendly(page, context)
    yield eco_friendly_page
    # Получаем активную страницу и делаем скриншот
    base.take_screenshot_and_close(context)


@pytest.fixture()
def sale_page(page, context):
    # Создаем объект страницы
    sale = SalePage(page, context)
    yield sale
    # Получаем активную страницу и делаем скриншот
    base.take_screenshot_and_close(context)
