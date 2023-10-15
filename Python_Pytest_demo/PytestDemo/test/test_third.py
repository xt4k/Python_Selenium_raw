import pytest


@pytest.mark.regression
def test_method_first():
    print(f"<<<first pytest method from test_third.py>>>  - marked as `regression-test`.")


def test_method_second(setup):
    print("{{{second pytest method from test_third.py}}}")


@pytest.mark.smoke
def test_method_third(setup):
    print("[[[third pytest method from test_third.py]]]  - marked as `smoke-test`.")
