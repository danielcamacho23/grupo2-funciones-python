from funciones.multiplicargallardo import multiplicargallardo

def test_multiplicargallardo():
    assert multiplicargallardo(3, 4) == 12
    assert multiplicargallardo(-2, 5) == -10
    assert multiplicargallardo(0, 7) == 0
