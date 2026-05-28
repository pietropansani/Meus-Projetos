def sistema_recrutamento():

    qtdCadastrados = 0
    qtdSelecionados = 0
    somaIdades = 0

    print("--- SISTEMA RECRUTAMENTO ---")

    while True:
        print(f"\n--- CADASTRO DO CANDIDATO {qtdCadastrados + 1}---")

        # Coleta de dados do usuario
        numero = input("Numero de Inscricao: ")
        nome = input("Digite o Nome do Candidato: ")
        idade = int(input("Digite a idade do candidato: "))
        sexo = input("Sexo M/F: ").strip().upper()
        
        # perguntas de nivel sup / idiomas

        nivel_superior = input("Possui nível superior? (S/N): ").strip().upper()
        experiencia = input("Possui experiência no serviço? (S/N): ").strip().upper()
        ingles = input("Fala inglês? (S/N): ").strip().upper()
        espanhol = input("Fala espanhol? (S/N): ").strip().upper()

        # Atualiza as variáveis de contagem e soma
        qtdCadastrados += 1
        somaIdades += idade

        # Tomada de decisão: Avaliando os critérios com operadores lógicos (AND e OR)
        # Critérios: Superior (S) E Maior de 21 E Experiência (S) E (Inglês (S) OU Espanhol (S))
        criterio_superior = (nivel_superior == 'S')
        criterio_idade = (idade > 21)
        criterio_experiencia = (experiencia == 'S')
        criterio_idioma = (ingles == 'S' or espanhol == 'S')

        # Estrutura condicional para verificar aprovação
        if criterio_superior and criterio_idade and criterio_experiencia and criterio_idioma:
            print(f"\n>>> RESULTADO: O candidato {nome} FOI SELECIONADO! <<<")
            qtdSelecionados += 1
        else:
            print(f"\n>>> RESULTADO: O candidato {nome} NÃO FOI SELECIONADO. <<<")
            
        # Pergunta se o usuário deseja continuar o loop
        continuar = input("\nDeseja cadastrar outro candidato? (S/N): ").strip().upper()
        if continuar != 'S':
            break # Encerra o loop se a resposta não for 'S'

    # Cálculos finais
    print("\n===============================")
    print("      RELATÓRIO FINAL          ")
    print("===============================")
    print(f"Quantidade de pessoas cadastradas: {qtdCadastrados}")
    print(f"Quantidade de pessoas selecionadas: {qtdSelecionados}")
    
    if qtdCadastrados > 0:
        media_idade = somaIdades / qtdCadastrados
        print(f"Média geral de idade dos candidatos: {media_idade:.1f} anos")
    else:
        print("Nenhum candidato foi cadastrado.")

# Executa o programa
if __name__ == "__main__":
    sistema_recrutamento()


    