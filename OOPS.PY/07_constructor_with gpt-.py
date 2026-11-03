class Employe:

    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def get_info(self):
        print(f"The name is {self.name}, the language is {self.language}, the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


name = input("Enter your name : ")
language = input("Enter your language : ")
salary = int(input("Enter your salary : "))

usman = Employe(name, language, salary)

print(usman.name, usman.language, usman.salary)