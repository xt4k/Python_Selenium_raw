# pytest files begin with `test_*` or end with `*_test` pytest method names should start with `test*` Any code should
# be wrapped in methods only Method manes should be valuable keys: -k - for method names selection, -s logs in
# output, -v - detailed info about metadata py.test test_second.py -v -s  - run test from file `test_second.py`
# `py.test -k method_third -v -s` - run test which contains `method_third` in name
# `py.test -m regression -v -s` - run test with mark `regression`
# @pytest.mark.skip allow skip test from run.  so it will be added to skipped in final report
# @pytest.mark.xfail - run test but `xfail`/`xpass` it result. will be added to `xpassed`/`xfailed` in final statistic

def test_first_program(setup):
    print("Hi")
    pass


def test_first_failed_one(actual_message="some_actual_message"):
    expected_message = "some_expected_message"
    assert actual_message == expected_message
