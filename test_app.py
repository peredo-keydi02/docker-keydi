from app import mensaje

def test_mensaje():
    esperado = "¡Hola, mundo desde Docker!\nKeydi Peredo | IDSM41 | 18-05"
    assert mensaje() == esperado
