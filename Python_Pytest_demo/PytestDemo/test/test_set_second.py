import pytest


@pytest.mark.usefixtures("setup_class")
class TestSet:
    @pytest.mark.smoke
    def test_method_first(self):
        print("`first pytest method from test_set_second.py` - marked as `smoke-test`.")

    pass

    def test_method_second(self):
        print("`second pytest method from test_set_second.py`")

    pass

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_method_third(self):
        print("[third pytest method from test_set_second.py] - marked as `smoke-test`, skipped so it should not run.")
