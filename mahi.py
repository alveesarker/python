# Booked_list = [["Seat no.", "Passenger name", "Ticket no."],
#               ["A1", "      Bushra", "        01"],
#               ["B1", "      Imtiaz", "        02"],
#               ["C1", "      Akhi", "          03"],
#               ["D1", "      Youshra", "       04"],
#               ["A2", "      Fatin", "         05"],
#               ["B2", "      Tahia", "         06"],
#               ["A3", "      Sanjeeda", "      07"],
#               ["B3", "      Seefat", "        08"],
#               ["C3", "      Mehedi", "        09"],
#               ["D3", "      Shihab", "        10"]]
#
# for i in range(len(Booked_list)):
#     for j in range(len(Booked_list[i])):
#         print(Booked_list[i][j], end='  ')
#     print()
#
# Seat_status = [["Seat no.", "Status"],
#                ["A1", "      reclining"],
#                ["B1", "      reclining"],
#                ["C1", "      reclining"],
#                ["D1", "      reclining"],
#                ["A2", "      reclining"],
#                ["B2", "      reclining"],
#                ["C2", "      reclining"],
#                ["D2", "      reclining"],
#                ["A3", "      reclining"],
#                ["B3", "      reclining"],
#                ["C3", "      reclining"],
#                ["D3", "      reclining"],
#                ["A4", "      reclining"],
#                ["B4", "      reclining"],
#                ["C4", "      reclining"],
#                ["D4", "      reclining"]]
# print()
# for i in range(len(Seat_status)):
#     for j in range(len(Seat_status[i])):
#         print(Seat_status[i][j], end='  ')
#     print()
#
# available_seats = ["available seats.","A4","B4","C2","D2","C4","D4"]
# for i in available_seats:
#     print(i)
#
# status ={
#     "A1": "reclining",
#     "B1": "reclining",
#     "C1": "reclining",
#     "D1": "reclining",
#     "A2": "reclining",
#     "B2": "reclining",
#     "C2": "reclining",
#     "D2": "reclining",
#     "A3": "reclining",
#     "B3": "reclining",
#     "C3": "reclining",
#     "D3": "reclining",
#     "A4": "reclining",
#     "B4": "reclining",
#     "C4": "reclining",
#     "D4": "reclining",
# }
# number = input('Enter the seat number:')
# print(status[number])

# seat_number = ['A1', 'A2', 'A3', 'A4', 'A1', 'A2', 'A3', 'A4', 'A1', 'A2', 'A3', 'A4', 'A1', 'A2', 'A3', 'A4']
# t_s_number = int(input('Enter ticket serial number: '))
# Name = input('Your Name: ')
# print('Ticket serial number:', t_s_number)
# print('Name:',Name)
# print('Seat Number:',seat_number[t_s_number-1])


# def status(a):
#     Seat_status = [["Seat no.", "Status"],
#                    ["A1", "      reclining"],
#                    ["B1", "      reclining"],
#                    ["C1", "      reclining"],
#                    ["D1", "      reclining"],
#                    ["A2", "      reclining"],
#                    ["B2", "      reclining"],
#                    ["C2", "      reclining"],
#                    ["D2", "      reclining"],
#                    ["A3", "      reclining"],
#                    ["B3", "      reclining"],
#                    ["C3", "      reclining"],
#                    ["D3", "      reclining"],
#                    ["A4", "      reclining"],
#                    ["B4", "      reclining"],
#                    ["C4", "      reclining"],
#                    ["D4", "      reclining"]]
#     print()
#     for i in range(len(Seat_status)):
#         for j in range(len(Seat_status[i])):
#             print(Seat_status[i][j], end='  ')
#         print()
#
# print('Menu:')
# menu = ['1. Show status of all seats', '2. Show available seats', '3. Show status of a specific seat', '4. Book a seat', '5. Cancel booking of a seat']
# for i in menu:
#     print(i)
#
# status(c)
# a = int(input('Choose your option: '))
#
# status()

# class Bus:
#     def __init__(self):
#         self.seats = [False] * 16  # Initialize all seats as not booked
#
#     def show_all_seats(self):
#         print("Status of all 16 seats on the bus:")
#         for i, seat_status in enumerate(self.seats, start=1):
#             print(f"Seat {i}: {'Booked' if seat_status else 'Available'}")
#
#     def show_available_seats(self):
#         print("Available seats on the bus:")
#         seat_number = ['A1', 'A2', 'A3', 'A4', 'A1', 'A2', 'A3', 'A4', 'A1', 'A2', 'A3', 'A4', 'A1', 'A2', 'A3', 'A4']
#         for i, seat_status in enumerate(self.seats, start=0):
#             if not seat_status:
#                 print(f"Seat {seat_number[i]}")
#
#     def show_seat_status(self, seat_number):
#
#         if 1 <= seat_number <= 16:
#             status = 'Booked' if self.seats[seat_number - 1] else 'Available'
#             print(f"Seat {seat_number}: {status}")
#         else:
#             print("Invalid seat number. Please enter a seat number between 1 and 16.")
#
#     def book_seat(self, seat_number, name):
#         number = ['A1', 'A2', 'A3', 'A4', 'A1', 'A2', 'A3', 'A4', 'A1', 'A2', 'A3', 'A4', 'A1', 'A2', 'A3', 'A4']
#         if 1 <= seat_number <= 16:
#             if not self.seats[seat_number - 1]:
#                 self.seats[seat_number - 1] = True
#                 print('Serial Number:',seat_number)
#                 print(f'Name: {name}')
#                 print(f"Seat {number[seat_number-1]} booked successfully.")
#             else:
#                 print(f"Seat {seat_number} is already booked.")
#         else:
#             print("Invalid seat number. Please enter a seat number between 1 and 16.")
#
#     def cancel_booking(self, seat_number):
#         if 1 <= seat_number <= 16:
#             if self.seats[seat_number - 1]:
#                 self.seats[seat_number - 1] = False
#                 print(f"Booking canceled for Seat {seat_number}.")
#             else:
#                 print(f"Seat {seat_number} is not booked.")
#         else:
#             print("Invalid seat number. Please enter a seat number between 1 and 16.")

# Main program
# bus = Bus()
#
# while True:
#     print("\nMenu:")
#     print("1. Show status of all seats")
#     print("2. Show available seats")
#     print("3. Show status of a specific seat")
#     print("4. Book a seat")
#     print("5. Cancel booking of a seat")
#     print("6. Exit")
#
#     choice = input("Enter your choice (1-6): ")
#
#     if choice == '1':
#         bus.show_all_seats()
#     elif choice == '2':
#         bus.show_available_seats()
#     elif choice == '3':
#         seat_number = int(input("Enter seat number: "))
#         bus.show_seat_status(seat_number)
#     elif choice == '4':
#         seat_number = int(input("Enter ticket serial number: "))
#         name = input('Your Name: ')
#         bus.book_seat(seat_number, name)
#     elif choice == '5':
#         seat_number = int(input("Enter seat number to cancel booking: "))
#         bus.cancel_booking(seat_number)
#     elif choice == '6':
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 6.")



# i= 0
# while i < 5:
#     print(i)
#     i += 1
# print(i)

# for i in range(5):
#     print(i)
# print(i)

def my_func(a, *b, c = 0):
    print(a, b, c)
my_func(2, 4, 5,6, c= 4)
