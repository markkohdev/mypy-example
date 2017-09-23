from typing import Sequence, Optional, Tuple


def word_tokenize(text: str, language: str = 'english', preserve_line: bool = False) -> Sequence[
    str]: ...


def pos_tag(tokens: Sequence[str], tagset: Optional[str] = None, lang: str = 'eng') -> Sequence[
    Tuple[str, str]]: ...
