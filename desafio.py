CONSTANTE_BONUS = 1000


# Parte 1 - O programa deve começar solicitando ao usuário que insira seu nome.
nome_do_usuario = input("insira seu nome: ")

# Parte 2 - Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal
valor_salario = float(input("Insira seu salário: "))

# Parte 3 - Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
valor_bonus = float(input("Insira a porcentagem do bônus recebido: "))

# Parte 4 - O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
calculo_kpi_2024 = CONSTANTE_BONUS + (valor_salario * valor_bonus)

# Parte 5 - Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {nome_do_usuario}, o seu valor bônus foi de {calculo_kpi_2024}")

# Parte 6 - Salve esse script python como kpi.py
# Parte 7 - Faça uma documentação simples de como executar esse programa, utilize o README
# Parte 8 - Salve no Git e no Github