menu = """
-----|Menu|------
|               |
| 1 - Sacar     |
| 2 - Depositar |
| 3 - Extrato   |
| 4 - Sair      |
    
"""

saldo = 0
extrato = ""
contador_saque = 1
numero_saque = 1
numero_deposito = 1

while True:
    opção = input(menu)
    
    if opção == '1':
        valor_saque = float(input('Digite o valor do saque: '))
        if contador_saque <= 3:
            
            if valor_saque <= saldo and valor_saque <= 500:
                saldo -= valor_saque
                print(f'Seu saldo atual é de R${saldo: .2f}')
                print(f'Você ainda possui {3 - contador_saque} saques.')
                contador_saque += 1
            else:
                if valor_saque > saldo: 
                    print(f'Seu saldo atual de R${saldo: .2f} é insuficiente para sacar a quantia desejada.')
                else:
                    print('O valor máximo de saque é de R$ 500.00')
        else:
            print('O limite de saques foi atingindo')

        extrato += f'Saque número {numero_saque} no valor de {valor_saque: .2f}| Saldo: {saldo: .2f} \n'
        numero_saque += 1
        
    elif opção == '2':
        valor_deposito = float(input('Digite o valor do deposito: '))
        
        saldo += valor_deposito
        print(f'Seu saldo atual é de R${saldo: .2f}')
        
        extrato += f'Deposito número {numero_deposito} no valor de{valor_deposito: .2f} | Saldo:{saldo: .2f} \n'  
        numero_deposito += 1
        
    elif opção == '3':
          print(extrato)
          
    elif opção == '4':
        break
    
    else:
        print('Informe uma opção válida!')