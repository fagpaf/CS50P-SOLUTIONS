from CS50_P.problem_set_7.numb3rs.numb3rs import validate

def test_format():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False

def test_range():
    assert validate("255.255.255.255") == True
    assert validate("512.1.1.1") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.512.1") == False
    assert validate("1.1.1.512") == False

def test_invalid_types():
    assert validate("cat") == False
    assert validate("255.255.255.cat") == False
