import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from src import calculator


def test_add():
    assert calculator.add(2, 3) == 5


def test_subtract():
    assert calculator.subtract(5, 3) == 2
