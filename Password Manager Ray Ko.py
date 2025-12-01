# Character set used for ROT3 encryption
CHAR_SET = (
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef""ghijkl"
    "mnopqrstuvwxyz""`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
)

# List to store decrypted entries
temp_list = []


# Encrypt using ROT3
def encrypt(text):
    result = ""
    for c in text:
        index = CHAR_SET.find(c)
        result += CHAR_SET[(index + 3) % len(CHAR_SET)]
    return result


# Decrypt ROT3
def decrypt(text):
    result = ""
    for c in text:
        index = CHAR_SET.find(c)
        result += CHAR_SET[(index - 3) % len(CHAR_SET)]
    return result


# Create file only once
def create_file():
    try:
        with open("credentials.txt", "x", encoding="utf-8") as file:
            file.write("WEBSITE | USERNAME | PASSWORD\n")
            file.write("--------------------------------\n")
    except FileExistsError:
        pass


# Add encrypted credentials
def add_credentials():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    with open("credentials.txt", "a", encoding="utf-8") as file:
        file.write(
            f"{encrypt(website)} | {encrypt(username)} | {encrypt(password)}\n"
        )

    print("Credentials saved.\n")


# View decrypted credentials
def view_credentials():
    temp_list.clear()

    with open("credentials.txt", "r", encoding="utf-8") as file:
        for line in file:
            # Skip header
            if "WEBSITE" in line or "---" in line or line.strip() == "":
                continue

            parts = line.split("|")

            if len(parts) == 3:
                website = decrypt(parts[0].strip())
                username = decrypt(parts[1].strip())
                password = decrypt(parts[2].strip())
                temp_list.append([website, username, password])

    print("\nStored Credentials")
    print("--------------------------------")

    for item in temp_list:
        print(f"{item[0]:15} | {item[1]:15} | {item[2]:15}")

    print()


# Menu loop
def main():
    create_file()

    print("\nPassword Manager\n")

    choice = ""

    while choice != "q":
        print("[1] Add credentials")
        print("[2] View credentials")
        print("[q] Quit")

        choice = input("Make your choice: ")

        if choice == "1":
            add_credentials()
        elif choice == "2":
            view_credentials()
        elif choice != "q":
            print("Invalid option, try again.\n")

    print("Program exit.")


if __name__ == "__main__":
    main()
