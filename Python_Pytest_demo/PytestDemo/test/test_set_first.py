import pytest

@pytest.mark.usefixtures("setup")
class TestSet:
    @pytest.mark.smoke
    def test_method_first(self):
        print("`first pytest method from test_set_first.py` - marked as `smoke-test`.")
    pass

    def test_method_second(self):
        print("`second pytest method from test_set_first.py`")
    pass

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_method_third(self):
        print("[third pytest method from test_set_first.py]  - marked as `smoke-test`, but skipped so it should not run.")
        
        
    @pytest.mark.regression
    @pytest.mark.xfail
    def test_method_fourth(self):
        print("(fourth pytest method from test_set_first.py)  - marked as `xfail`, so fails will not affect pass rate.")
        assert 2 == 3


    @pytest.mark.regression
    @pytest.mark.xfail
    def test_method_fifth(self):
        print("`fourth pytest method from test_set_first.py` - `xfail` marked, so pass not change pass rate. + CONFTEST FIXTURE")
        assert 2 == 2
    @pytest.mark.regression
    @pytest.mark.xfail
    def test_method_sixth(self):
        print("*6th pytest method from test_set_first.py* - `xfail`-ed, fails will not affect pass rate. with CONFTEST FIXTURE")
        assert 2 == 3
