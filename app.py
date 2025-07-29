# Projeto: Sistema simples de padaria (Simple Bakery System)
# Revisado dia 29/07/2025

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
option = input("\nChefe, diz ai qual pão você deseja (digite o nome ou número)? ").strip().lower()

# Convertendo número para nome se necessário
bread_list = list(stock.keys())
if option.isdigit() and 1 <= int(option) <= len(bread_list):
    bread_type = bread_list[int(option) - 1]
elif option in bread_list:
    bread_type = option
else:
    print("Não tem esse pão ai não mano!.")
    exit()

# Verificar quantidade desejada
quantity = int(input(f"\nQuantos pães de {bread_type} você quer meu nobre? "))
if quantity > stock[bread_type]:
    print(f"Foi mal, só temos {stock[bread_type]} {bread_type}(s) no estoque.")
    exit()

# Preço do pão escolhido
bread = bread_price[bread_type]

# Seleção de método de pagamento
print("\nMétodos de pagamento:")
print("1- Pix")
print("2- Débito")
print("3- Crédito")
print("4- Dinheiro (à vista)")
print("5- Fiado")

payment_options = input("\nQual vai ser o método de pagamento chefe?: ").strip().lower()

# Convertendo número para texto
methods = ['pix', 'débito', 'crédito', 'dinheiro', 'fiado']
if payment_options.isdigit() and 1 <= int(payment_options) <= 5:
    payment = methods[int(payment_options) - 1]
elif payment_options in methods:
    payment = payment_options
else:
    print("Método inválido.")
    exit()

# Verificação de cartão e bandeira
if payment in ['crédito', 'débito']:
    flag = input("Qual a bandeira do cartão?: ").lower()
    accepted_flags = ['visa', 'mastercard', 'elo', 'ticket']
    if flag not in accepted_flags:
        print("Vish, acietamos essa bandeira ai não patrão!")
        exit()
    else:
        print("Cartão aceito! :)")

# Se for cartão, aplicar acréscimo
if payment in ['crédito', 'débito']:
    bread *= 1.05  # 5% de acréscimo

# Se for crédito, perguntar parcelas
if payment == 'crédito':
    installments = int(input("Quantas parcelas deseja? "))
    print(f"Compra em {installments}x de R${(quantity * bread)/installments:.2f}.")

# Valor total da compra
total = quantity * bread

# Se for fiado, adicionar à lista de devedores
if payment == 'fiado':
    name = input("Qual seu nome pro caderninho dos devedores?: ")
    debtors.append(name)
    print(f"\n{name}, sua dívida de R${total:.2f} foi registrada.")
    print("Volte sempre, seu caloteiro! (Pra pagar)")
    exit()

# Receber dinheiro se for necessário
if payment == 'dinheiro':
    money = float(input("\nDiga quanto você tem em R$: "))
    if money < total:
        print(f"Você não tem dinheiro suficiente, ta pobre hein? O total é R${total:.2f}")
        exit()
    change = money - total
else:
    change = 0.0

# Finalizando venda
stock[bread_type] -= quantity
print(f"\nO pão {bread_type} custa R${bread:.2f} cada.")
print(f"Total: R${total:.2f}")

if change > 0:
    print(f"Seu troco é R${change:.2f}")
elif change == 0:
    print("Pagamento exato, sem troco. Valeu!")
else:
    print("Erro de cálculo!")

print("\nCompra finalizada! Obrigado pela preferência!")

# Mostrar lista de devedores se houver
if len(debtors) > 0:
    print("\nLista de devedores atual:")
    for name in debtors:
        print(f"- {name}")
