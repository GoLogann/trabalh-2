from afd_um_a import afd_1a, testes_1a
from afd_dois_b import afd_1b, testes_1b
from automato.base_automato import MaquinaEstados
from maquina_refrigerante import maquina_refri
from match_palavra import transdutor_computador

def main():
    while True:
        print("\nMenu:")
        print("  1 - Executar AFD 1a")
        print("  2 - Executar AFD 1b")
        opcao = input("\nEscolha uma opção:")

        if opcao == "1":
            for teste in testes_1a:
                cadeia = teste[0]
                esperado = teste[1]

                resultado = MaquinaEstados(afd_1a).processar_cadeia(cadeia)
                print(f"Cadeia {cadeia}: Esperado: {esperado}, Resultado: {resultado}")

        if opcao == "2":
            for teste in testes_1b:
                cadeia = teste[0]
                esperado = teste[1]

                resultado = MaquinaEstados(afd_1b).processar_cadeia(cadeia)
                print(f"Cadeia {cadeia}: Esperado: {esperado}, Resultado: {resultado}")
        elif opcao == "3":
            break


if __name__ == "__main__":
    main()
