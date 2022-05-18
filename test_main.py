from main import *

def test_cakes():
    assert cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) == 2

