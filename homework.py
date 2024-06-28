# Jessica Uriostegui
# June 26, 2024

# class was created with attributes
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
# Implemented getter and setter to update owner  
    def get_owner(self):
        return self.owner
    
    def set_owner(self, new_owner):
        self.owner = new_owner

# Created an instance to show the update      
jeep = Vehicle("1ABCD34567E891011","Wrangler","Bob")

jeep.set_owner("Alice")


print(f"Jeep registration number : {jeep.registration_number}")
print(f"Jeep model type: {jeep.type}")
print(f"Jeep's new vehicle owner : {jeep.get_owner()}")



# Task 2: Event Management System Enhancement
# Class was created with attributes
class Event:
    # count attribute was added to keep track of participants
    def __init__(self, name, date, participant_count=0):
            self.name = name
            self.date = date
            self.participant_count = participant_count
    # method to add participants to add to participant_count 
    def add_participant(self,count=1):
         self.participant_count += count
    # method for retrieving updated participant_count
    def get_participant_count(self):
         return self.participant_count
    # created an instance
event = Event("Birthday", "2024-27-06", 25)
    
event.add_participant(5)


print(event.name)
print(event.date)
print(event.get_participant_count())