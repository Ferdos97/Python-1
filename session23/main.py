from data_manager import DataManager
from bank_account_management import BankAccountManagement

dm = DataManager()
try: 
    accounts = dm.get()
except:
    accounts = dict()
    
bam = BankAccountManagement(accounts)

def show_menu():
    print('\n\n\n------------------')
    print('1- Show All')
    print('2- Add user')
    print('3- Transfer')
    print('4- Deposite')
    print('5- Withdraw')
    print('6- Exit\n')
  
def add_user():
    name = input('Insert name: ')
    first_amount = input('Insert amount: ')
    result = bam.add_user(name, first_amount)
    if result['status'] == 'ok':
        print(f"{name} is addedd successfully.")
        
    if result['status'] == 'error':
        print(result['msg'])    

def transfer():
    from_who = input('From who: ')
    to_whom = input('To whom: ')
    amount = input('Amount: ')
    
    result = bam.transfer(from_who, to_whom, amount)
    if result['status'] == 'error':
        print(result['msg'])
    else:
        print('Transfer is done.')

def deposit():
    pass

def withdraw():
    pass

def main():
    while True:
        show_menu()
        dm.set(accounts)
        command = input('Select from menu: ')
        if command == '1':
            bam.show_info()
        elif command == '2':
            add_user()
        elif command == '3':
            transfer()
        elif command == '4':
            deposit()
        elif command == '5':
            withdraw()
        elif command == '6':
            break
        else:
            print('Wrong choice, Try again.')
            
    
main()