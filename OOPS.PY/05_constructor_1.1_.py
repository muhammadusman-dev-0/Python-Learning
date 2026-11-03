class Employe:
    name=input("Enter your name : ")
    language=input("Enter your language :")
    salary=int(input("Enter your salary :"))

    def __init__(self, name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
        print("I am creating an object")
    
    def get_info(self):
        print(f"the name is {self.name},the language is{self.language},the salary is {self.salary}")

        @staticmethod
        def greet():
            print("good morning")
    

usman=Employe()
print(usman.name , usman.language ,usman.salary)













