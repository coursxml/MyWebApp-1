import pytest

def test_login():
    url_attendue= 'https://login.salesforce.com'
    url_obtenue = 'https://login.salesforce.com'
    # if url_obtenue==url_attendue:
    #      print('test past')
    # else:
    #     print('test failed')
    print('copy de validation')
    assert url_attendue==url_obtenue , 'les url sont differentes'
    assert 'login' in url_obtenue
    assert  False,'je force la test a echouer'  #pour forcer un test a etre en echec
    #assert  true # pour forcer un test a etre true
    print('fin de verification ') # ce print ne va pas s'afficher parceque le assert false s'appel
    #hard assertion si il est en echec le reste des validation ne seront pas executer

