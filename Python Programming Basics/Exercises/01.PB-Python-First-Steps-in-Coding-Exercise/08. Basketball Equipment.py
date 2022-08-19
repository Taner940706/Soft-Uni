tax = int(input())

shoes = 0.6*tax
jersey = 0.8*shoes
ball = 0.25*jersey
accessory = 0.20*ball

bill = tax + jersey + ball + accessory + shoes
print(bill)
