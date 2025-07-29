# Revisado em: 28/07/2025

# Estoque de pães (quantidade disponível de cada tipo)
stock = {
    'bolachão': 20,
    'frances': 30,
    'baiano': 25,
    'doce': 15
}

# Preços dos pães
bread_price = {
    'bolachão': 0.5,
    'frances': 0.33,
    'baiano': 0.5,
    'doce': 0.5
}

# Lista de devedores (para compras fiadas)
debtors = []

# Exibir cardápio
print("¨¨¨ CARDÁPIO DE PÃES ¨¨¨")
for idx, name in enumerate(stock.keys(), 1):
    print(f"{idx}- {name.capitalize()} (R${bread_price[name]:.2f})")

# Escolha do tipo de pão
option = input("\nQual pão você deseja (digite o nome ou número)? ").strip().lower()

# Convertendo número para nome se necessário
bread_list = list(stock.keys())
if option.isdigit() and 1 <= int(option) <= len(bread_list):
    tipo_pao = bread_list[int(option) - 1]
elif option in bread_list:
    tipo_pao = option
else:
    print("Pão inválido.")
    exit()

# Verificar quantidade desejada
quantidade = int(input(f"\nQuantos pães de {tipo_pao} você quer meu nobre? "))
if quantidade > stock[tipo_pao]:
    print(f"Desculpe, só temos {stock[tipo_pao]} {tipo_pao}(s) no estoque.")
    exit()

# Preço do pão escolhido
pao = bread_price[tipo_pao]

# Seleção de método de pagamento
print("\nMétodos de pagamento:")
print("1- Pix")
print("2- Débito")
print("3- Crédito")
print("4- Dinheiro (à vista)")
print("5- Fiado")

pagamento_opcao = input("\nQual vai ser o método de pagamento chefe?: ").strip().lower()

# Convertendo número para texto
metodos = ['pix', 'débito', 'crédito', 'dinheiro', 'fiado']
if pagamento_opcao.isdigit() and 1 <= int(pagamento_opcao) <= 5:
    pagamento = metodos[int(pagamento_opcao) - 1]
elif pagamento_opcao in metodos:
    pagamento = pagamento_opcao
else:
    print("Método inválido.")
    exit()

# Verificação de cartão e bandeira
if pagamento in ['crédito', 'débito']:
    bandeira = input("Qual a bandeira do cartão?: ").lower()
    bandeiras_aceitas = ['visa', 'mastercard', 'elo']
    if bandeira not in bandeiras_aceitas:
        print("Desculpe, não aceitamos essa bandeira.")
        exit()
    else:
        print("Cartão aceito! :)")

# Se for cartão, aplicar acréscimo
if pagamento in ['crédito', 'débito']:
    pao *= 1.05  # 5% de acréscimo

# Se for crédito, perguntar parcelas
if pagamento == 'crédito':
    parcelas = int(input("Quantas parcelas deseja? "))
    print(f"Compra em {parcelas}x de R${(quantidade * pao)/parcelas:.2f}.")

# Valor total da compra
total = quantidade * pao

# Se for fiado, adicionar à lista de devedores
if pagamento == 'fiado':
    nome = input("Qual seu nome pro caderninho dos devedores?: ")
    debtors.append(nome)
    print(f"\n{nome}, sua dívida de R${total:.2f} foi registrada.")
    print("Volte sempre, caloteiro! 😁")
    exit()

# Receber dinheiro se for necessário
if pagamento == 'dinheiro':
    dinheiro = float(input("\nDiga quanto você tem em R$: "))
    if dinheiro < total:
        print(f"Você não tem dinheiro suficiente. O total é R${total:.2f}")
        exit()
    troco = dinheiro - total
else:
    troco = 0.0

# Finalizando venda
stock[tipo_pao] -= quantidade
print(f"\nO pão {tipo_pao} custa R${pao:.2f} cada.")
print(f"Total: R${total:.2f}")

if troco > 0:
    print(f"Seu troco é R${troco:.2f}")
elif troco == 0:
    print("Pagamento exato, sem troco. Valeu!")
else:
    print("Erro de cálculo!")

print("\nCompra finalizada! Obrigado pela preferência!")

# Mostrar lista de devedores se houver
if len(debtors) > 0:
    print("\nLista de devedores atual:")
    for nome in debtors:
        print(f"- {nome}")
