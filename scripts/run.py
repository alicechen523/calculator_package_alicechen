from pathlib import Path

from calculator_package_alicechen.calc_class import Calculator
from calculator_package_alicechen.file_calc import FileCalculator

print(Calculator().add(1,2))
FileCalculator().sum_file(Path("~/3150/class_examples/nums.csv").expanduser())
