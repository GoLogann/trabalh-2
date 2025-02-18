from automato.base_automato import Automato

estados_1a = {'q0', 'q1', 'q2', 'q3'}
alfabeto_1a = {'0', '1'}
transicoes_1a = {
    ('q0', '0'): 'q0',
    ('q0', '1'): 'q1',
    ('q1', '0'): 'q2',
    ('q1', '1'): 'q3',
    ('q2', '0'): 'q0',
    ('q2', '1'): 'q3',
    ('q3', '0'): 'q3',
    ('q3', '1'): 'q3'
}
estado_inicial_1a = 'q0'
estados_finais_1a = {'q0'}

afd_1a = Automato(
    estados_1a,
    alfabeto_1a,
    transicoes_1a,
    estado_inicial_1a,
    estados_finais_1a
)

testes_1a = [
    ("0", True),
    ("0100", True),
    ("100", True),
    ("1", False),
    ("1001", False),
    ("010", False),
    ("0001", False)
]