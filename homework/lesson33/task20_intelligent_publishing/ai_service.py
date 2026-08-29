import os

from dotenv import load_dotenv
from openai import AsyncOpenAI


load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")


async def summarize_post(title: str, content: str) -> str:
    response = await client.responses.create(
        model=MODEL,
        instructions=(
            "Streść podany post po polsku w maksymalnie 5-6 zdaniach. "
            "Napisz naturalne streszczenie z perspektywy osoby opisującej treść posta, "
            "a nie jako skróconą wersję wypowiedzi autora. "
            "Możesz używać sformułowań takich jak: 'Post przedstawia', "
            "'Autor wskazuje', 'Tekst zwraca uwagę' lub 'Głównym wnioskiem jest'. "
            "Wyciągnij najważniejsze informacje i wnioski, pomijając przykłady, "
            "powtórzenia oraz szczegóły drugorzędne. "
            "Nie dodawaj faktów, których nie ma w tekście."
        ),
        input=f"Tytuł: {title}\n\nTreść:\n{content}",
    )

    return response.output_text.strip()


async def analyze_sentiment(content: str) -> str:
    response = await client.responses.create(
        model=MODEL,
        instructions=(
            "Określ sentyment komentarza. "
            "Zwróć wyłącznie jedno słowo: positive, neutral albo negative. "
            "Oceniaj znaczenie całej wypowiedzi, także gdy emocja "
            "jest wyrażona pośrednio."
        ),
        input=content,
    )

    sentiment = response.output_text.strip().lower()

    if sentiment not in {"positive", "neutral", "negative"}:
        return "neutral"

    return sentiment


async def violates_ai_moderation(content: str) -> bool:
    response = await client.moderations.create(
        model="omni-moderation-latest",
        input=content,
    )

    return response.results[0].flagged


async def violates_content_policy(content: str, field: str) -> bool:
    response = await client.responses.create(
        model=MODEL,
        instructions=(
            "Oceń, czy tekst powinien zostać zablokowany na publicznym blogu. "
            "Zwróć wyłącznie ALLOW albo BLOCK. "
            "Blokuj poważne obelgi i nękanie, groźby, mowę nienawiści, "
            "nawoływanie do przemocy, szkodliwe treści seksualne, "
            "promowanie samookaleczeń, przestępczości, oszustw, "
            "doxxingu lub podobnych nadużyć. "
            "Nie blokuj zwykłej krytyki, negatywnej opinii, żartobliwych "
            "eufemizmów ani neutralnego omawiania trudnych tematów, "
            "takich jak polityka, religia, wojna czy przemoc. "
            "Oceniaj znaczenie, kontekst i cel całej wypowiedzi. "
            "Jeżeli oceniane pole to name, pamiętaj, że może zawierać "
            "prawdziwe imię i nazwisko, pseudonim albo nick. "
            "Jeżeli tekst ma formę imienia i nazwiska, zwróć ALLOW, "
            "nawet gdy nazwisko jest fikcyjne, żartobliwe albo zawiera "
            "fragment przypominający wulgarne lub obraźliwe słowo. "
            "Blokuj name tylko wtedy, gdy całość wyraźnie pełni funkcję "
            "obraźliwego lub szkodliwego nicku."
        ),
        input=f"Pole: {field}\nTekst: {content}",
    )

    return response.output_text.strip().upper() == "BLOCK"