"""Tests for plates.is_valid."""

from plates import is_valid


def test_valid_plate():
    assert is_valid("CS")


def test_too_short():
    assert not is_valid("50")


def test_letters_then_digit():
    assert not is_valid("C5")


def test_single_digit():
    assert not is_valid("5")
