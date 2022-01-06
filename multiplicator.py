from time import sleep

try:
    num = int(input('Digite um número para calcularmos a sua tabuáda: '))

except ValueError:
    sleep(1)
    print('O Valor digitado é inválido!')
    exit()

sleep(1)
print('Carregando...')
sleep(2)

try:
    choice = int(input(f'''
__________________________________________________________

Caso você queira multiplicar o número  "{num}" de 1 a 10, digite 1,
caso queira multiplicar esse número em um valor maior do que 10, digite 2: '''))

except ValueError:
    sleep(1)
    print('O Valor digitado é inválido!')
    exit()

if choice == 1:
    x01 = num * 1
    x02 = num * 2
    x03 = num * 3
    x04 = num * 4
    x05 = num * 5
    x06 = num * 6
    x07 = num * 7
    x08 = num * 8
    x09 = num * 9
    x10 = num * 10

    print(f''' Toda a tabuáda de {num} é: 
    {num} x 01 = {x01}
    {num} x 02 = {x02}
    {num} x 03 = {x03}
    {num} x 04 = {x04}
    {num} x 05 = {x05}
    {num} x 06 = {x06}
    {num} x 07 = {x07}
    {num} x 08 = {x08}
    {num} x 09 = {x09}
    {num} x 10 = {x10}
    ''')

elif choice == 2:
    try:
        calculate = int(input(f'Digite o número no qual você quer multiplicar {num}: '))

    except:
        sleep(1)
        print('O Valor digitado é inválido!')
        exit()

    multiplication = num * calculate
    print(f'O resultado de {num} x {calculate} é: {multiplication}')
    
else:
    sleep(1)
    print('o valor que foi digitado está incorreto ou é inválido')

