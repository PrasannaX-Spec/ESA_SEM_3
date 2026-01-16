from large_small import largest_smallest

def test_for_positive():
    assert largest_smallest(10,5,2) == (10,2)

def test_for_negative():
    assert largest_smallest(-10,-5,-2) == (-2,-10)

def test_for_zero():
    assert largest_smallest(0,5,3) == (5,0)