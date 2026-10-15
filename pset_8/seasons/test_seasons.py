from seasons import is_valid, age_in_minutes
from datetime import date

import pytest


def test_is_valid_valid_date():
    assert is_valid(["2000", "1", "1"]) == [2000, 1, 1]


def test_is_valid_invalid_date():
    with pytest.raises(SystemExit):
        is_valid(["invalid", "1", "1"])


def test_age_in_minutes_today():
    today = date.today()
    result = age_in_minutes([today.year, today.month, today.day])
    assert result == 0  # diferença entre hoje e hoje = 0 minutos


def test_age_in_minutes_past_date():
    # Se ontem foi 1 dia atrás, diferença deve ser 1440 minutos
    today = date.today()
    yesterday = date(today.year, today.month, today.day - 1)
    result = age_in_minutes([yesterday.year, yesterday.month, yesterday.day])
    assert result == 1440
