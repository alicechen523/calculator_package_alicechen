from calculator_package_alicechen.file_calc import FileCalculator


def test_file_calc():
    assert FileCalculator.sum_file() == 6
