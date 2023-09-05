import random

class Person:
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    IDEAL_WEIGHT = 0
    BELOW_IDEAL_WEIGHT = -1
    OVERWEIGHT = 1

    def __init__(self, name='', age=0, gender=GENDER_MALE, weight=0, height=0):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__weight = weight
        self.__height = height
        self.__id = self.__generate_id()

    def __generate_id(self):
        return random.randint(10000000, 99999999)

    def __check_gender(self, gen):
        return gen.upper() in [self.GENDER_MALE, self.GENDER_FEMALE]

    def calculate(self):
        if self.__height == 0:
            return self.IDEAL_WEIGHT
        bmi = self.__weight / (self.__height ** 2)
        if bmi < 18.5:
            return self.BELOW_IDEAL_WEIGHT
        elif bmi >= 18.5 and bmi < 25:
            return self.IDEAL_WEIGHT
        else:
            return self.OVERWEIGHT

    def is_over_18(self):
        return self.__age >= 18

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_gender(self, gender):
        if self.__check_gender(gender):
            self.__gender = gender

    def set_weight(self, weight):
        self.__weight = weight

    def set_height(self, height):
        self.__height = height

    def __str__(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nGender: {self.__gender}\nWeight: {self.__weight}\nHeight: {self.__height}\nID: {self.__id}"

# Executable class
class PersonTest:
    @staticmethod
    def input_person():
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender (M/F): ")
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))
        return Person(name, age, gender, weight, height)

    @staticmethod
    def main():
        person1 = PersonTest.input_person()
        person2 = Person(name="John", age=25)
        person3 = Person()

        person_list = [person1, person2, person3]

        for person in person_list:
            bmi_result = person.calculate()
            legal_age = "Legal Age" if person.is_over_18() else "Not Legal Age"

            if bmi_result == person.IDEAL_WEIGHT:
                bmi_msg = "Ideal Weight"
            elif bmi_result == person.BELOW_IDEAL_WEIGHT:
                bmi_msg = "Below Ideal Weight"
            else:
                bmi_msg = "Overweight"

            print("\n" + str(person))
            print(f"BMI Result: {bmi_msg}")
            print(legal_age)
            print("=" * 30)

if __name__ == "__main__":
    PersonTest.main()