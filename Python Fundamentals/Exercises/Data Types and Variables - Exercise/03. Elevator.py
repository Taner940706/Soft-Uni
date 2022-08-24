n=int(input())
p=int(input())
counter=0

if n>p:
   if n%p==0:
      counter=n/p
      print(int(counter))
   elif n%p>0:
        counter=(int(n/p)+1)
        print(counter)
else:
    print("All the persons fit inside the elevator.")
    print("Only one course is needed.")
    