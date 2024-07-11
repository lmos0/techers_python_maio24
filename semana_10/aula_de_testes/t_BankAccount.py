import pytest
from BankAccount import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)


def test_get_balance(account):
    assert account.get_balance() == 100

def test_deposit(account):
    account.deposit(50)
    assert account.get_balance() == 150

    with pytest.raises(ValueError):
        account.deposit(-10)

def test_withdraw(account):
    account.withdraw(30)
    assert account.get_balance() == 70

    with pytest.raises(ValueError):
        account.withdraw(-10)
    
    with pytest.raises(ValueError):
        account.withdraw(200)

def test_insufficient_funds(account):
    with pytest.raises(ValueError):
        account.withdraw(200) 
