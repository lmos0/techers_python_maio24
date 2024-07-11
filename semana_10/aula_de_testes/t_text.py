import pytest
from text import reverse_string, to_uppercase, to_lowercase

def test_to_uppercase():
    assert to_uppercase('hello') == 'HELLO'
    assert to_uppercase('') == ''
    assert to_uppercase('Hello World') == 'HELLO WORLD'


def test_to_lowercase():
    assert to_lowercase('HEllO') == 'hello'
    assert to_lowercase('') == ''
    assert to_lowercase('hello') == 'hello'

def test_reverse_string():
    assert reverse_string('hello') == 'olleh'
    assert reverse_string('world') == 'dlrow'
    assert reverse_string('') == ''
    assert reverse_string('A') == 'a'