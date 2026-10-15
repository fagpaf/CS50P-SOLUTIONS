from CS50_P.problem_set_7.um.um import count

def test_single_and_multiple():
    assert count("um") == 1
    assert count("um, um, um") == 3
    assert count("um?") == 1
    assert count("hello, um, world") == 1

def test_inside_words():
    # Não deve contar se "um" for parte de outra palavra
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("Um, thanks for the album.") == 1

def test_case_insensitivity():
    # Deve contar independentemente de ser maiúscula ou minúscula
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM") == 1
