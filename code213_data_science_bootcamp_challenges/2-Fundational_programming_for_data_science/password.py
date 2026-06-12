import random 
import string 

def generate_password(length, strength):
    """ Input: length of the password, strength level
        Output: a random password based on criteria
    """
    # List of weak passwords
    lst = ["password", "123456676", "sabrina"]
    
    # Check the strength of the password 
    if strength.lower() == "weak":
        return random.choice(lst)
    else:
        length = int(length)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

# This block must be completely unindented (outside the function)
if __name__ == "__main__":
    print("--- Password Generator ---")
    
    # Asking the user for input as required by the prompt
    user_strength = input("How strong do you want your password to be? (weak/strong): ").strip()
    
    user_length = 0
    if user_strength.lower() != "weak":
        user_length = input("Enter the desired password length: ")
    
    # Generate and print the password
    generated_pwd = generate_password(user_length, user_strength)
    print(f"Your generated password is: {generated_pwd}")