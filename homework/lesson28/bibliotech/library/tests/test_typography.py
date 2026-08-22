from django.test import SimpleTestCase

from library.templatetags.polish_typography import polish_nbsp


class PolishTypographyTests(SimpleTestCase):
    def test_short_words_stay_with_the_following_word(self) -> None:
        text = "Dom bez powrotu i opowieść w starym mieście"

        result = polish_nbsp(text)

        self.assertIn("bez\u00a0powrotu", result)
        self.assertIn("i\u00a0opowieść", result)
        self.assertIn("w\u00a0starym", result)
