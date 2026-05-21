import os
from pathlib import Path

os.path.join(os.getcwd(), "lesson9", "dane.txt")
p = Path() / "lesson9" / "dane.txt"

p = open(Path() / "lesson9" / "safe_calculator_dict.py")
# ale są biblioteki, które tego nie łykną, więc bezpieczniejsze
p = open(str(Path() / "lesson9" / "safe_calculator_dict.py"))