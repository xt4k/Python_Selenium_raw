import pytest

from test_base_class import BaseClass


@pytest.mark.usefixtures("data_load")
class TestWithLogging(BaseClass):

    def test_do_some_action(self, data_load):

        log = self.get_logger()

        print(data_load[0])
        log.info(data_load[0])

        log.info(data_load)
        print(data_load)
