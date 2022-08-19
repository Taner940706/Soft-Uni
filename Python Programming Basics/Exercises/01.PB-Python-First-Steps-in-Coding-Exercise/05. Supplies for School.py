count_pens = int(input())
count_markers = int(input())
litre_preparation = int(input())
discount = int(input())

pens = 5.80
markers = 7.20
preparation = 1.20

res = (count_pens*pens + count_markers*markers + litre_preparation*preparation)*((100-discount)/100)
print(res)

