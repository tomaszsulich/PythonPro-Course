import io
import random
from dataclasses import dataclass
from pathlib import Path

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from faker import Faker
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFont, ImageOps

from library.models import Author, Book, BookCopy, Genre


GENRE_SETS = [
    ("Fantastyka",),
    ("Kryminał",),
    ("Literatura piękna",),
    ("Nauka",),
    ("Historia",),
    ("Fantastyka", "Literatura piękna"),
    ("Fantastyka", "Historia"),
    ("Kryminał", "Literatura piękna"),
    ("Kryminał", "Historia"),
    ("Nauka", "Historia"),
    ("Historia", "Literatura piękna"),
]

SCIENCE_TOPICS = [
    ("algorytmów", "computer,technology"),
    ("matematyki", "mathematics,formula"),
    ("astronomii", "telescope,stars"),
    ("wynalazków", "gears,machine"),
    ("technologii", "electronics,circuit"),
    ("kosmosu", "galaxy,stars"),
]

HISTORY_TOPICS = [
    ("dawnych cywilizacji", "ancient,ruins"),
    ("wielkich odkryć", "old,map"),
    ("starego miasta", "oldtown,street"),
    ("kolei", "steam,train"),
    ("wynalazków", "gears,vintage"),
]

CRIME_MOTIFS = [
    ("starego domu", "abandoned,house"),
    ("nocnego pociągu", "train,night"),
    ("zaginionego listu", "old,letter"),
    ("ostatniego śladu", "footprint,ground"),
    ("zamkniętego pokoju", "closed,door"),
]

FANTASY_NOUNS = [
    ("ogród", "garden,flowers"),
    ("las", "green,forest"),
    ("labirynt", "hedge,maze"),
    ("most", "stone,bridge"),
    ("zamek", "castle,ruins"),
]

FANTASY_ADJECTIVES = [
    "Ukryty",
    "Zapomniany",
    "Zaginiony",
    "Cichy",
    "Ostatni",
]

LITERARY_MOTIFS = [
    ("Dom nad jeziorem", "house,lake"),
    ("Między światłem a ciszą", "window,sunlight"),
    ("Ostatnia podróż", "empty,road"),
    ("List bez powrotu", "letter,desk"),
    ("Opowieść z końca mapy", "old,map"),
]

DESCRIPTION_OPENINGS = {
    "Fantastyka": [
        "Opowieść prowadzi bohaterów do świata, w którym dawne reguły przestają obowiązywać.",
        "Historia łączy codzienność z tajemnicą i stopniowo poszerza granice znanego świata.",
    ],
    "Kryminał": [
        "Punktem wyjścia jest zagadka, której rozwiązanie okazuje się bardziej złożone, niż początkowo sądzono.",
        "Jedno pozornie drobne odkrycie uruchamia ciąg zdarzeń prowadzących do niewygodnej prawdy.",
    ],
    "Literatura piękna": [
        "Książka skupia się na relacjach, pamięci i decyzjach, które zmieniają codzienne życie bohaterów.",
        "To spokojna opowieść o ludziach próbujących uporządkować własną przeszłość i teraźniejszość.",
    ],
    "Nauka": [
        "Autor przystępnie wprowadza czytelnika w najważniejsze pojęcia i pokazuje ich praktyczne znaczenie.",
        "Książka porządkuje podstawowe zagadnienia i wyjaśnia je na przykładach bez zbędnego formalizmu.",
    ],
    "Historia": [
        "Książka przygląda się wydarzeniom z szerszej perspektywy i pokazuje ich wpływ na późniejsze przemiany.",
        "Autor prowadzi czytelnika przez wybrany fragment przeszłości, zwracając uwagę na ludzi i kontekst epoki.",
    ],
}

DESCRIPTION_ENDINGS = [
    "Całość napisana jest w przystępnym stylu i nie wymaga wcześniejszej znajomości tematu.",
    "Narracja rozwija się stopniowo, pozostawiając miejsce zarówno na szczegóły, jak i własną interpretację.",
    "To propozycja dla czytelników, którzy lubią historie prowadzone spokojnie, ale z wyraźnym pomysłem.",
    "Książka sprawdzi się jako lekka lektura, ale daje też kilka tematów do dalszego zastanowienia.",
]

CoverFont = ImageFont.FreeTypeFont | ImageFont.ImageFont
COVER_WIDTH = 700
COVER_HEIGHT = 1210
COVER_SOURCE_DIR = (
    Path(__file__).resolve().parents[2]
    / "static"
    / "library"
    / "cover_sources"
)

TITLE_COLOR = (246, 241, 229, 255)
AUTHOR_COLOR = (224, 165, 74, 255)
BRAND_COLOR = (245, 241, 232, 255)
EDITION_COLOR = (221, 217, 208, 255)

SHORT_POLISH_WORDS = {
    "a", "i", "o", "u", "w", "z", "do", "na", "od", "po", "za", "ze", "bez"
}

TITLE_PROTECTED_PHRASES = (
    "do algorytmów",
    "do matematyki",
    "do astronomii",
    "do technologii",
    "do kosmosu",
    "z końca mapy",
    "zamkniętego pokoju",
    "starego domu",
    "nocnego pociągu",
    "zaginionego listu",
    "ostatniego śladu",
    "dawnych cywilizacji",
    "starego miasta",
)


@dataclass(frozen=True)
class CoverPreset:
    title: str
    primary_genre: str
    asset_name: str
    title_x: int = 78
    title_y: int = 96
    title_max_width: int = 545
    title_font_max: int = 92
    title_font_min: int = 66
    author_gap: int = 34
    brand_x: int = 78
    brand_y: int = 1105
    edition_y: int = 1150
    darken_left: int = 70
    darken_top: int = 44


COVER_PRESETS = (
    CoverPreset(
        title="Tajemnica starego domu",
        primary_genre="Kryminał",
        asset_name="crime_old_house.jpg",
        title_max_width=520,
        darken_left=76,
        darken_top=48,
    ),
    CoverPreset(
        title="Wprowadzenie do algorytmów",
        primary_genre="Nauka",
        asset_name="science_algorithms.jpg",
        title_max_width=555,
        darken_left=64,
        darken_top=48,
    ),
    CoverPreset(
        title="Śladami kolei",
        primary_genre="Historia",
        asset_name="history_railway.jpg",
        title_max_width=360,
        darken_left=62,
        darken_top=38,
    ),
    CoverPreset(
        title="Historia wielkich odkryć",
        primary_genre="Historia",
        asset_name="history_discoveries.jpg",
        title_max_width=390,
        darken_left=70,
        darken_top=50,
    ),
    CoverPreset(
        title="Cichy las",
        primary_genre="Fantastyka",
        asset_name="fantasy_quiet_forest.jpg",
        title_max_width=475,
        darken_left=56,
        darken_top=30,
    ),
    CoverPreset(
        title="Wprowadzenie do kosmosu",
        primary_genre="Nauka",
        asset_name="science_space.jpg",
        title_max_width=560,
        darken_left=58,
        darken_top=36,
    ),
    CoverPreset(
        title="Psychologia codzienności",
        primary_genre="Nauka",
        asset_name="literary_psychology.jpg",
        title_max_width=555,
        darken_left=66,
        darken_top=44,
    ),
    CoverPreset(
        title="Opowieści z dawnych lat",
        primary_genre="Literatura piękna",
        asset_name="literary_old_stories.jpg",
        title_max_width=555,
        darken_left=62,
        darken_top=34,
    ),
    CoverPreset(
        title="Bezpieczeństwo w cyfrowym świecie",
        primary_genre="Nauka",
        asset_name="science_cybersecurity.jpg",
        title_max_width=550,
        title_font_max=86,
        title_font_min=62,
        darken_left=72,
        darken_top=48,
    ),
    CoverPreset(
        title="Światło i kompozycja",
        primary_genre="Literatura piękna",
        asset_name="literary_light_composition.jpg",
        title_max_width=530,
        darken_left=72,
        darken_top=46,
    ),
)


def _generate_title(fake: Faker, primary_genre: str) -> tuple[str, str]:
    """Generuje tytuł i konkretne słowa kluczowe opisujące jego motyw."""
    if primary_genre == "Nauka":
        topic, keywords = fake.random_element(SCIENCE_TOPICS)
        return f"Wprowadzenie do {topic}", keywords

    if primary_genre == "Historia":
        topic, keywords = fake.random_element(HISTORY_TOPICS)
        prefix = fake.random_element(["Śladami", "Historia"])
        return f"{prefix} {topic}", keywords

    if primary_genre == "Kryminał":
        motif, keywords = fake.random_element(CRIME_MOTIFS)
        return f"Tajemnica {motif}", keywords

    if primary_genre == "Fantastyka":
        adjective = fake.random_element(FANTASY_ADJECTIVES)
        noun, keywords = fake.random_element(FANTASY_NOUNS)
        return f"{adjective} {noun}", keywords

    return fake.random_element(LITERARY_MOTIFS)


def _generate_unique_title(fake: Faker, primary_genre: str) -> tuple[str, str]:
    """Generuje niepowtarzalny tytuł spójny z głównym gatunkiem książki."""
    while True:
        title, cover_keywords = _generate_title(fake, primary_genre)
        if not Book.objects.filter(title=title).exists():
            return title, cover_keywords


def _generate_description(fake: Faker, primary_genre: str) -> str:
    """Buduje krótki opis zgodny z głównym gatunkiem książki."""
    opening = fake.random_element(DESCRIPTION_OPENINGS[primary_genre])
    ending = fake.random_element(DESCRIPTION_ENDINGS)
    return f"{opening} {ending}"


def _load_cover_font(size: int, *, role: str) -> CoverFont:
    """Ładuje font możliwie zbliżony do typografii serii na Windows i Linux."""
    serif_candidates = [
        "C:/Windows/Fonts/georgia.ttf",
        "C:/Windows/Fonts/times.ttf",
        "/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    ]
    
    sans_candidates = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    candidates = sans_candidates if role == "edition" else serif_candidates

    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue

    return ImageFont.load_default()


def _text_width(draw: ImageDraw.ImageDraw, text: str, font: CoverFont) -> int:
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def _protect_title_phrases(title: str) -> list[str]:
    """Zamienia logiczne frazy na nierozdzielne tokeny używane przy łamaniu tytułu."""
    protected_title = title
    placeholders: dict[str, str] = {}

    for index, phrase in enumerate(TITLE_PROTECTED_PHRASES):
        if phrase.lower() not in protected_title.lower():
            continue

        words = protected_title.split()
        phrase_words = phrase.split()
        phrase_len = len(phrase_words)

        for start in range(len(words) - phrase_len + 1):
            candidate = " ".join(words[start:start + phrase_len])
            if candidate.lower() == phrase.lower():
                placeholder = f"__PHRASE_{index}__"
                placeholders[placeholder] = candidate
                words[start:start + phrase_len] = [placeholder]
                protected_title = " ".join(words)
                break

    return [placeholders.get(token, token) for token in protected_title.split()]


def _wrap_cover_title(
    draw: ImageDraw.ImageDraw,
    title: str,
    font: CoverFont,
    max_width: int,
    *,
    protect_phrases: bool = True,
) -> list[str]:
    """Łamie tytuł naturalnie, zachowując krótkie słowa i chronione frazy."""
    tokens = _protect_title_phrases(title) if protect_phrases else title.split()
    lines: list[str] = []
    current: list[str] = []

    for token in tokens:
        candidate_tokens = [*current, token]
        candidate = " ".join(candidate_tokens)

        if _text_width(draw, candidate, font) <= max_width or not current:
            current = candidate_tokens
            continue

        if current[-1].lower() in SHORT_POLISH_WORDS:
            orphan = current.pop()
            if current:
                lines.append(" ".join(current))
            current = [orphan, token]
        else:
            lines.append(" ".join(current))
            current = [token]

    if current:
        lines.append(" ".join(current))

    return lines


def _fit_cover_title(draw: ImageDraw.ImageDraw, title: str,
                     preset: CoverPreset) -> tuple[CoverFont, list[str], int]:
    """Dobiera font i interlinię tak, aby tytuł mieścił się w maksymalnie trzech wierszach."""
    for size in range(preset.title_font_max, preset.title_font_min - 1, -2):
        font = _load_cover_font(size, role="title")
        lines = _wrap_cover_title(draw, title, font, preset.title_max_width)
        if len(lines) <= 3 and all(
            _text_width(draw, line, font) <= preset.title_max_width
            for line in lines
        ):
            line_gap = max(2, round(size * 0.02))
            return font, lines, line_gap

    emergency_min = max(28, preset.title_font_min - 38)
    for size in range(preset.title_font_min, emergency_min - 1, -2):
        font = _load_cover_font(size, role="title")
        lines = _wrap_cover_title(
            draw,
            title,
            font,
            preset.title_max_width,
            protect_phrases=False,
        )
        if all(
            _text_width(draw, line, font) <= preset.title_max_width
            for line in lines
        ):
            return font, lines, max(1, round(size * 0.02))

    font = _load_cover_font(emergency_min, role="title")
    return font, _wrap_cover_title(
        draw,
        title,
        font,
        preset.title_max_width,
        protect_phrases=False,
    ), 1


def _apply_tonal_treatment(image: Image.Image, preset: CoverPreset) -> Image.Image:
    """Delikatnie uspokaja zdjęcie pod jasną typografią bez tworzenia panelu lub boxa."""
    image = ImageEnhance.Contrast(image).enhance(1.04)
    image = ImageEnhance.Color(image).enhance(0.94)

    horizontal = Image.linear_gradient("L").rotate(90, expand=False).resize(image.size)
    horizontal = ImageOps.invert(horizontal).point(
        lambda value: round(value * preset.darken_left / 255)
    )

    vertical = Image.linear_gradient("L").resize(image.size)
    vertical = ImageOps.invert(vertical).point(
        lambda value: round(value * preset.darken_top / 255)
    )

    combined = ImageChops.lighter(horizontal, vertical)
    shadow = Image.new("RGB", image.size, (4, 7, 9))
    return Image.composite(shadow, image, combined)


def _draw_spaced_text(draw: ImageDraw.ImageDraw,
                      position: tuple[int, int],
                      text: str, font: CoverFont, 
                      fill: tuple[int, int, int, int],
                      spacing: int) -> None:
    """Rysuje tekst z subtelnym trackingiem charakterystycznym dla bloku autora."""
    x, y = position
    
    for character in text:
        draw.text((x, y), character, fill=fill, font=font)
        x += _text_width(draw, character, font) + spacing


def _fit_author_font(draw: ImageDraw.ImageDraw, author_label: str, max_width: int) -> tuple[CoverFont, int]:
    """Dobiera dyskretny rozmiar autora; przy długiej nazwie zmniejsza tracking i font."""
    for size in range(30, 23, -1):
        font = _load_cover_font(size, role="author")
        
        for spacing in range(3, -1, -1):
            width = sum(_text_width(draw, char, font) for char in author_label)
            width += max(0, len(author_label) - 1) * spacing
            
            if width <= max_width:
                return font, spacing

    return _load_cover_font(23, role="author"), 0


def _generate_cover(title: str, author_names: list[str], preset: CoverPreset) -> ContentFile:
    """Składa lokalny asset i typografię w spójny front okładki BiblioTech."""
    source_path = COVER_SOURCE_DIR / preset.asset_name
    
    with Image.open(source_path) as source_image:
        background = source_image.convert("RGB")

    image = ImageOps.fit(
        background,
        (COVER_WIDTH, COVER_HEIGHT),
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    )
    
    image = _apply_tonal_treatment(image, preset).convert("RGBA")
    draw = ImageDraw.Draw(image)

    title_font, title_lines, line_gap = _fit_cover_title(draw, title, preset)
    title_y = preset.title_y

    for line in title_lines:
        draw.text(
            (preset.title_x, title_y),
            line,
            fill=TITLE_COLOR,
            font=title_font,
        )
        
        bbox = draw.textbbox((0, 0), line, font=title_font)
        line_height = bbox[3] - bbox[1]
        title_y += line_height + line_gap

    author_label = " · ".join(author_names).upper()
    
    author_font, author_spacing = _fit_author_font(
        draw,
        author_label,
        COVER_WIDTH - preset.title_x - 72,
    )
    
    author_y = title_y + preset.author_gap
    
    _draw_spaced_text(
        draw,
        (preset.title_x, author_y),
        author_label,
        author_font,
        AUTHOR_COLOR,
        author_spacing,
    )

    brand_font = _load_cover_font(39, role="brand")
    edition_font = _load_cover_font(19, role="edition")
    
    draw.text(
        (preset.brand_x, preset.brand_y),
        "BiblioTech",
        fill=BRAND_COLOR,
        font=brand_font,
    )
    
    draw.text(
        (preset.brand_x, preset.edition_y),
        "wydanie demonstracyjne",
        fill=EDITION_COLOR,
        font=edition_font,
    )

    buffer = io.BytesIO()
    
    image.convert("RGB").save(
        buffer,
        format="JPEG",
        quality=92,
        optimize=True,
        progressive=True,
    )
    
    return ContentFile(buffer.getvalue())


def _cover_preset_for_index(index: int) -> CoverPreset:
    """Wybiera semantycznie kompletny preset dla książek, które mają otrzymać okładkę."""
    cover_position = index // 3
    return COVER_PRESETS[cover_position % len(COVER_PRESETS)]


class Command(BaseCommand):
    help = "Tworzy przykładowe dane BiblioTech."

    def handle(self, *args, **options) -> None:
        fake = Faker("pl_PL")

        genre_by_name = {
            name: Genre.objects.get_or_create(name=name)[0]
            for name in [
                "Fantastyka",
                "Kryminał",
                "Literatura piękna",
                "Nauka",
                "Historia",
            ]
        }

        authors = []

        for _ in range(8):
            first_name = fake.first_name()
            last_name = fake.last_name()
            author, _ = Author.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                defaults={
                    "description": f"{first_name} {last_name}",
                },
            )
            authors.append(author)

        for index in range(12):
            cover_preset = _cover_preset_for_index(index) if index % 3 == 0 else None

            if cover_preset is not None:
                primary_genre = cover_preset.primary_genre
                genre_names = [primary_genre]
                title = cover_preset.title
            else:
                genre_names = list(random.choice(GENRE_SETS))
                primary_genre = genre_names[0]
                title, _ = _generate_unique_title(fake, primary_genre)

            selected_genres = [genre_by_name[name] for name in genre_names]

            book = Book.objects.create(
                title=title,
                description=_generate_description(fake, primary_genre),
                publication_year=random.randint(1950, 2026),
            )

            author_count = 1 if cover_preset is not None else random.randint(1, 2)
            selected_authors = random.sample(authors, k=author_count)
            book.authors.set(selected_authors)
            book.genres.set(selected_genres)

            if cover_preset is not None:
                author_names = [str(author) for author in selected_authors]
                cover = _generate_cover(title, author_names, cover_preset)
                book.cover.save(f"cover_{book.pk}.jpg", cover, save=True)

            for copy_number in range(1, random.randint(1, 3) + 1):
                BookCopy.objects.create(
                    book=book,
                    inventory_code=f"BT-{book.pk:03d}-{copy_number}",
                )

        User.objects.get_or_create(username="czytelnik")

        self.stdout.write(self.style.SUCCESS("Utworzono dane demonstracyjne BiblioTech."))