from plates import is_valid


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("CS50") == True


def test_start_with_two_letters():
    assert is_valid("1A") == False
    assert is_valid("A1") == False
    assert is_valid("C5") == False
    assert is_valid("CS50") == True


def test_numbers_position():
    assert is_valid("CS50P") == False
    # Todos números só no final
    assert is_valid("CS50") == True
    # Sem números
    assert is_valid("CS") == True


def test_leading_zero():
    assert is_valid("CS05") == False
    assert is_valid("AB0") == False
    assert is_valid("CS50") == True


def test_only_alnum():
    assert is_valid("CS.50") == False
    assert is_valid("AB-12") == False
    assert is_valid("ROAD22") == True


def test_upper_lower_consistency():
    # Deve funcionar mesmo se for minúsculo
    assert is_valid("cs50") == True
    assert is_valid("ab") == True
