import pytest


@pytest.fixture()
def setup():
    print("******* `BEFORE` fixture - this action will be done before test ************")
    yield
    print("******* `AFTER` fixture - this action will be done after test ************")


def test_fixture_first(setup):
    print("<first test_with_fixture method> from test_fixture_first.py - run after fixture.")


def test_fixture_second():
    print("{second test_with_fixture method} from test_fixture_first.py} - run without fixture.")


@pytest.mark.smoke
def test_with_fixture_third(setup):
    print("[third test_with_fixture] method from test_fixture_first.py - run after fixture.")
