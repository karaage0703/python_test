#import pytest
from .. import base

def test_ok():
    assert base.add(1, 1) == 2

def test_ng():
    assert base.add(1, 1) == 3
