from . import Article

# Stworzenie nowego artykułu i zapisanie go w bazie danych
# To jest odpowiednik polecenia INSERT INTO w SQL
new_article = Article.objects.create(
    title="Nowy artykuł o Django",
    content="Treść artykułu o potędze ORM."
)

# User.objects.filter(score__gt=10_000)
Article.objects.filter(title__contains="Django") # contains to filtr sprawdzający, czy tekst zawiera podaną frazę

ar = Article(title="Nowy artykuł o Django", 
             content="Treść artykułu o potędze ORM.")
ar.save()

print(f"Utworzono artykuł o ID: {new_article.id}")



r"le22\articles\static\articles\styles.css"
# Django interpretują wszystkie foldery static ze wszystkich aplikacji jako jeden folder
# dlatego używamy:
# nazwa_aplikacji/static/nazwa_aplikacji/...
# żeby uniknąć konfliktów nazw plików