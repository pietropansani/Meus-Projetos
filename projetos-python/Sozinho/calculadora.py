def calculadora():
    print("Vamos Calcular?")

    while True:
        # Usando float() em vez de int() para permitir números decimais
        try:
            n1 = float(input("\nDigite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, digite apenas números válidos!")
            continue

        operacao = input("Digite a operação (+, -, *, /): ").strip()
        res = None  # Inicializa a variável para evitar erros

        match operacao:
            case "+":
                res = n1 + n2
            case "-":
                res = n1 - n2
            case "*":
                res = n1 * n2
            case "/":
                if n2 == 0:
                    print("Erro: Não é possível dividir por zero!")
                else:
                    res = n1 / n2
            case _:  # Caso o usuário digite uma operação que não existe
                print("Operação inválida!")

        # Só imprime o resultado se a operação foi bem-sucedida
        if res is not None:
            print(f"Resultado é igual a: {res}")

        # Lógica de continuar corrigida
        continuar = input("\nDeseja fazer outro calculo (S/N): ").strip().upper()
        if continuar != "S":
            print("Vamos Fazer outro calculo entao!")
        else:
            print("Encerrando a calculadora. Até mais!")
            break


# Executa o programa
if __name__ == "__main__":
    calculadora()
