#tests/test_potencia.py camacho
from funciones.potenciacamacho import potencia
def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1