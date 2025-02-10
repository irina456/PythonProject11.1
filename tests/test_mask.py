from src.masks import get_mask_account, get_mask_card_number

# The expected result is positive


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number, 14) == "Visa Platinum 7000 79** **** 6361"


def test_get_mask_account(account_number):
    assert get_mask_account(account_number, 5) == "Счет **4305"


def test_get_mask_card_number_no_input():
    assert get_mask_card_number() == ""


def test_get_mask_account_no_input():
    assert get_mask_account() == ""
