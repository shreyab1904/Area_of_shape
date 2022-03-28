import area

def test_area_rect():
    x=2
    y=3
    result=area.area_rect(x,y)
    assert x*y==result

def test_perimeter_rect():
    x=2
    y=3
    result=area.perimeter_rect(x,y)
    assert x+x+y+y==result

def test_area_square():
    x=2
    result=area.area_square(x)
    assert x*x==result