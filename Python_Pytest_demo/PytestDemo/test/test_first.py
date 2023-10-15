import pytest


@pytest.mark.smoke
def test_method_first():
    print("`first pytest method from test_first.py` - marked as `smoke-test`.")
    pass


def test_method_second():
    print("`second pytest method from test_first.py`")
    pass


@pytest.mark.smoke
@pytest.mark.skip
def test_method_third(setup):
    print("[third pytest method from test_first.py]  - marked as `smoke-test`, but skipped so it should not run.")


@pytest.mark.regression
@pytest.mark.xfail
def test_method_fourth():
    print("(fourth pytest method from test_first.py)  - marked as `xfail`, so fails will not affect pass rate.")
    assert 2 == 3

@pytest.mark.regression
@pytest.mark.xfail
def test_method_fifth(setup):
    print("`fourth pytest method from test_first.py` - `xfail` marked, so pass not change pass rate. + CONFTEST FIXTURE")
    assert 2 == 2


@pytest.mark.regression
@pytest.mark.xfail
def test_method_sixth(setup):
    print("*6th pytest method from test_first.py* - `xfail`-ed, fails will not affect pass rate. with CONFTEST FIXTURE")
    assert 2 == 3

