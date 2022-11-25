import pytest


def get_data():
    return[
        ('anis','aouadi'),
        ('anis1', 'aouadi1'),
        ('anis2', 'aouadi2'),
        ('anis3', 'aouadi3')
    ]


@pytest.mark.parametrize('username, password',get_data())
def test_login(username,password):
    print(username, '-------' , password,'------')