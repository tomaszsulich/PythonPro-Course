from pathlib import Path

# r mówi programowi, aby nie czytał ukośników jako elementów znaków specjalnych
rawpath = r"C:\Users\tomek\OneDrive\Desktop\PythonPro-Course\python_lessons"
lesson9 = rawpath + r"\lesson9.py"
print(lesson9)

print(Path() / "lesson9.py")
# string nie posiada atrybutu absolute odsyłającego do ścieżki bezwzględnej pliku!
# print(Path() / "lesson9.py".absolute())
# ale posiada go Path
print((Path() / "lesson9.py").absolute())

print(Path() / "lesson9" / "dane.txt") # ścieżka względna
p = Path() / "lesson9" / "dane.txt" # Windows Path i tak dalej