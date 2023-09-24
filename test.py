# import json
from main import app


def test():
    print('inside test function')
    response = app.test_client().get('/')
    assert response.text == 'Welcome to Login system'
    print('return from endpoint is tested successfully')
    assert response.status_code == 200
    print('endpoint responded successfully')


def test2():
    print('inside test2 function')
    response = app.test_client().get('/product')
    print('response is', response.get_data())
    assert response.status_code == 200
    print('endpoint responded successfully')


test()
test2()
