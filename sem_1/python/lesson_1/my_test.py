from my import add
import pytest


def test_processing():
    data = add(1, 1)
    assert data == 2
