from match_palavra import transdutor_computador

#Acception Tests
def test_validate_computer_transducer_1() -> None:
    sequence = """O computador é uma máquina capaz de variados tipos de tratamento automático de
                informações ou processamento de dados. Entende-se por computador um sistema físico
                que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e
                laptops são ícones da era da informação. O primeiro computador eletromecânico foi
                construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também
                chamado computador pessoal ou ainda computador doméstico."""
    expected = "2 149 342 492 520 "
    result = transdutor_computador.processar_cadeia(sequence)
    print(f"\nSequence: {sequence}\nExpected: {expected}, Result: {result}")
    assert result == expected

def test_validate_computer_transducer_2() -> None:
    sequence = "Na loja de eletrônicos, encontrei um computador incrível. Decidi comprar o computador para substituir o antigo."
    expected = "37 75 "
    result = transdutor_computador.processar_cadeia(sequence)
    print(f"\nSequence: {sequence}\nExpected: {expected}, Result: {result}")
    assert result == expected

def test_validate_computer_transducer_3() -> None:
    sequence = "Computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados."
    expected = "0 "
    result = transdutor_computador.processar_cadeia(sequence)
    print(f"\nSequence: {sequence}\nExpected: {expected}, Result: {result}")
    assert result == expected

def test_validate_computer_transducer_4() -> None:
    sequence = "O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados."
    expected = "2 "
    result = transdutor_computador.processar_cadeia(sequence)
    print(f"\nSequence: {sequence}\nExpected: {expected}, Result: {result}")
    assert result == expected

def test_validate_computer_transducer_5() -> None:
    sequence = "Eu trabalho com computador durante o dia, à noite gosto de jogar jogos no meu computador e nos fins de semana utilizo o computador para aprender novas habilidades."
    expected = "16 78 120 "
    result = transdutor_computador.processar_cadeia(sequence)
    print(f"\nSequence: {sequence}\nExpected: {expected}, Result: {result}")
    assert result == expected

# Rejection tests
def test_validate_computer_transducer_6() -> None:
    sequence = "Os computadores são ferramentas essenciais no mundo moderno, pois permitem a comunicação global, o acesso a informações instantâneas e a realização de tarefas complexas de maneira eficiente."
    expected = "3 "
    result = transdutor_computador.processar_cadeia(sequence)
    print(f"\nSequence: {sequence}\nExpected (should NOT match): {expected}, Result: {result}")
    assert result != expected

def test_validate_computer_transducer_7() -> None:
    sequence = "O microcomputador, também conhecido como PC, é uma forma popular de computador pessoal. "
    expected = "2 68 "
    result = transdutor_computador.processar_cadeia(sequence)
    print(f"\nSequence: {sequence}\nExpected (should NOT match): {expected}, Result: {result}")
    assert result != expected

def test_validate_computer_transducer_8() -> None:
    sequence = "A computadorização das empresas trouxe avanços significativos, automatizando processos, aumentando a eficiência e proporcionando um ambiente de trabalho mais produtivo."
    expected = "2 "
    result = transdutor_computador.processar_cadeia(sequence)
    print(f"\nSequence: {sequence}\nExpected (should NOT match): {expected}, Result: {result}")
    assert result != expected