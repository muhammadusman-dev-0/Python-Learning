class Employe:
    language="urdu"
    salary="20000"

    def __init__(self):
        print(" i am creating an object")
    

    def get_info (self):
        print(f"you are my employe {self.language},what is your salary{self.salary}")



harry=Employe()
harry.name="usman"
print(harry.name,harry.language,harry.salary)

rohan=Employe()




