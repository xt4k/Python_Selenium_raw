import pytest


@pytest.mark.smoke
def test_method_first(setup):
    print("<<first pytest method from test_second.py>>  - marked as `smoke-test`.")
    pass


@pytest.mark.regression
def test_method_second():
    print("{{second pytest method from test_second.py}}  - marked as `regression-test`.")
    pass


@pytest.mark.smoke
def test_method_third(setup):
    print("[[third pytest method from test_second.py]] - marked as `smoke-test`.")
    pass
