class Room:
    def __init__(self,name, type , roomType ,money, address,zone, img_list, area):
        self.name = name
        self.type = type
        self.roomType = roomType
        self.money = money  
        self.address = address  
        self.zone = zone
        self.img_list = img_list  
        self.area = area 
    def to_dict(self):
            return {
                "name":self.name,
                "type":self.type,
                "roomType":self.roomType,
                "money": self.money,
                "address": self.address,
                "zone":self.zone,
                "img_list": self.img_list,
                "area": self.area
            }

class MyFilter:
    def __init__(self, moneyMax, moneyMin, address):
        self.moneyMax = moneyMax
        self.moneyMin = moneyMin
        self.address = address
    
    def to_dict(self):
        return {
            "moneyMax": self.moneyMax,
            "moneyMin": self.moneyMin,
            "address": self.address
        }
    
class MyHistory:
    def __init__(self, person, room):
        self.person = person
        self.room = room
    
    def to_dict(self):
        return {
            "person": self.person,
            "room": self.room.to_dict()  # Convert Room object to a dictionary
        }

class MyFavorite:
    def __init__(self, person, room):
        self.person = person
        self.room = room
    
    def to_dict(self):
        return {
            "person": self.person,
            "room": self.room.to_dict()  # Convert Room object to a dictionary
        }