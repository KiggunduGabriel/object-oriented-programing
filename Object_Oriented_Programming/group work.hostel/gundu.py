class Visitor:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

class Resident:
    def __init__(self, name, room):
        self.name = name
        self.room = room

class Hostel:
    def __init__(self, name):
        self.name = name
        self.visits = []  # to store visits

    def record_visit(self, visitor, resident):
        self.visits.append((visitor, resident))

    def show_visits(self):
        print(f"Visits recorded at {self.name}:")
        for v, r in self.visits:
            # Handle info safely for either Visitors or Residents
            visitor_info = getattr(v, "ID", "No ID")
            resident_info = getattr(r, "room", "No room")
            print(f"{v.name} (ID: {visitor_info}) visited {r.name} in room {resident_info}")


# Create two visitors and two residents
visitor1 = Visitor("Alice", "V001")   
visitor2 = Visitor("Mary", "V002")    
resident1 = Resident("Akram", "12B")    
resident2 = Resident("Kiggundu", "14A")   

# Create hostel
hostel = Hostel("Deans")

# Record visits (they visit each other)
hostel.record_visit(visitor1, resident1)  
hostel.record_visit(visitor2, resident2)  
hostel.record_visit(resident1, visitor1)  
hostel.record_visit(resident2, visitor2)  

# Show all visits
hostel.show_visits()