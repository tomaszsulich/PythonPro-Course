from random import choice
from flask import Flask, render_template, request
from typing import TypedDict, NotRequired
from itertools import permutations

class Movie(TypedDict):
    """
    Reprezentuje pojedynczy film wyświetlany na stronie.
    
    Przechowuje podstawowe informacje o filmie oraz jego pozycję w obrębie danego gatunku.
    """
    
    title: str
    genre: str
    description: str
    genre_index: NotRequired[int]
    
class Book(TypedDict):
    """
    Określa strukturę danych pojedynczej książki.
    
    Definiuje wymagane pola wykorzystywane podczas walidacji
    i renderowania danych w szablonie HTML.
    """
    
    title: str
    author: str
    year: int

class GalleryImage(TypedDict):
    """
    Opisuje pozycję w galerii obrazów.
    
    Łączy adres grafiki z jej podpisem
    towarzyszącym jej na stronie.
    """
    
    url: str
    cap: str


app = Flask(__name__)

@app.route("/movies")
def show_movies() -> str:
    """
    Wyświetla listę ulubionych filmów.
    
    Funkcja:
    - przygotowuje dane filmów,
    - waliduje ich strukturę,
    - losuje kolejność kolorów dla gatunków,
    - numeruje filmy w obrębie gatunków,
    - przekazuje dane do szablonu movies.html.
    """
    
    # Konfiguracja listy filmów przekazywanej do szablonu (zadanie 3)
    favourite_movies: list[Movie] = [
        {"title": "Film o pszczołach", "genre": "animation", "description": "animacja / komedia"},
        {"title": "Pieprzyć Mickiewicza", "genre": "cinema", "description": "dramat młodzieżowy"},
        {"title": "Pieprzyć Mickiewicza 2", "genre": "cinema", "description": "dramat młodzieżowy"},
        {"title": "Pieprzyć Mickiewicza 3", "genre": "comedy", "description": "komedia obyczajowa"},
        {"title": "Vabank", "genre": "comedy", "description": "komedia kryminalna"},
        {"title": "Miś", "genre": "comedy", "description": "komedia"},
        {"title": "Fineasz i Ferb", "genre": "animation", "description": "animacja"},
    ]
    
    # Konfiguracja kolorów dostępnych dla poszczególnych gatunków
    genre_themes: dict[str, tuple[str, ...]] = {
        "classic": ("beige", "thistle", "aliceblue", "mintcream", "floralwhite"),
        "comedy": ("lightyellow", "palegreen", "oldlace", "mistyrose", "peachpuff"),
        "animation": ("paleturquoise", "lightcoral", "lightskyblue", "whitesmoke", "powderblue"),
        "cinema": ("rosybrown", "palegoldenrod", "silver", "lightslategray", "ghostwhite"),
    }
    
    # Walidacja podstawowej struktury danych
    required_keys: set[str] = {"title", "genre", "description"}
    validation_errors: list[str] = []
    
    for movie in favourite_movies:
        movie_keys = set(movie.keys())
        movie_keys_lower = {key.lower() for key in movie_keys}
        missing_keys = required_keys - movie_keys_lower
        
        wrong_case_keys = [
            key for key in movie_keys
            if key.lower() in required_keys and key not in required_keys
        ]
        
        if wrong_case_keys:
            validation_errors.append(
                f"{movie.get('title', 'Nieznany film')}: "
                f"popraw wielkość liter w kluczach: {', '.join(wrong_case_keys)}",
            )
        
        if missing_keys:
            validation_errors.append(
                f"{movie.get('title', 'Nieznany film')}: "
                f"brak pól: {', '.join(missing_keys)}",
            )
            
        elif movie["genre"] not in genre_themes:
            validation_errors.append(
                f"{movie['title']}: nieznany gatunek: {movie['genre']}",
            )
        
    for error in validation_errors:
        print(error)
        
    def randomize_colors(colors: tuple[str, ...]) -> tuple[str, str]:
        """
        Losuje uporządkowaną parę kolorów z puli przypisanej do gatunku.
        Kolejność kolorów ma znaczenie, ponieważ pierwszy kolor trafia
        do elementów nieparzystych, a drugi do parzystych.
        
        Args:
            colors: Krotka kolorów przypisanych do gatunku.
            
        Returns:
            tuple[str, str]:
                Pierwszy kolor dla elementów nieparzystych, drugi dla elementów parzystych.
        """
        color_pairs = list(permutations(colors, 2))
        return choice(color_pairs)
    
    # Przygotowanie wylosowanej kolejności kolorów dla każdego gatunku
    selected_genre_themes: dict[str, tuple[str, str]] = {}
    
    for genre, colors in genre_themes.items():
        selected_genre_themes[genre] = randomize_colors(colors)
    
    # Numerowanie filmów osobno w obrębie każdego gatunku
    genre_counter: dict[str, int] = {}
    
    for movie in favourite_movies:
        genre = movie["genre"]
        genre_counter[genre] = genre_counter.get(genre, 0) + 1
        movie["genre_index"] = genre_counter[genre]
    
    # Przekazanie przygotowanych danych do szablonu
    return render_template(
        "movies.html",
        movies = favourite_movies,
        # Dynamiczny tytuł strony (zadanie 4)
        page_title = "Moje ulubione filmy",
        genre_themes = selected_genre_themes,
    )
    
# Źródło danych dla widoku prezentującego kolekcję książek (zadanie 6)
@app.route("/books")
def show_books() -> str:
    """
    Obsługuje widok kolekcji książek, który waliduje dane, 
    interpretuje parametry sortowania i renderuje
    uporządkowaną listę książek.
    """
    
    books: list[Book] = [
        {
            "title": "Nie mów nikomu", 
            "author": "Karolina Wójciak", 
            "year": 2022,
        },
        
        {
            "title": "Krzyk",
            "author": "Tokuro Nukui",
            "year": 1993,
        },
        
        {
            "title": "Faworyci",
            "author": "Layne Fargo",
            "year": 2025,
        },
        
        {
            "title": "Simon kontra reszta homo sapiens",
            "author": "Becky Albertalli",
            "year": 2024,
        },
        
        {
            "title": "Love, Creekwood",
            "author": "Becky Albertalli",
            "year": 2024,
        },
    ]
    
    required_keys: set[str] = {"title", "author", "year"}
    validation_errors: list[str] = []
    
    for book in books:
        missing_keys = required_keys - book.keys()
        
        if missing_keys:
            validation_errors.append(
                f"{book.get('title', 'Nieznana książka')}: "
                f"brak pól: {', '.join(missing_keys)}",
            )
    
    for error in validation_errors:
        print(error)
    
    sort_keys = [
        request.args.get("sort_1"),
        request.args.get("sort_2"),
        request.args.get("sort_3"),
    ]
    sort_keys = [key.lower() for key in sort_keys if key]
    
    allowed_sort_keys: set[str] = {"title", "author", "year"}
    allowed_orders: set[str] = {"asc", "desc"}
    
    sort_keys = [key for key in sort_keys if key in allowed_sort_keys]
    unique_sort_keys: list[str] = []
    
    for key in sort_keys:
        if key not in unique_sort_keys:
            unique_sort_keys.append(key)
    
    sort_keys = unique_sort_keys
    
    if not sort_keys:
        sort_keys = ["title"]
        
    order = request.args.get("order", "asc").lower()

    if order not in allowed_orders:
        order = "asc"
    
    reverse_order = order == "desc"
    
    books = sorted(
        books,
        key = lambda book: tuple(book[key] for key in sort_keys),
        reverse = reverse_order,
    )
    
    return render_template(
        "books.html",
        books = books,
        page_title = "Moje książki",
        sort_keys = sort_keys,
        order = order,
    )
    
# Galeria obrazów wraz z przypisanymi opisami (zadanie 7)
@app.route("/gallery")  
def gallery() -> str:
    """
    Udostępnia galerię obrazów 
    wraz z przypisanymi opisami.
    
    Gromadzi zasoby wykorzystywane
    przez galerię aplikacji. 
    """
    
    # Struktura listy pozwala skalować galerię bez zmiany pętli w szablonie.
    imgs: list[GalleryImage] = [
        {
            "url": "https://tse4.mm.bing.net/th/id/OIP.KT0rjWfTkAi67Uv_t_pQNAHaF_?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
            "cap": "Ilustracja związana z projektowaniem graficznym",
        },
        
        {
            "url": "https://public-images.interaction-design.org/literature/articles/materials/ixdf-design-skills-required-by-graphic-artists-and-graphic-designers.png",
            "cap": "Kluczowe umiejętności związane z projektowaniem graficznym",
        },
    ]
    return render_template(
        "gallery.html",
        imgs = imgs,
    )

   
if __name__ == "__main__":
    app.run(debug=True)