suma=0
while suma<10000:
      step=input()
      if step=="Going home":
         step=int(input())
         suma=suma+step
         if suma<10000:
            print(f'{10000-suma} more steps to reach goal.')
         break
      step=int(step)
      suma=suma+step
if suma>=10000:
   print("Goal reached! Good job!")
   print(f'{suma-10000} steps over the goal!')