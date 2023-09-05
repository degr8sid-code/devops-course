import random
import string

class Password:
    def __init__(self, length=8):
        self.__length = length
        self.__password = self.__generate_password()

    def __generate_password(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(self.__length))

    def is_strong(self):
        uppercase_count = 0
        lowercase_count = 0
        digit_count = 0

        for char in self.__password:
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
            elif char.isdigit():
                digit_count += 1

        return uppercase_count > 2 and lowercase_count > 1 and digit_count > 5

    def generate_password(self):
        self.__password = self.__generate_password()

    def get_password(self):
        return self.__password

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length
        self.generate_password()

class PasswordTest:
    @staticmethod
    def main():
        num_passwords = int(input("Enter the number of passwords: "))
        passwords = []

        for _ in range(num_passwords):
            length = int(input("Enter password length: "))
            passwords.append(Password(length))

        strong_passwords = [password.is_strong() for password in passwords]

        print("\nGenerated Passwords and Strength:")
        for password, strong in zip(passwords, strong_passwords):
            print(f"{password.get_password()} {strong}")

if __name__ == "__main__":
    PasswordTest.main()