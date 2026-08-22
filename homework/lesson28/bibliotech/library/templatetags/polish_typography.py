import re

from django import template


register = template.Library()

_NO_BREAK_AFTER = (
    "a",
    "i",
    "o",
    "u",
    "w",
    "z",
    "bez",
    "do",
    "dla",
    "ku",
    "na",
    "nad",
    "od",
    "po",
    "pod",
    "przy",
    "we",
    "za",
    "ze",
)

_PATTERN = re.compile(
    rf"(?<!\S)({'|'.join(map(re.escape, _NO_BREAK_AFTER))}) ",
    flags=re.IGNORECASE,
)


@register.filter
def polish_nbsp(value: str) -> str:
    """Łączy krótkie polskie wyrazy z następnym słowem twardą spacją."""
    return _PATTERN.sub(lambda match: f"{match.group(1)}\u00a0", str(value))