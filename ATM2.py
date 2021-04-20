import random
from datetime import date, datetime

print("\nWelcome to Python ATM app")
print("*" * 20)

continued = "1"

# ******************List of existing customers
fname = ["James", "Ojo", "Ola", "Cole", "Ase"]
lname = ["Temi", "Vik", "Sit", "Ricado", "Eric"]
acctNum = [4011234567, 1268483838, 661783883737, 179476162737, 1738467367]
sex = ["Male", "Female", "Male", "Female", "Male"]
usernames = ["Felix", "Matt", "Andrew", "Emeka", "Bidemi"]
dob = ["2/3/1990", "23/4/1980", "12/3/1982", "3/9/1994", "29/2/1991"]
passwords = ["olrik", "figh", "Temil", "rtwe34", "tyeii"]

balance = 20000


# ******************Register function
def register(reg_fname, reg_lname, reg_sex, reg_dob, reg_usernames, reg_passwords):
    # Accept customer information
    add_fname = input("\nEnter your First Name : \n")
    add_lname = input("\nEnter your Last Name : \n")
    add_sex = input("\nWhat is your Sex :  'Male' or 'Female'\n")
    add_dob = input("\nWhat is your Date of birth ;  'dd/mm/yyyy'  \n")
    add_usernames = input("\nCreate your username : \n")
    add_passwords = input("\nCreate your password : \n")

    # Add new customer information to existing customer list
    reg_fname.append(add_fname)
    reg_lname.append(add_lname)
    reg_sex.append(add_sex)
    reg_dob.append(add_dob)
    reg_usernames.append(add_usernames)
    reg_passwords.append(add_passwords)

    print("Regsiteration was successful!!")


def login(allowedUsers, passwords):
    count = 0
    while count != 3:
        username = input("\nEnter username: 》 ")
        if username in allowedUsers:
            userId = allowedUsers.index(username)
            enterPassword = input("Enter password: 》 ")
            if enterPassword == passwords[userId]:
                print("\nYou have logged in successfully")
                return 1
                break
            else:
                print("Pasword is incorrect.")

        else:
            if count != 2:
                print("Username is incorrect.\nTry again")

            else:
                print(
                    "\nUsername is incorrect and You have exceeded number of login attempts")
        count += 1


# ******************Account generator Function
def acctGen(accounts):
    for num in accounts:
        if add_acctNum != num:
            accounts.append(add_acctNum)
            break


while continued == "1":
    print("\nWelcome back")
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # randomize 10digits account number
    add_acctNum = random.randint(1100000000, 10000000000)

    print("\nTo Login: 1")
    print("To Register: 2")
    actionNum = int(input("\nEnter action to perform >>:  "))
    if actionNum == 1:
        print("\nLogin page")
        done = login(usernames, passwords)
        if done == 1:
            print("\n**************   *************")
            print("\nToday's date:   ", today)
            print("Current Time :  ", current_time)
            print("\n**************   *************")

            print("1: Withdrawal")
            print("2 : Deposit")
            print("3 : Complaint")

            option = input("Select an option: 》 ")

            if int(option) == 1:
                cash = float(
                    input("\nHow much would you like to withdraw? 》 "))
                balance -= cash
                print("Take your cash: N", cash)

            elif int(option) == 2:
                cash = float(input("\nHow much would you like to deposit? 》 "))
                balance += cash
                print("Your current balance is: ", balance)

            elif int(option) == 3:
                issue = input("\nWhat issue will you  like to report? 》 ")
                print("\nThank you for contacting us")

            else:
                print("\nYou entered an invalid option")

    elif actionNum == 2:
        print("\nRegister page")
        # Function calls to update customer register
        register(fname, lname, sex, dob, usernames, passwords)
        acctGen(acctNum)

    else:
        print("\nWrong selection made")

    continued = input(
        "\nEnter 1 to run app again and any other number to exit 》 ")
    if continued != "1":
        print("  Goodbye!  ")
