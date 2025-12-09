from data import accounts
from bank_account_management import BankAccountManagement

bam = BankAccountManagement(accounts)

def show_menu():
    print('\n\n\n------------------')
    print('1- Show All')
    print('2- Add user')
    print('3- Transfer')
    print('0- Exit')

def add_user():
    name = input('insert name: ')
    first_amount = input('insert amount: ')
    result = bam.add_user(name, first_amount)
    if result['status'] == 'ok':
        print(f"{name} is addedd successfully")
        
    if result['status'] == 'error':
        print(result['msg'])    
     
def main():
    while True:
        show_menu()
        command = input('select from menu: ')
        match command:
            case '1':
                bam.show_info()
            case '2':
                add_user()
            case '0':
                break
                
        
main()