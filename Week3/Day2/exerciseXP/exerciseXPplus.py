#Exercise 1 : Family
members = [
                {'name':'Michael','age':35,'gender':'Male','is_child':False},
                {'name':'Sarah','age':32,'gender':'Female','is_child':False}
            ]

class Family:
    
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
    def born(self, **kwargs):
        # newborn = {}
        # for key, value in kwargs.items():
            # newborn[key] = value
        self.members.append(kwargs)
        print("Congrats on a newborn")
    def is_18(self, member_name):
        value = member_name
        member = {}
        for dict in self.members:
            if value in dict["name"]:
                member = dict
        if (member["age"] >= 18):
            return True
        else:
            return False
    def family_presentation(self):
        result = self.last_name
        for member in self.members:
            result += ("\n " + member["name"])
        print(result)
family = Family(members, "Smith")
print(family.is_18("Sarah"))
family.family_presentation()
family.born(name="Bob", age = 0, gender = "Male", is_child = True)
family.family_presentation()

#Exercise 2 : TheIncredibles Family

incredibles = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
                ]

class TheIncredibles(Family):
    def use_power(self, member_name):
        value = member_name
        for dict in self.members:
            if value in dict["name"]:
                if dict["age"] < 18:
                    raise Exception("You are not over 18 years old")
                else:
                    print (dict["power"])
    def incredible_presentation(self):
        result = ""
        super().family_presentation()
        for member in self.members:
            result += (" " + member["incredible_name"] + " " + member["power"] + "\n")
        print(result)

theIncredible = TheIncredibles(incredibles, "Dunno")
theIncredible.family_presentation()
theIncredible.incredible_presentation()
theIncredible.born(name="Jack", age = 0, gender = "Male", is_child = True, power = "Unknown Power", incredible_name = "BOB")
print("FAMILY PRESENTATION AFTER BOB")
theIncredible.incredible_presentation()
theIncredible.use_power("Michael")
theIncredible.use_power("Bob")