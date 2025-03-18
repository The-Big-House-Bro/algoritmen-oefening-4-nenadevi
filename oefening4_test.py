import pytest
from oefening4 import countTargetPairs  # Vervang 'jouw_module' door de naam van het bestand waar de functie staat.

def test_countTargetPairs1():
    assert countTargetPairs([-1,1,2,3,1], 2) == 3

def test_countTargetPairs2():
    assert countTargetPairs([-6,2,5,-2,-7,-1,3], -2) == 10

def test_countTargetPairs3():
    assert countTargetPairs([0], 0) == 0
