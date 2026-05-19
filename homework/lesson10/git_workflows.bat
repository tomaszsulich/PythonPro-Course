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

git commit -m "feat: add multilingual hello world support" -m "The app now lets the user choose a language instead of printing only one hardcoded message"

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

git commit -m "Change hello world message to Polish"

git reset --hard HEAD~1
:: git reset --hard przywraca repozytorium do dokładnego stanu z wybranego commita. Cofane są nie tylko commity, ale także zmiany
:: w stagingu i plikach lokalnych.


:: task 7
git checkout main
git checkout -b feature-branch

git add .
git commit -m "feat: add first line of function docstring"

git add .
git commit -m "fix: update second line of calculator"

git add .
git commit -m "docs: add comment about hard reset"

git rebase -i HEAD~3
git push

:: task 8
git init

echo Linia 1 - main version > conflict_example.txt
git add .
git commit -m "feat: added first line"

git checkout -b branch-A
echo Linia 1 - changed in branch-A > conflict_example.txt
git add .
git commit -m "feat: changed first line in branch-A"

git checkout main
echo Linia 1 - changed in main > conflict_example.txt
git add .
git commit -m "fix: changed first line in main"

git merge branch-A

:: Po konflikcie ręcznie rozwiązujemy plik. Zostawiamy jedną wspólną wersję bez markerów <<<<<<< ======= >>>>>>>.

echo Linia 1 - changed after conflict resolution > conflict_example.txt
git add conflict_example.txt
git commit -m "fix: update file after conflict resolution"

:: task 10
:: Simulating Git Flow manually without git-flow extension

git init
git branch -M main

git checkout -b develop


:: feature branch
git checkout -b feature-moja-funkcja
git commit -m "docs: added first and second line"
git commit -m "fix: update second line"
git commit -m "feat: append calculator function"


:: finish feature
git checkout develop
git merhe feature-moja-funkcja


:: release branch
git checkout -b release-1.0.0
git commit -m "fix: append except in calculator"


:: finish release
git checkout main
git merge release-1.0.0

git checkout develop
git merge release-1.0.0