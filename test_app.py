from app import mensaje

def test_mensaje_correcto():
    """
    Verifica que el mensaje retornado sea el esperado.
    Esta prueba valida la funcionalidad de la función mensaje()
    """
    esperado = "¡Hola, mundo desde Docker!\nKeydi Peredo | IDSM41 | 18-05"
    assert mensaje() == esperado
