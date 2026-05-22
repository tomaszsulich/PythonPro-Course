mkdir Git-Merge-Conflict-Resolution
cd Git-Merge-Conflict-Resolution

git init
git branch -M main

echo Shared deployment instructions for the production environment. > konflikt.txt

git add .
git commit -m "docs: add initial deployment instructions"

git checkout galaz-A 2>nul
IF ERRORLEVEL 1 (
    git checkout -b galaz-A
)

echo Rollback steps must be verified before every production release. >> konflikt.txt

git add .
git commit -m "docs: add rollback instructions from galaz-A"

git checkout main
echo Production deployment requires approval from the release manager. >> konflikt.txt

git add .
git commit -m "docs: add release manager approval requirement"
git merge galaz-A
