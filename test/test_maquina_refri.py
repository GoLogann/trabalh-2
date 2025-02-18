from maquina_refrigerante import maquina_refri

#Aceitacao
def test_validar_maquina_refri_1() -> None:
    cadeia = ("50", "25", "50", "100", "25", "50", "100")
    esperado = "0011011"
    resultado = maquina_refri.processar_cadeia(cadeia)
    print(f"\nSequence: {cadeia}\nExpected: {esperado}, Result: {resultado}")
    assert resultado == esperado

def test_validar_maquina_refri_2() -> None:
    cadeia = ("100", "50", "50", "50", "50")
    esperado = "10101"
    resultado = maquina_refri.processar_cadeia(cadeia)
    print(f"\nSequence: {cadeia}\nExpected: {esperado}, Result: {resultado}")
    assert resultado == esperado

def test_validar_maquina_refri_3() -> None:
    cadeia = ("100", "50", "50", "50", "50", "50", "50", "50", "50", "50")
    esperado = "1010101010"
    resultado = maquina_refri.processar_cadeia(cadeia)
    print(f"\nSequence: {cadeia}\nExpected: {esperado}, Result: {resultado}")
    assert resultado == esperado

def test_validar_maquina_refri_4() -> None:
    cadeia = ("25", "100", "25", "50")
    esperado = "0101"
    resultado = maquina_refri.processar_cadeia(cadeia)
    print(f"\nSequence: {cadeia}\nExpected: {esperado}, Result: {resultado}")
    assert resultado == esperado

#Rejeicao
def test_validar_maquina_refri_5() -> None:
    cadeia = ("100", "100", "50", "50")
    esperado = "1111"
    resultado = maquina_refri.processar_cadeia(cadeia)
    print(f"\nSequence: {cadeia}\nExpected: {esperado}, Result: {resultado}")
    assert resultado == esperado

def test_validar_maquina_refri_6() -> None:
    cadeia = ("25", "25", "25", "25")
    esperado = "0010"
    resultado = maquina_refri.processar_cadeia(cadeia)
    print(f"\nSequence: {cadeia}\nExpected: {esperado}, Result: {resultado}")
    assert resultado == esperado

def test_validar_maquina_refri_7() -> None:
    cadeia = ("25", "25", "50", "25")
    esperado = "0001"
    resultado = maquina_refri.processar_cadeia(cadeia)
    print(f"\nSequence: {cadeia}\nExpected: {esperado}, Result: {resultado}")
    assert resultado == esperado