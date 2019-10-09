import time

################## List of Properties ################## 
'''
Global Object Properties:
- id
- name

Room Object Properties:
- description
- exits

Player Object Properties:
- strength
- arm_wrestle
'''


################## Generic Object ################## 

class generic:
    # kids should be a dictionary that contains all of the important 
    # info about each child object -- change to obj_info
    kids = 0
    obj_info = {}
    def __init__(self, name=None):
        __class__.kids += 1
        self.num = __class__.kids
        if name == None:
            self._name = f'Generic {self.__class__.__name__}'
        else:
            self._name = name
        obj_info[self.id] = {"name": self._name}
        

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'({self.id}) {self.name}'

    @property
    def id(self):
        return str(self.num).zfill(5)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

################## Room Object ################## 

class room(generic):
    def __init__(self, exits=[], desc="A Generic Room"):
        super().__init__()
        self._exits = exits
        self.desc = desc 

    @property
    def description(self):
        self.obj_info[self.id]['description'] = self.desc
        return self.desc

    @property
    def exits(self):
        self.obj_info[self.id]['exits'] = self.exits
        return self._exits

################## Player Object ################## 

class Player(generic):
    
    def __init__(self, name, stren):
        super().__init__(name)
        self._strength = stren

    
    @property
    def strength(self):
        return self._strength
    
    @property
    def arm_wrestle(self):
        return int(self.strength/2)

def arm_wrestle(plyr1, plyr2):
    match = [(plyr1, plyr1.arm_wrestle), (plyr2, plyr2.arm_wrestle)]
    # need to break this out to be more complex -->> Need a draw scenario
    return f'{repr(match[0][0]) if match[0][1] >= match[1][1] else repr(match[1][0])} wins!'

def main():
    print(f'Initializing...')
    time.sleep(2)
    print("||| Connected |||")
    user = input("Username>> ")
    

#main()

    

gener1 = generic("Genery the helpful generic object")
print(gener1.id)
print(gener1)
print(repr(gener1))

# player1 = Player("Muhammad Ali", 20)

# player1
# print(player1.strength)
# print(player1.arm_wrestle)
# print(player1.name)

# room1 = room()
# print(room1.name)

# player2 = Player("Jimmy Buckets", 14)
# print(player2.arm_wrestle)


# print(repr(player1))
# print(player2.id)

# room2 = room()
# print(repr(room2))
# room2.name = "Ball Room"
# print(repr(room2))

# player3 = Player("Tandem Bicycleman", 47)

# print(player3)
# print(repr(player3))

# print(arm_wrestle(player2, player1))
