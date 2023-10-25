def print_menu():
    print("Menu")
    print(13 * '-')
    print("1. Encode")
    print("2. Quit")

def encoder(password):
    new_password = []
    final_password = ''
    for i in range(len(password)):
        if int(password[i]) >= 7:
            new_password.append((str((int(password[i]) + 3))[1:]))
        else:
            new_password.append(str((int(password[i]) + 3)))
    for i in range(len(new_password)):
        final_password += new_password[i]
    return final_password

def main():
    print_menu()
    user_option = input('Please enter an option: ')
    while user_option != "2":
        if user_option == "1":
            user_password = input("Please enter your password to encode: ")
            encoded_password = encoder(user_password)
            print("Your password has been encoded and stored")
        print_menu()
        user_option = input('Please enter an option: ')

if __name__ == "__main__":
    main()