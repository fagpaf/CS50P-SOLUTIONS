from twttr import shorten


def test_lower_case():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"


def test_upper_case():
    assert shorten("HELLO") == "HLL"
    assert shorten("TWITTER") == "TWTTR"


def test_mixed():
    assert shorten("HelLo") == "HlL"
    assert shorten("twiTTEr") == "twTTr"


def test_numbers_symbols():
    assert shorten("1234!?") == "1234!?"
    assert shorten("h3ll0!") == "h3ll0!"

