import pytest
from pages.sale_page import SalePage
from pages.create_account_page import CreateAccount
from pages.collections_eco_friendly_page import CollectionsEcoFriendly


@pytest.fixture()
def create_account_page(page, context):
    return CreateAccount(page, context)


@pytest.fixture()
def collections_eco_friendly_page(page, context):
    return CollectionsEcoFriendly(page, context)


@pytest.fixture()
def sale_page(page, context):
    return SalePage(page, context)
