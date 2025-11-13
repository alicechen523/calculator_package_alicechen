# our package
from calculator_package_alicechen.calc_class import Calculator

# pip installed
from tqdm import tqdm

# built in
from pathlib import Path

class FileCalculator(Calculator):
    def sum_file(self, path=None) -> int:
        if path is None:
            path = Path(__file__).parent / "nums.csv"
        with tqdm(total=1_000_000, desc="summing file") as pbar:
            total = 0
            with path.open() as f:
                for line in f:
                    total += int(line)
                    pbar.update()
            return total
