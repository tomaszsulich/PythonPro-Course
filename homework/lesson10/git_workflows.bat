@echo off
chcp 65001

:: task 1
git init
git branch -M main

echo Simple Git training project > README.md

git add README.md
git commit -m "docs: add README file"
git log --oneline --graph --decorate --all

:: task 2
git checkout -b feature-login

echo # login feature > login.py

git add .
git commit -m "feat: add login file"
git checkout main
git merge feature-login

:: task 3
git clone git@github.com:tomaszsulich/PythonPro-Course.git PythonPro-Course-test

cd PythonPro-Course-test

git checkout -b testing

echo Tomasz Sulich > contributors.txt

git add .
git commit -m "docs: add contributor information"
git push -u origin testing

:: task 4
mkdir team-project-basic
cd team-project-basic

git init
git config user.name "Tomasz"
git config user.email "tomeksulich5@gmail.com"
git config --list

:: task 5
echo print("Hello world!") > app.py

git add app.py
git commit -m "feat: add hello world function"

echo print("Cześć świecie!") > app.py

git status
git add app.py
git commit -m "fix: change hello world message to Polish"

:: task 6
echo(# Simple multilingual hello world app > app.py
echo def hello_world(language^): >> app.py
(
echo     messages = {
echo 	     "pl": "Cześć świecie!",
echo 	     "en": "Hello world!",
echo         "fr": "Bonjour le monde!",
echo         "it": "Ciao mondo!",
echo         "es": "Hola mundo!"
echo     }
) >> app.py

echo. >> app.py

echo     print(messages.get(language, "Language not supported")) >> app.py

echo. >> app.py
echo. >> app.py

(
echo user_language = input^("Choose language (pl/en/fr/it/es): "^)
echo hello_world(user_language^)
) >> app.py

git add .
git reset HEAD app.py

echo(# Simple Polish hello world app >> app.py
echo message = "Cześć świecie!" >> app.py
echo print(message) >> app.py

git add .
git commit -m "fix: change hello world message to Polish" -m "The app is changed back to a simple Polish message to demonstrate committing new changes before using git reset --hard."

git reset --hard HEAD~1
:: git reset --hard przywraca repozytorium do dokładnego stanu z wybranego commita. Cofane są nie tylko commity, ale także zmiany
:: w stagingu i plikach lokalnych.


:: task 7
git checkout main
git checkout -b feature-branch

echo def calculate(a, b, operation^): > calculator.py
echo     """Perform arithmetic operations and return the result.""" >> calculator.py
git add .
git commit -m "feat: add first line of function docstring"

echo     if operation == "/": >> calculator.py
echo         return a / b if b != 0 else "Cannot divide by zero!" >> calculator.py
git add .
git commit -m "fix: update second line of calculator"

echo # git reset --hard removes local changes and restores repository state >> calculator.py
git add .
git commit -m "docs: add comment about hard reset"

git rebase -i HEAD~3

:: In the editor:
:: 1. Leave the first commit as pick.
:: 2. Change the second and third commits from pick to squash.
:: 3. Save and close the editor.
:: 4. Set the final commit message to:
:: feat: add calculator changes and hard reset note

git push --force

:: task 8
git init
git branch -M main

echo Line 1 - main version > conflict_example.txt
git add .
git commit -m "feat: added first line"

git checkout -b branch-A
echo Line 1 - main version > conflict_example.txt
echo Line 2 - from branch-A >> conflict_example.txt
git add .
git commit -m "feat: added second line in branch-A"

git checkout main
echo Line 1 - changed in main > conflict_example.txt
echo Line 2 - from main >> conflict_example.txt
git add .
git commit -m "fix: changed first line and added second line in main"

git merge branch-A

:: Resolve the conflict manually in conflict_example.txt.
:: Remove conflict markers and keep the final desired version.

git add conflict_example.txt
git commit -m "fix: resolve merge conflict"

:: task 10
:: Simulating Git Flow manually without git-flow extension

git init
git branch -M main

git checkout -b develop


:: feature branch
git checkout -b feature-calculator

echo def divide(a, b^): > calculator.py
echo     return a / b >> calculator.py
git add .
git commit -m "docs: added first and second line"

echo def multiply(a, b^): >> calculator.py
git add .
git commit -m "fix: update second line"

echo def subtract(a, b^): >> calculator.py
echo     return a - b >> calculator.py
git commit -m "feat: append calculator function"


:: finish feature
git checkout develop
git merge feature-calculator


:: release branch
git checkout -b release-1.0.0

echo Release fix: division by zero should be handled in calculator.py >> release_notes.txt
git add .
git commit -m "fix: document division by zero handling"


:: finish release
git checkout main
git merge release-1.0.0

git checkout develop
git merge release-1.0.0