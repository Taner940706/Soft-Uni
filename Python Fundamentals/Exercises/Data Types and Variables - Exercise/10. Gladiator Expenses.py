loss=int(input())
helmet=float(input())
sword=float(input())
shield=float(input())
armor=float(input())
aureas=0
br=0
for i in range(1,loss+1):
    if i%2==0:
       aureas=aureas+helmet
    if i%3==0:
       aureas=aureas+sword
    if i%3==0 and i%2==0:
       aureas=aureas+shield
       br=br+1
for i in range(1,br+1):
    if i%2==0:
       aureas=aureas+armor
print(f"Gladiator expenses: {aureas:.2f} aureus")
