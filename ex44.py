price = float(input('Insira o preço desejado: '))
print('Formas de Pagamento aceitas:\n Cheque, Cartão de Crédito (com até 2x sem juros e 3x com juros)\n obs: cartão à vista tem desconto de 10%')
payment = str(input('Insira a forma de pagamento:'))
if payment.upper() in "CARTÃO DE CRÉDITO CARTAO DE CREDITO":
    choice = str(input('Deseja ser à vista, 2x ou 3x? '))
    if choice.upper() == 'VISTA':
        discount = price * 0.95
        print('O preço final será de {}'.format(discount))
    elif choice.upper() == '2X':
        print('O valor total será de {} com duas parcelas de {}'.format(price, price / 2))
