import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import calculator, helpers

print("starting app")

x = input("Enter your name: ")
print("Hello " + x)

result = calculator.add(5, 3)
print("Result:", result)

data = helpers.get_data()
print("Data:", data)
