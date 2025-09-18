price = float(input('Insira o preço desejado: '))
print('Formas de Pagamento aceitas:\n Cheque, Cartão de Crédito (com até 2x sem juros e 3x com juros\n obs: cartão à vista tem desconto')
payment = str(input('Insira a forma de pagamento: '))

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
if payment.upper() in "CARTÃO DE CRÉDITO CARTAO CREDITO":
    choice = str(input('Deseja ser à vista, 2x ou 3x no cartão? '))
    if choice.upper() == 'VISTA':
        print(f'O preço final será de {price * 0.95}')
    elif choice.upper() == '2X':
        print(f'O valor total será de {price} com duas parcelas de {price / 2}')
    elif choice.upper() == '3X':
        print(f'O valor final será de {price * 1.20} com três parcelas de {(price *1.20) / 3}')
    else:
        print('Opção não valida! Por favor, tente novamente.')
#Ao invés de Python, deveria se chamar de "ELIFython"
