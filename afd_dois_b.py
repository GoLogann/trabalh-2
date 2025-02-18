from automato.base_automato import Automato


estados_1b = {'q0', 'q1', 'q2', 'q3'}
alfabeto_1b = {'a', 'b'}
transicoes_1b = {
    ('q0', 'a'): 'q2',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q2',
    ('q1', 'b'): 'q1',
    ('q2', 'a'): 'q0',
    ('q2', 'b'): 'q3',
    ('q3', 'a'): 'q0',
    ('q3', 'b'): 'q3'
}
estado_inicial_1b = 'q0'
estados_finais_1b = {'q1'}

afd_1b = Automato(
    estados_1b,
    alfabeto_1b,
    transicoes_1b,
    estado_inicial_1b,
    estados_finais_1b
)

testes_1b = [
    ("b", True),
    ("babab", True),
    ("baab", True),
    ("aab", True),
    ("a", False),
    ("ab", False),
    ("bab", False),
    ("aba", False)
]