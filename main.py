# Написать приложение - контактная книга - с возможностью
# - добавлять
# - удалять
# - редактировать
# - искать по имени
#
# контакты (имя и множество номеров телефонов)


names = [
    "John", "Emily", "Aiden", "Sophia", "Muhammad", "Ava", "Matteo", "Isabella", "Santiago", "Mia",
    "Hiroshi", "Yui", "Yuto", "Haruka", "Mohammed", "Layla", "Gabriel", "Olivia", "Lucas", "Emma",
    "Liam", "Amelia", "Luis", "Sofia", "Rafael", "Camila", "Enzo", "Victoria", "Hugo", "Julia",
    "Sebastian", "Valentina", "Daniel", "Isabella", "Andres", "Maria", "Felipe", "Gabriela", "Diego", "Alejandra",
    "Leonardo", "Ana", "Carlos", "Mariana", "Matias", "Florencia", "Pedro", "Emilia", "Eduardo", "Luna",
    "Mario", "Carmen", "Raul", "Isabel", "David", "Elena", "Julian", "Carolina", "Javier", "Laura",
    "Manuel", "Paula", "Antonio", "Sara", "Miguel", "Luisa", "Jesus", "Beatriz", "Jose", "Marta",
    "Fernando", "Catarina", "Marcelo", "Sophie", "Joao", "Marianne", "Diogo", "Clara", "Pedro", "Lara",
    "Ricardo", "Alicia", "Gustavo", "Valeria", "Samuel", "Emilia", "Jorge", "Daniela", "Alejandro", "Adriana",
    "Ivan", "Monica", "Francisco", "Antonia", "Rafael", "Valeria", "Joel", "Natalia", "Gabriel", "Gabriela",
    "Ricardo", "Ana", "Cristian", "Lucia", "Mauricio", "Marina", "Emilio", "Raquel", "Victor", "Eva",
    "Hector", "Selena", "Roberto", "Catalina", "Mateo", "Ana", "Andres", "Maria", "Pablo", "Valentina",
    "Felix", "Ines", "Nathan", "Charlotte", "Emmanuel", "Alice", "Benjamin", "Chloe", "Louis", "Lena",
    "Mohamed", "Nora", "Ali", "Lara", "Khaled", "Leyla", "Youssef", "Jasmine", "Ahmed", "Sara",
    "Omar", "Lina", "Mustafa", "Aya", "Salim", "Rania", "Hassan", "Zara", "Jamil", "Laila",
    "Sami", "Noor", "Tariq", "Yara", "Arjun", "Aishwarya", "Ravi", "Sneha", "Vikram", "Pooja",
    "Rahul", "Neha", "Sachin", "Anaya", "Aarav", "Diya", "Rohan", "Ishika", "Aryan", "Sia"
]
surnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
    "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
    "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", "Walker", "Hall", "Young",
    "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams",
    "Nelson", "Baker", "Hall", "Mitchell", "Carter", "Roberts", "Turner", "Phillips", "Campbell", "Parker",
    "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan",
    "Bell", "Murphy", "Bailey", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Cruz", "Peterson",
    "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood",
    "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes",
    "Flores", "Simmons", "Foster", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes", "Myers",
    "Ford", "Hamilton", "Graham", "Sullivan", "Wallace", "Woods", "Cole", "West", "Jordan", "Owens",
    "Reynolds", "Fisher", "Ellis", "Harrison", "Gibson", "McDonald", "Cruz", "Marshall", "Ortega", "Byrd",
    "Davidson", "Hopkins", "May", "Terry", "Herrera", "Wade", "Soto", "Walters", "Curtis", "Neal",
    "Caldwell", "Lowe", "Jennings", "Barnett", "Graves", "Jimenez", "Horton", "Shelton", "Barrett", "Obrien",
    "Castro", "Sutton", "Gregory", "McKinney", "Lucas", "Miles", "Craig", "Rodriquez", "Chambers", "Holt",
    "Lambert", "Fletcher", "Watts", "Bates", "Hale", "Rhodes", "Pena", "Beck", "Newman", "Haynes",
    "McDaniel", "Mendoza", "Brewer", "Curtis", "Day", "Haynes", "Gibbs", "Chapman", "Griffith", "Miller"
]


country_codes = ["+38","+1","+44","+49","+33","+61","+81","+1","+55","+91","+86","+34","+39","+52","+7","+82","+54","+27","+31","+46","+41","+32","+47","+64","+966","+20","+90","+30","+48","+66","+65"]


emails = ["gmail.com","yahoo.com","hotmail.com","outlook.com","aol.com","icloud.com","protonmail.com","mail.com","zoho.com",
          "yandex.com","live.com","inbox.com","rocketmail.com","gmx.com","rediffmail.com","comcast.net","att.net","verizon.net",
          "cox.net","roadrunner.com","yahoo.co.uk","tutanota.com","mail.ru","abv.bg","web.de"]


contacts = [{"id":"ravimay", "name":"Ravi", "surname":"May", "phone":"0936655857","email":"ravimay@gmail.com"},
            {"id":"linamiles", "name":"Lina", "surname":"Miles", "phone":"0988959857","email":"linamiles@cox.net"},
            {"id":"alimiller", "name":"Ali", "surname":"Miller", "phone":"0988765434","email":"alimiller@cox.net"}]



def add_contact():
    name = input("Enter name -> ")
    if name in names:
        surname = input("Enter surname -> ")
        if surname in surnames:
            phone_country_code = input("Enter phone's country_code -> ")
            if phone_country_code in country_codes:
                phone_num = input("Enter phone number ( min 4 and max 12 numbers after country code ) -> ")
                if len(phone_num) > 3 and len(phone_num) < 13:
                    email = input("Enter email -> ")
                    if len(email) < 254 and len(email) > 4:
                        contact_id = (name + surname).lower()
                        phone = phone_country_code + phone_num
                        contacts.append({"id":contact_id, "name":name, "surname":surname,"phone":phone,"email":email})
                        print("You successfully added contact !")
                    else:
                        print("You entered invalid email params!")
                else:
                    print("You entered invalid phone params!")
            else:
                print("You entered invalid phone country code params!")
        else:
            print("You entered invalid surname!")
    else:
        print("You entered invalid name!")

#
def edit_contact():
    edited_contact = input("Enter contact's name and surname to edit info about him/ her ->  ")
    find_by_id = edited_contact.lower().replace(" ", "")
    for i in range(len(contacts)):
        if find_by_id == contacts[i]["id"]:
            edited_param = input("What do you want to change in contacts? Name/ surname/ phone/ email ? Choose just 1 parameter -> ")
            valid_edited_param = edited_param.lower()
            if valid_edited_param == "name":
                edited_name = input("Enter new name for editing the last one -> ")
                if edited_name in names:
                    name = edited_name
                    contacts[i]["name"] = name
                    contact_id = name.lower() + contacts[i]["surname"].lower()
                    contacts[i]["id"] == contact_id
                    print("You successfully changed name params!")
                    break
                else:
                    print("You didn't follow to instructions while editing name params!")

            if valid_edited_param == "surname":
                edited_surname = input("Enter new surname for editing the last one")
                if edited_surname in surnames:
                    surname = edited_surname
                    contacts[i]["surname"] = surname
                    contact_id = contacts[i]["name"].lower() + surname.lower()
                    contacts[i]["id"] == contact_id
                    print("You successfully changed surname params!")
                    break
                else:
                    print("You didn't follow to instructions while editing surname params!")

            if valid_edited_param == "phone":
                edited_phone_country_code = input("Enter new phone's country_code to edit the last one -> ")
                edited_phone_num = input("Enter new phone number ( min 4 and max 12 numbers after country code ) -> ")
                if edited_phone_country_code in country_codes:
                    if len(edited_phone_num) > 3 and len(edited_phone_num) < 13:
                        phone = edited_phone_country_code + edited_phone_num
                        contacts[i]["phone"] = phone
                        print("You successfully changed phone params!")
                        break
                else:
                    print("You didn't follow to instructions while editing phone params!")

            if valid_edited_param == "email":
                edited_email = input("Enter new email -> ")
                if len(edited_email) < 254 and len(edited_email) > 4 :
                    email = edited_email
                    contacts[i]["email"] = email
                    print("You successfully changed email params!")
                    break
                else:
                    print("You didn't follow to instructions while editing email params!")
        else:
            print("You entered invalid name or surname values!")



def delete_contact():
    contact_to_del = input("Enter contact's name and surname to delete contact -> ")
    valid_contact_to_del = contact_to_del.lower().replace(" ", "")
    for i in range(len(contacts)):
        if valid_contact_to_del == contacts[i]["id"]:
            del contacts[i]
            print("Contact successfully deleted!")
            break
        else:
            print("You entered invalid values of name and surname!")

def search_name():
    name_to_search = input("Enter contact's name to get more info -> ")
    for i in range(len(contacts)):
        if contacts[i]["name"] == name_to_search:
            print(contacts[i])

def exit_contacts():
    print("exit")

def print_contact():
    if len(contacts) > 0:
        for i in contacts:
            print(i)
    else:
        print("Your list of contacts is empty!")


menu = [["add contact", add_contact], ["delete contact", delete_contact], ["edit contact", edit_contact], ["search name", search_name], ["print contact", print_contact], ["exit", exit_contacts]]
print("\nWelcome to CONTACTS BOOK! ")


def print_menu():
    print("\nChoose your action -> ")
    for i in range(len(menu)):
        if i != len(menu)-1:
            print(menu[i][0].upper(), end=" or ")
        else:
            print(menu[i][0].upper(), end="")

print_menu()
option = input("\nWrite what do you want to do -> ")

while option != "exit":
    for i in range(len(menu)):
        if option.lower() == menu[i][0]:
            menu[i][1]()
    print_menu()
    option = input("\nWrite what do you want to do -> ")

