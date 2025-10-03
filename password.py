import random
import string
def generate_password(length , username):
    if length < 1:
        return "Password must be greater than 1"
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)for _ in range(length))
    return password
def main():
    print(":Welcome to password generator")
    username = input("Enter Username ")
    length = int(input("Enter the desired length of password "))

    password = generate_password(length , username)
    print(f"Generate Password for {username} : {password}")

if __name__=="__main__":
    main()