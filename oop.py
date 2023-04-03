# class vehicle:
#     #attributes
#     colour="black"
# class car(vehicle):
#     pass
# print(car.__mro__)

# v1=vehicle()
# c1=car()
# print(c1.colour)
# class vehicle:
#    def __init__(self,color,model):
#       self.color=color
#       self.model=model
# class car(vehicle):
#    def __init__(self, color, model):
#       super().__init__(color, model)
# class sportscar(car):
#    def s_cars(self,color,model):
#       return f"color: {color}  model: {model} "
# print(sportscar.__mro__)
# c1=sportscar("blue","BMW")
# print(c1.s_cars("blue","BMW"))
# print(c1.color)

class person:
    #when using a contructor 
    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age
    def person_info(self,name,age):
        return f"hello there my name is {name} and aged {age}"
class company:
    def company_info(self,name,location):
        return f"Welcome to {name} we are currently based at {location}"
class employee(person,company):
    def employee_info(self,name,position,salary):
        return f"my name is {name} am the {position} with a salary of {salary}"
    #while using a contructors on calling the method using an object it should take arguments
# em = employee("Spedag","Kenya")
em = employee()
print(em.company_info("Spedag","Kenya"))