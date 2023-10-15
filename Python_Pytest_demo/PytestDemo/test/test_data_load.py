import pytest


@pytest.mark.usefixtures("data_load")
class TestWithData:

    def test_do_some_action(self, data_load):
        print(data_load)
