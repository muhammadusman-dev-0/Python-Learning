class SkillTrack:
    def __init__(self):
        self.skills = []
        self.file_name = "skills.txt"
        self.load_skills()

    def load_skills(self):
     file = open(self.file_name, "a+")
     file.seek(0)

     for line in file:
        data = line.strip().split(",")

        if len(data) == 2:
            skill = {
                "name": data[0],
                "progress": int(data[1])
            }
            self.skills.append(skill)

        file.close()

    def add_skill(self):
        name = input("Enter skill name: ")
        progress = int(input("Enter progress (0-100): "))

        if progress >= 0 and progress <= 100:
            skill = {
                "name": name,
                "progress": progress
            }

            self.skills.append(skill)

            file = open(self.file_name, "a")
            file.write(name + "," + str(progress) + "\n")
            file.close()

            print("Skill saved!")

        else:
            print("Progress must be between 0 and 100.")

    def view_skills(self):
        if len(self.skills) == 0:
            print("No skills added yet.")
        else:
            for skill in self.skills:
                print(
                    skill["name"],
                    "-",
                    str(skill["progress"]) + "%"
                )

    def average_progress(self):
        if len(self.skills) == 0:
            print("Add a skill first.")
        else:
            total = 0

            for skill in self.skills:
                total = total + skill["progress"]

            average = total / len(self.skills)

            print("Average progress:", str(round(average, 1)) + "%")

    def run(self):
        while True:
            print("\n===== SKILLTRACK =====")
            print("1. Add Skill")
            print("2. View Skills")
            print("3. Calculate Average Progress")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_skill()

            elif choice == "2":
                self.view_skills()

            elif choice == "3":
                self.average_progress()

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Choose 1 to 4.")


app = SkillTrack()
app.run()








