from main import *

def test_cakes_1():
    assert cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) == 2

def test_cakes_2():
    assert cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}) == 0

def test_cakes_3():
    assert cakes({'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}) == 11

def test_cakes_4():
    assert cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000, 'apples': 15, 'oil': 20}) == 0

