import random
import operator

class Cipher:
    def __init__(self):
        self.numbers = []
        self.encrypted_numbers = []
        self.operations = []
        self.has_encrypted = False

    def input_numbers(self):  # The missing input_numbers method!
        while True:
            try:
                number = input("Enter a number (or 'q' to quit): ")
                if number.lower() == 'q':
                    break
                self.numbers.append(int(number))
                if self.has_encrypted:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def encrypt(self):
        if not self.numbers:
            print("No numbers to encrypt.")
            return

        number = self.numbers[0]
        operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        operation_symbol = random.choice(list(operations.keys()))
        operation = operations[operation_symbol]
        random_number = random.randint(1, 10)
        if operation_symbol == '/':
            while random_number == 0:
                random_number = random.randint(1, 10)
        try:
            encrypted_number = operation(number, random_number)
        except ZeroDivisionError:
            print("Error: division by zero")
            return

        self.encrypted_numbers.append(encrypted_number)
        self.operations.append((operation_symbol, random_number))
        self.has_encrypted = True

    def decrypt(self):
        if not self.encrypted_numbers:
            print("No numbers to decrypt.")
            return []

        decrypted_numbers = []
        encrypted_number = self.encrypted_numbers[0]
        operation_symbol, random_number = self.operations[0]
        operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv} # Use operator module
        operation = operations[operation_symbol] # Get the actual function
        try:
            decrypted_number_val = operation(encrypted_number, -random_number) if operation_symbol == '+' else \
                operation(encrypted_number, random_number) if operation_symbol == '-' else \
                operation(encrypted_number, 1/random_number) if operation_symbol == '/' else \
                operation(encrypted_number, random_number)
        except ZeroDivisionError:
            print("Error: division by zero")
            return []
        decrypted_numbers.append(decrypted_number_val)
        return decrypted_numbers

    def __str__(self):
        return str(self.encrypted_numbers)


# Create a Cipher object
cipher = Cipher()

# Get numbers from the user
cipher.input_numbers()

# Encrypt the numbers
cipher.encrypt()

# Print the encrypted numbers
print("Encrypted numbers:", cipher)

# Decrypt and print the original numbers
decrypted_numbers = cipher.decrypt()
print("Decrypted numbers:", decrypted_numbers)