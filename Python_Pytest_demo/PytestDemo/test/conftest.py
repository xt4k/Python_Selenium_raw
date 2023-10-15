import pytest


@pytest.fixture()
def setup():
    print("******* `BEFORE` fixture  from CONFTEST.PY - this action will be done before test ************")
    yield
    print("******* `AFTER` fixture  from CONFTEST.PY - this action will be done after test ************")


@pytest.fixture(scope="class")
def setup_class():
    print("******* `BEFORE` `class-scope` fixture from CONFTEST.PY - action will be done before test class ONCE ******")
    yield
    print("******* `AFTER` `class-scope` fixture from CONFTEST.PY - action will be done after test class ONCE *******")


@pytest.fixture()
def data_load():
    print("~~~~~`DATA-LOAD` from CONFTEST.PY -  some action will be done before test  ******")
    return ["Yuriy", "L.", "https://github.com/xt4k"]


@pytest.fixture(params=[("chrome", "Yuriy", "L."), "firefox", ("edge","better not use"), "internet explorer", "safari"])
def data_sets(request):
    print("Data set returns:",request.param)
    return request.param
