# Variáveis
print("====================================")
print("=== PARTE 1 - EXEMPLO FICTICIO ===")
print("====================================")
salario = 3000
taxa_imposto = 10

# Cálculo do imposto
valor_imposto = salario * taxa_imposto / 100

# Salário após desconto
salario_final = salario - valor_imposto

# Exibição dos resultados
print("Salário:", salario)
print("Taxa de imposto:", taxa_imposto, "%")
print("Valor do imposto:", valor_imposto)
print("Salário final:", salario_final)


# SITUAÇÃO REAL
print("====================================")
print("=== - PARTE 2 - SITUAÇÃO REAL - ===")
print("====================================")

salario = float(input("Digite o seu salário atual: "))
taxa_imposto = float(input("Digite a taxa de imposto (%): "))

# Calculo
valor_imposto = salario * taxa_imposto / 100

# Calculo do Salario Final
salario_final = salario - valor_imposto

# Exibição

print(f"\n====================================")
print("=== - RELATÓRIO FINAL - ===")
print(f"\n====================================")
print("Salário:", salario)
print("Taxa de imposto:", taxa_imposto, "%")
print("Valor do imposto:", valor_imposto)
print("Salário final:", salario_final)
