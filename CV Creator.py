# CV Creator
class CVCreator:
    def login(self):
        login_id = "admin"
        password = "12345"
        entered_id = input("Enter Login ID: ")
        entered_password = input("Enter Password: ")
        if entered_id == login_id and entered_password == password:
            print("Login successful!")
            self.display_cv_form()
        else:
            print("Invalid Login ID or Password!")

    def display_cv_form(self):
        name = input("Dynamic CV Creator\nEnter your full name: ")
        fathers_name = input("Enter father's name: ")
        mothers_name = input("Enter mother's name: ")
        education = input("Enter your education details: ")
        skills = input("Enter your skills: ")
        experience = input("Enter your work experience: ")
        out_skills = input("Enter other skills: ")
        marital_status = input("Enter marital status: ")
        religion = input("Enter your religion: ")
        self.generate_cv(name, fathers_name, mothers_name, education, skills,
                         experience, out_skills, marital_status, religion)

    def generate_cv(self, name, fathers_name, mothers_name, education,
                    skills, experience, out_skills, marital_status, religion):
        print("\nCV Preview")
        print(f"Name: {name}")
        print(f"Father's Name: {fathers_name}")
        print(f"Mother's Name: {mothers_name}")
        print(f"Education: {education}")
        print(f"Skills: {skills}")
        print(f"Experience: {experience}")
        print(f"Other Skills: {out_skills}")
        print(f"Marital Status: {marital_status}")
        print(f"Religion: {religion}")

if __name__ == "__main__":
    cv_creator = CVCreator()
    cv_creator.login()