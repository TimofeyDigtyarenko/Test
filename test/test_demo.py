import pytest


@pytest.fixture()         #создание фиксированного названия, при обращении к которому будет вызвана функция before_after
def before_after():
    print('Before test')
    yield                 #место для запуска автотеста
    print('\nAfter test')




def test_demo():
    assert 1 == 1

def test_demo2(before_after):
    assert 2 == 3
