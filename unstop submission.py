# Initializing the coach with 80 seats (7 seats per row, last row with 3 seats)
coach = [['O' for _ in range(7)] for _ in range(11)]
coach[-1] = ['O' for _ in range(3)]

def reserve_seats(num_seats):
    for row in range(len(coach)):
        if coach[row].count('O') >= num_seats:
            reserved_seats = []
            for seat in range(len(coach[row])):
                if coach[row][seat] == 'O' and len(reserved_seats) < num_seats:
                    coach[row][seat] = 'X'
                    reserved_seats.append((row, seat))
            return reserved_seats
    # If no single row can accommodate, find nearest available seats
    reserved_seats = []
    for row in range(len(coach)):
        for seat in range(len(coach[row])):
            if coach[row][seat] == 'O' and len(reserved_seats) < num_seats:
                coach[row][seat] = 'X'
                reserved_seats.append((row, seat))
            if len(reserved_seats) == num_seats:
                return reserved_seats
    return None

def display_seats():
    for row in coach:
        print(' '.join(row))
    print()

def main():
    while True:
        num_seats = int(input("Enter the number of seats to reserve: "))
        if num_seats > 7:
            print("You can reserve up to 7 seats at a time.")
            continue
        reserved_seats = reserve_seats(num_seats)
        if reserved_seats:
            print(f"Reserved seats: {reserved_seats}")
        else:
            print("Not enough seats available.")
            break
        display_seats()

if __name__ == "__main__":
    main()