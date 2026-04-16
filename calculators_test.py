from calculators import add

def test_add():
#setup
    num = 10
    expected = 11
# invoke
    actual = add(num)

    assert expected == actual