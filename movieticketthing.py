x = 10
Booked_seat = 0
prize_of_ticket = 0
Total_Income = 0
print()
print("~~~~~~~~~~~~~~~~WELCOME TO BOOKMYMOVIE.COM, OUR MOVIE TICKET BOOKING PLATFORM!~~~~~~~~~~~~~~~~")
print("**********************************************************************************************")
print("\n\n")
Row = int(input('Enter the number of rows - \n'))
Seats = int(input('Enter the number of seats in a row - \n'))
Total_seat = Row*Seats
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]

class chart:

    @staticmethod
    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j+1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

    @staticmethod
    def find_percentage():
        percentage = (Booked_seat/Total_seat)*100
        return percentage

class_call = chart
table_of_chart = class_call.chart_maker()

while x != 0:
    print()
    print('Press 1 - Display Seating Arrangement \nPress 2 - Purchase Ticket \nPress 3 - Display Statistics ',
          '\nPress 4 - Display Booked Tickets User Info \nPress 0 - Exit')
    print()
    x = int(input('Select Option - '))
    if x == 1:
        if Seats < 10:
            for seat in range(Seats):
                print(seat, end='  ')
            print(Seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, Seats):
                print(seat, end=' ')
            print(Seats)
        if Seats < 10:
            for num in table_of_chart.keys():
                print(int(num)+1, end='  ')
                for no in table_of_chart[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num]) < 9:
                    print(int(num)+1, end='  ')
                else:
                    print(int(num)+1, end=' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print()
        print("S - Seats available ")
        print("B - Seats booked ")
        print()
        print('Vacant Seats = ', Total_seat - Booked_seat)
        print()

    elif x == 2:
        Row_number = int(input('Enter the row number - \n'))
        Column_number = int(input('Enter the column number - \n'))
        if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
            if table_of_chart[str(Row_number-1)][str(Column_number)] == 'S':
                if Row*Seats <= 60:
                    prize_of_ticket = 10
                elif Row_number <= int(Row/2):
                    prize_of_ticket = 10
                else:
                    prize_of_ticket = 8
                print('prize_of_ticket - ', '$', prize_of_ticket)
                confirm = input('Type "yes" to confirm booking or "no" to stop booking - ')
                person_detail = {}
                if confirm == 'yes':
                    person_detail['Name'] = input('Enter Name - ')
                    person_detail['Gender'] = input('Enter Gender - ')
                    person_detail['Age'] = input('Enter Age - ')
                    person_detail['Phone_No'] = input('Enter Phone number - ')
                    person_detail['Ticket_prize'] = prize_of_ticket
                    table_of_chart[str(Row_number-1)][str(Column_number)] = 'B'
                    Booked_seat += 1
                    Total_Income += prize_of_ticket
                else:
                    continue
                Booked_ticket_Person[Row_number-1][Column_number-1] = person_detail
                print()
                print('Ticket Booked Successfully!')
            else:
                print()
                print('This seat is unavailable.')
        else:
            print()
            print('***  Invalid Input  ***')
        print()

    elif x == 3:
        print('Number of purchased Ticket - ', Booked_seat)
        print('Percentage - ', class_call.find_percentage())
        print('Current  Income - ', '$', prize_of_ticket)
        print('Total Income - ', '$', Total_Income)
        print()

    elif x == 4:
        Enter_row = int(input('Enter the row number - \n'))
        Enter_column = int(input('Enter the column number - \n'))
        if Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1):
            if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'B':
                person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                print('Name - ', person['Name'])
                print('Gender - ', person['Gender'])
                print('Age - ', person['Age'])
                print('Phone number - ', person['Phone_No'])
                print('Ticket Prize - ', '$', person['Ticket_prize'])
            else:
                print()
                print('---**---  Vacant seat  ---**---')
        else:
            print()
            print('***  Invalid Input  ***')
        print()

    else:
        print()
        print('***  Thank you for your time, see you again!  ***')
        print()
