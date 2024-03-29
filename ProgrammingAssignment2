from enum import Enum #Imports enum

class TicketType(Enum): #enumeration for types of tickets
    EXHIBITION = 1
    TOUR = 2

class Location(Enum): #enum for the locations
    PERMANENT_GALLERY = 1
    EXHIBITION_HALL = 2
    OUTDOOR_SPACE = 3

class VisitorType(Enum): #the visitor types (to identfy who get a discount or free tickets)
    GROUP = 1
    STUDENT = 2
    TEACHER = 3

class Person: #person class (parent)
    def __init__(self, name, age): #constructor initializing the Person with its attributes
        self.name = name #name attribute
        self.age = age #age attribute

    def set_name(self, name): #setter
        self.name = name

    def get_name(self): #getter
        return self.name

    def set_age(self, age): #setter
        self.age = age

    def get_age(self): #getter
        return self.age

class Visitor(Person): #Visitor class which inherits for the parent class Person
    def __init__(self, name, age, visitor_type): #constructor
        super().__init__(name, age) #super function that calls attributes from the parent class
        self.visitor_type = visitor_type #visitor type attribute

    def set_visitor_type(self, visitor_type): #setter
        self.visitor_type = visitor_type

    def get_visitor_type(self): #getter
        return self.visitor_type

class Ticket: #Ticket class
    def __init__(self, visitor, visitor_type):
        self.visitor = visitor
        self.ticket_type = self.get_ticket_type(visitor_type)
        self.price = self.calculate_ticket_price()

    def get_ticket_type(self, visitor_type): #method to determine ticket type based on visitor type
        if visitor_type != VisitorType.GROUP: #If function for if the visitor is not a group
            return TicketType.EXHIBITION #then return exhibition ticket type
        elif visitor_type == VisitorType.GROUP: #if the visitor is in a group then they get a tour ticket
            return TicketType.TOUR
        else: #else function, it would retun none
            return None

    def calculate_ticket_price(self): #To calculate the ticket price
        age = self.visitor.age #gets the visitors age
        visitor_type = self.visitor.visitor_type #get the visitors type

        if age <= 18 or age >= 60 or visitor_type in [VisitorType.STUDENT, VisitorType.TEACHER]: #if the visitor is under 18 or over 60, or a student/teacher
            ticket_price = 0  #The ticket is free
        elif 18 <= age <= 60 and visitor_type != VisitorType.GROUP: #if the visitor is between 18 and 60 and not in a group
            ticket_price = 63 #then their ticket is 63
        elif visitor_type == VisitorType.GROUP: #If they are in a group
            ticket_price = 63 * 0.5 #then their ticket is 50 precent off
        else:
            ticket_price = None

        if ticket_price is not None:
            ticket_price *= 1.05 #with the VAT tax

        return ticket_price #returns the calculated price

class Museum: #Museum class
    def __init__(self, museum_Name, rooms):#Constructor
        self.museum_Name = museum_Name
        self.rooms = [] #composition: Museum "owns" Room objects

    def set_museum_Name(self, museum_Name): #setter
        self.museum_Name = museum_Name

    def get_museum_Name(self): #getter
        return self.museum_Name

    def set_rooms(self, rooms): #setter
        self.rooms = rooms

    def get_rooms(self): #getter
        return self.rooms

class Room: #Room class
    def __init__(self, number, capacity):
        self.number = number #attribute
        self.capacity = capacity

    def set_number(self, number): #setter
        self.number = number

    def get_number(self): #getter
        return self.number

    def set_capacity(self, capacity): #setter
        self.capacity = capacity

    def get_capacity(self): #getter
        return self.capacity

class Exhibition: #Exhibition class
    def __init__(self, title, location): #Constructor
        self.title = title
        self.location = location
        self.artworks = [] #initializing an empty list to store artworks

    def set_location(self, location): #setter
        self.location = location

    def get_location(self): #getter
        return self.location

    def add_artwork(self, artwork): #adds artwork to the exhibition's collection
        self.artworks.append(artwork) #appends the artwork to the list of artworks with this Exhibition

class Artwork: #Artwork class
    def __init__(self, title, artist, date_of_creation, significance, location): #Constructor
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.significance = significance
        self.location = location

    def set_title(self, title): #setter
        self.title = title

    def get_title(self): #getter
        return self.title

    def set_artist(self, artist): #setter
        self.artist = artist

    def get_artist(self): #getter
        return self.artist

#Creates Visitors
visitor1 = Visitor("Afra", 19, None)
visitor2 = Visitor("Khalifa", 16, None)
visitor3 = Visitor("Mozzah", 25, VisitorType.STUDENT)
visitor4 = Visitor("Mohammed", 40, VisitorType.GROUP)

#Creates Tickets
ticket1 = Ticket(visitor1, visitor1.visitor_type)
ticket2 = Ticket(visitor2, visitor2.visitor_type)
ticket3 = Ticket(visitor3, visitor3.visitor_type)
ticket4 = Ticket(visitor4, visitor4.visitor_type)

#Displays ticket prices for visitors with their age
print(f"{visitor1.name} (Age {visitor1.age}): Ticket Price: {ticket1.price:.2f} AED")
print(f"{visitor2.name} (Age {visitor2.age}): Ticket Price: {ticket2.price:.2f} AED")
print(f"{visitor3.name} (Age {visitor3.age}): Ticket Price: {ticket3.price:.2f} AED")
print(f"{visitor4.name} (Age {visitor4.age}): Ticket Price: {ticket4.price:.2f} AED")


#Creates the Museum and Rooms
museum = Museum("The Louvre Museum", [Room(1, 100), Room(2, 300), Room(3, 200)])

#Displays museum name and rooms
print(f"Museum Name: {museum.get_museum_Name()}")
print("Rooms:")
for room in museum.get_rooms():
    print(f"Room {room.get_number()}: Capacity - {room.get_capacity()}")

#Creates an Exhibition
exhibition1 = Exhibition("Famous Art", Location.EXHIBITION_HALL)

#Adds Artworks to the Exhibition
artwork1 = Artwork("The Starry Night", "Vincent van Gogh", "1889", "Impressionism", exhibition1.get_location())
artwork2 = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Renaissance", exhibition1.get_location())

exhibition1.add_artwork(artwork1)
exhibition1.add_artwork(artwork2)

#Displays Exhibition Details
print(f"\nExhibition Title: {exhibition1.title}")
print(f"Location: {exhibition1.get_location().name}")
print("Artworks in the Exhibition:")
for artwork in exhibition1.artworks:
    print(f"- {artwork.get_title()} by {artwork.get_artist()}, {artwork.date_of_creation}, {artwork.significance}")


exhibition2 = Exhibition("Ancient Art Exhibition", Location.PERMANENT_GALLERY)

artwork3 = Artwork("Ivan the Terrible and his son", "Ilya Repin", "1883 - 1885", "History realism", exhibition2.get_location())
artwork4 = Artwork("Winged Victory of Samothrace", "Unknown", "200 - 190", "Greek sculpture", exhibition2.get_location())

exhibition2.add_artwork(artwork3)
exhibition2.add_artwork(artwork4)

#Prints the Exhibition Details for the second Exhibition
print(f"\nExhibition Title: {exhibition2.title}")
print(f"Location: {exhibition2.get_location().name}")
print("Artworks in the Exhibition:")
for artwork in exhibition2.artworks:
    print(f"- {artwork.get_title()} by {artwork.get_artist()}, {artwork.date_of_creation}, {artwork.significance}")


#Creates visitors with different types
visitor5 = Visitor("Ahmed", 32, VisitorType.STUDENT)
visitor6 = Visitor("Mera", 22, VisitorType.TEACHER)
visitor7 = Visitor("Thuraia", 25, VisitorType.GROUP)

#Creates tickets for each visitor
ticket5 = Ticket(visitor5, visitor5.visitor_type)
ticket6 = Ticket(visitor6, visitor6.visitor_type)
ticket7 = Ticket(visitor7, visitor7.visitor_type)

#Shows the people with their ticket type
print(f"{visitor5.name}'s Ticket Type: {ticket5.ticket_type.name}")
print(f"{visitor6.name}'s Ticket Type: {ticket6.ticket_type.name}")
print(f"{visitor7.name}'s Ticket Type: {ticket7.ticket_type.name}")
