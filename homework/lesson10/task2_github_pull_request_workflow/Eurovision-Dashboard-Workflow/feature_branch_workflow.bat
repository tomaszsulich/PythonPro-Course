cd C:\Users\tomek

:: Clone repository (run only once)
IF NOT EXIST Eurovision-Dashboard-Workflow\.git (
    git clone git@github.com:tomaszsulich/Eurovision-Dashboard-Workflow.git
)

cd Eurovision-Dashboard-Workflow

:: Create feature branch (skip if branch already exists)
git checkout feature-readme 2>nul
IF ERRORLEVEL 1 (
    git checkout -b feature-readme
)

git add .
git commit -m "docs: update workflow script"

echo ## Planned features > projekt.md
echo - Interactive filters by year and decade >> projekt.md
echo - Average normalized points analysis >> projekt.md
echo - Jury and televoting comparison >> projekt.md

git add .
git commit -m "docs: expand project feature description"
git push -u origin feature-readme

git checkout main
git branch -d feature-readme