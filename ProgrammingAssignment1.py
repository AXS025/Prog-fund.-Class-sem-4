from enum import Enum #Import Enum

class Gender(Enum): #Defines a Gender enumeration using the Enum class
    MALE = 1 #Male is represented by 1
    FEMALE = 2 #Female is represented by 2

class Person: #The parent class
    def __init__(self, name, age, email, gender, nationality): #Constructor initializes the person with the attributes
        self.name = name
        self.age = age
        self.email = email
        self.gender = gender
        self.nationality = nationality

    # Setter and getter methods for the 5 attributes
    def set_name(self, name):  #setter
        self.name = name #getter

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_nationality(self, nationality):
        self.nationality = nationality

    def get_nationality(self):
        return self.nationality

class Passenger(Person): #The child class which inheterts attributes from the person class
    def __init__(self, name, age, email,  gender, nationality, passenger_id): #additional id attribute
        super().__init__(name, age, email, gender, nationality) #super function which calls attributes from the parent class within the child class
        self.passenger_id = passenger_id

    # Setter and getter
    def set_passenger_id(self, passenger_id):
        self.passenger_id = passenger_id

    def get_passenger_id(self):
        return self.passenger_id

    def __str__(self): #String representation of the passenger
        return f"Passenger Info:\nName: {self.name}\nAge: {self.age}\nEmail: {self.email}\nGender: {self.gender.name}\nNationality: {self.nationality}\nPassenger ID: {self.passenger_id}"

class Luggage: #luggage class
    def __init__(self, luggage_id, weight, color, size, luggage_type):
        self.luggage_id = luggage_id
        self.weight = weight
        self.color = color
        self.size = size
        self.luggage_type = luggage_type

    # Setters and getters
    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_luggage_type(self, luggage_type):
        self.luggage_type = luggage_type

    def get_luggage_type(self):
        return self.luggage_type

    def __str__(self): #String representation of the luggage
        return f"Luggage Info:\nLuggage ID: {self.luggage_id}\nWeight: {self.weight}\nColor: {self.color}\nSize: {self.size}\nType: {self.luggage_type}"

    def track_location(self): #Placeholder function to track luggage location
        pass #pass statement

class BoardingTicket: #Boarding ticket class
    def __init__(self, ticket_number, boarding_till, seat_number, level, gate, terminal):
        self.ticket_number = ticket_number
        self.boarding_till = boarding_till
        self.seat_number = seat_number
        self.level = level
        self.gate = gate
        self.terminal = terminal

    # Setter and getter
    def set_seat_number(self, seat_number):
        self.seat_number = seat_number

    def get_seat_number(self):
        return self.seat_number

    def set_gate(self, gate):
        self.gate = gate

    def get_gate(self):
        return self.gate

    def set_level(self, level):
        self.level = level

    def get_level(self):
        return self.level

    def __str__(self): #String representation of the ticket
        return f"Boarding Ticket Info:\nTicket Number: {self.ticket_number}\nBoarding Till: {self.boarding_till}\nSeat Number: {self.seat_number}\nLevel: {self.level}\nGate: {self.gate}\nTerminal: {self.terminal}"

    def check_boarding_status(self): #place holder function
        pass #pass statment

class Flight: #Flight class
    def __init__(self, flight_code, destination, origin, arrival_time, departure_time, date): #constructor
        self.flight_code = flight_code
        self.destination = destination
        self.origin = origin
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.date = date

    # setters and getters
    def set_destination(self, destination):
        self.destination = destination

    def get_destination(self):
        return self.destination

    def set_origin(self, origin):
        self.origin = origin

    def get_origin(self):
        return self.origin

    def __str__(self): #String representation of the flight
        return f"Flight Info:\nFlight Code: {self.flight_code}\nDestination: {self.destination}\nOrigin: {self.origin}\nArrival Time: {self.arrival_time}\nDeparture Time: {self.departure_time}\nDate: {self.date}"

# Example objects 1
passenger1 = Passenger("James Smith", 22, "james@example.com", Gender.MALE, "American", "123456")
luggage1 = Luggage("L001", 20, "Black", "Medium", "Suitcase")
boarding_ticket1 = BoardingTicket("629", "11:20", "09A", "First Class", "03", "02")
flight1 = Flight("NA4321", "NEW YORK JFK", "CHICAGO ORD", "13:30", "11:40", "06, DEC, 20")

# Example objects 2
passenger2 = Passenger("Afra AlSuwaidi", 19, "Afra@email.com", Gender.FEMALE, "Emirati", "98765")
luggage2 = Luggage("L002", 30, "Pink", "Large", "Suitcase")
boarding_ticket2 = BoardingTicket("T678", "12:35", "06C", "Business", "07", "09")
flight2 = Flight("ABC123", "THAILAND", "ABU DHABI", "4:30", "12:40", "13, OCT, 20")

# Prints for 1
print(passenger1)
print(luggage1)
print(boarding_ticket1)
print(flight1)

# Prints for 2
print(passenger2)
print(luggage2)
print(boarding_ticket2)
print(flight2)
