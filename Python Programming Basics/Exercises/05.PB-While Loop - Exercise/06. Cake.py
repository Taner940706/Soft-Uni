a = int(input())
b = int(input())
parche = input()
torta = a*b

while parche != "STOP":
    parche = int(parche)
    if (torta-parche) < 0:
        torta = torta-parche
        print(f'No more cake left! You need {abs(torta)} pieces more.')
        break
    torta = torta-parche
    parche = input()
if torta > 0:
    print(f'{torta} pieces are left.')
