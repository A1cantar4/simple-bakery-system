# Project: Simple Bakery System
# Reviewed on 07/29/2025

# Bread stock (available quantity of each type)
stock = {
    'bolachão': 20,
    'frances': 30,
    'baiano': 25,
    'doce': 15
}

# Bread prices
bread_price = {
    'bolachão': 0.5,
    'frances': 0.33,
    'baiano': 0.5,
    'doce': 0.5
}

# Debtors list (for purchases on credit)
debtors = []

# Display menu
print("¨¨¨ CARDÁPIO DE PÃES ¨¨¨")
for idx, name in enumerate(stock.keys(), 1):
    print(f"{idx}- {name.capitalize()} (R${bread_price[name]:.2f})")

# Bread type selection
option = input("\nChefe, diz ai qual pão você deseja (digite o nome ou número)? ").strip().lower()

# Convert number to name if needed
bread_list = list(stock.keys())
if option.isdigit() and 1 <= int(option) <= len(bread_list):
    bread_type = bread_list[int(option) - 1]
elif option in bread_list:
    bread_type = option
else:
    print("Não tem esse pão ai não mano!.")
    exit()

# Check desired quantity
quantity = int(input(f"\nQuantos pães de {bread_type} você quer meu nobre? "))
if quantity > stock[bread_type]:
    print(f"Foi mal, só temos {stock[bread_type]} {bread_type}(s) no estoque.")
    exit()

# Price of chosen bread
bread = bread_price[bread_type]

# Payment method selection
print("\nMétodos de pagamento:")
print("1- Pix")
print("2- Débito")
print("3- Crédito")
print("4- Dinheiro (à vista)")
print("5- Fiado")

payment_options = input("\nQual vai ser o método de pagamento chefe?: ").strip().lower()

# Convert number to text
methods = ['pix', 'débito', 'crédito', 'dinheiro', 'fiado']
if payment_options.isdigit() and 1 <= int(payment_options) <= 5:
    payment = methods[int(payment_options) - 1]
elif payment_options in methods:
    payment = payment_options
else:
    print("Método inválido.")
    exit()

# If it's a card, apply fee
if payment in ['crédito', 'débito']:
    flag = input("Qual a bandeira do cartão?: ").lower()
    accepted_flags = ['visa', 'mastercard', 'elo', 'ticket']
    if flag not in accepted_flags:
        print("Vish, acietamos essa bandeira ai não patrão!")
        exit()
    else:
        print("Cartão aceito! :)")

# If it's a card, apply fee
if payment in ['crédito', 'débito']:
    bread *= 1.05  # 5% de acréscimo

# If credit, ask for installments
if payment == 'crédito':
    installments = int(input("Quantas parcelas deseja? "))
    print(f"Compra em {installments}x de R${(quantity * bread)/installments:.2f}.")

# Total purchase amount
total = quantity * bread

# If on credit, add to debtors list
if payment == 'fiado':
    name = input("Qual seu nome pro caderninho dos devedores?: ")
    debtors.append(name)
    print(f"\n{name}, sua dívida de R${total:.2f} foi registrada.")
    print("Volte sempre, seu caloteiro! (Pra pagar)")
    exit()

# Receive money if necessary
if payment == 'dinheiro':
    money = float(input("\nDiga quanto você tem em R$: "))
    if money < total:
        print(f"Você não tem dinheiro suficiente, ta pobre hein? O total é R${total:.2f}")
        exit()
    change = money - total
else:
    change = 0.0

# Finalizing sale
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

# Show debtors list if any
if len(debtors) > 0:
    print("\nLista de devedores atual:")
    for name in debtors:
        print(f"- {name}")