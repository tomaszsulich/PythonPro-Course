import io
from tempfile import TemporaryDirectory
from unittest.mock import patch

from django.core.files.base import ContentFile
from django.core.management import call_command
from django.test import SimpleTestCase, TestCase, override_settings
from PIL import Image, ImageDraw

from library.management.commands.seed_db import (
    COVER_HEIGHT,
    COVER_PRESETS,
    COVER_WIDTH,
    _fit_cover_title,
    _generate_cover,
)
from library.models import Book


class CoverCompositionTests(SimpleTestCase):
    def test_generated_cover_is_a_jpeg_with_expected_dimensions(self) -> None:
        preset = COVER_PRESETS[0]

        cover = _generate_cover(
            preset.title,
            ["Jan Kowalski"],
            preset,
        )

        with Image.open(io.BytesIO(cover.read())) as image:
            self.assertEqual(image.format, "JPEG")
            self.assertEqual(image.size, (COVER_WIDTH, COVER_HEIGHT))

    def test_protected_title_phrase_stays_together_when_it_fits(self) -> None:
        preset = next(
            preset
            for preset in COVER_PRESETS
            if preset.title == "Wprowadzenie do algorytmów"
        )
        
        canvas = Image.new("RGB", (COVER_WIDTH, COVER_HEIGHT))
        draw = ImageDraw.Draw(canvas)

        _, lines, _ = _fit_cover_title(draw, preset.title, preset)

        self.assertTrue(
            any("do algorytmów" in line for line in lines),
            msg=f"Chroniona fraza została rozdzielona: {lines}",
        )
        
        self.assertTrue(all(line.strip() for line in lines))
        self.assertLessEqual(len(lines), 3)


class SeedCoverTests(TestCase):
    def test_seed_assigns_covers_only_to_every_third_book(self) -> None:
        with TemporaryDirectory() as media_root:
            with override_settings(MEDIA_ROOT=media_root):
                with patch(
                    "library.management.commands.seed_db._generate_cover",
                    return_value=ContentFile(b"demo-cover"),
                ) as generate_cover:
                    call_command("seed_db", verbosity=0)

        books = list(Book.objects.order_by("id"))
        books_with_cover = [book for book in books if book.cover]

        self.assertEqual(len(books), 12)
        self.assertEqual(len(books_with_cover), 4)
        self.assertEqual(generate_cover.call_count, 4)
        
        self.assertEqual(
            [bool(book.cover) for book in books],
            [index % 3 == 0 for index in range(12)],
        )
        
        self.assertEqual(
            [book.title for book in books_with_cover],
            [preset.title for preset in COVER_PRESETS[:4]],
        )
