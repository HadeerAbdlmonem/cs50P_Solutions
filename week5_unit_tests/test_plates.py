from plates import is_valid

def test_valid_plate():
    assert is_valid("CS50")
    assert is_valid("CS")
    assert is_valid("ECTO88")

def test_too_short():
    assert not is_valid("C")
    assert not is_valid("5")
    assert not is_valid("")

def test_starts_with_two_letters():
    assert not is_valid("50")
    assert not is_valid("C5")
    assert not is_valid("5C")

def test_length():
    assert not is_valid("CS50CS50")

def test_zero_first():
    assert not is_valid("CS05")

def test_letters_after_numbers():
    assert not is_valid("CS50P")
