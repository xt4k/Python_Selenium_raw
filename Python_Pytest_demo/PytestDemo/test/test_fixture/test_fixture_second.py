import pytest

def test_fixture_first(setup):
    print("<first test_with_fixture method> from test_fixture_second.py - run after fixture.")


def test_fixture_second():
    print("{second test_with_fixture method} from test_fixture_second.py} - run without fixture.")


@pytest.mark.smoke
def test_with_fixture_third(setup):
    print("[third test_with_fixture] method from test_fixture_first.py - run after fixture.")
