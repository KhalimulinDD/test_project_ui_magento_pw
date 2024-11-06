import pytest
import allure
from pages.sale_page import SalePage
from pages.create_account_page import CreateAccount
from pages.collections_eco_friendly_page import CollectionsEcoFriendly


@pytest.fixture()
def create_account_page(page, context):
    account_page = CreateAccount(page, context)
    yield account_page
    # Снимаем скриншот перед закрытием страницы
    allure.attach(
        page.screenshot(full_page=True),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    page.close()


@pytest.fixture()
def collections_eco_friendly_page(page, context):
    eco_friendly_page = CollectionsEcoFriendly(page, context)
    yield eco_friendly_page
    # Снимаем скриншот перед закрытием страницы
    allure.attach(
        page.screenshot(full_page=True),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    page.close()


@pytest.fixture()
def sale_page(page, context):
    sale = SalePage(page, context)
    yield sale
    # Снимаем скриншот перед закрытием страницы
    allure.attach(
        page.screenshot(full_page=True),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    page.close()
