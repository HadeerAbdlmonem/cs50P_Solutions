"""Tests for bank_.greeting."""

from bank_ import greeting


def test_hello_greeting():
    assert greeting("hello") == "$0"


def test_h_greeting():
    assert greeting("h") == "$20"


def test_other_greeting():
    assert greeting("k") == "$100"
