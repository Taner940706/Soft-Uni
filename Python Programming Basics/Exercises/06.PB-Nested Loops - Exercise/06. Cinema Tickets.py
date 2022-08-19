movie = input()
total_tickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0

while movie != 'Finish':
    free_seats = int(input())
    busy_seats = 0

    for i in range(free_seats):
        ticket = input()

        if ticket == 'kid':
            kid_tickets += 1
        elif ticket == 'student':
            student_tickets += 1
        elif ticket == 'standard':
            standard_tickets += 1
        elif ticket == 'End':
            break
        total_tickets += 1
        busy_seats += 1

    percent_room = (busy_seats / free_seats) * 100
    total_tickets = standard_tickets + student_tickets + kid_tickets
    print(f'{movie} - {percent_room:.2f}% full.')

    movie = input()


print(f'Total tickets: {total_tickets}')
print(f'{(student_tickets / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.')
