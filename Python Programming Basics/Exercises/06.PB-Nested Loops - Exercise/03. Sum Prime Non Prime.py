command = input();
all_prime=0;
all_non_prime=0

while command != "stop":
    num = int(command);
    if num >= 0:
        if num == 2 or num==3 or num==5 or num==7:
             all_prime += num;
        elif num % 2 == 0 or num%3==0 or num%5==0 or num%7==0 and (num != 2 or num!=3 or num!=5 or num!=7):
            all_non_prime += num;
        else:
            all_prime += num;
    else:
        print("Number is negative.")
    command = input();

print(f"Sum of all prime numbers is: {all_prime}")
print(f"Sum of all non prime numbers is: {all_non_prime}")
        