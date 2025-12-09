from datetime import datetime as dt

class BankAccountManagement:
    def __init__(self, accounts:dict):
        self.accounts = accounts
        
    def show_info(self):
        for id in self.accounts:
            print(f"{id}- {self.accounts[id]['name']} ({self.accounts[id]['balance']})")
   
    def add_user(self, name:str, first_amount:float):
        if not name:
            return {'status': 'error', 'msg': 'Name is empty'}
            
        try:
            first_amount = float(first_amount)
        except:
            return {'status': 'error', 'msg': 'Amount is not float.'}
            
        id = len(self.accounts) + 1
        self.accounts.update({
            str(id): {
                    'name': name, 
                    'balance': first_amount, 
                    'history': [
                        {'time': dt.now().strftime('%Y-%m-%d %H:%M'), 'type': 'deposit', 'amount': first_amount},
                    ],
                    'status': 'active'     
                }
        })
        return {'status': 'ok'}
    
    def transfer(self, from_who:str, to_whom:str, amount:str): 
        # convert and check data type 
        try:
            from_who = int(from_who)
            to_whom = int(to_whom)
            amount = float(amount)
        except:
            return {'status': 'error', 'msg': 'Input types are not valid.'}          
            
        # check if id exist:
        if from_who not in self.accounts:
            return {'status': 'error', 'msg': 'Withdraw user does not exist.'}
        if to_whom not in self.accounts:
            return {'status': 'error', 'msg': 'Deposite user does not exist.'}
        if self.accounts[from_who]['balance'] < amount:
            return {'status': 'error', 'msg': 'Withdraw user does not have enough balance.'}
           
        try: 
            self.accounts[from_who]['balance'] -= amount
            self.accounts[to_whom]['balance'] += amount
            
            self.accounts[from_who]['history'].append(
                {'time': dt.now().strftime('%Y-%m-%d %H:%M'), 'type': 'Withdraw', 'Amount': amount}
            )

            self.accounts[to_whom]['history'].append(
                {'time': dt.now().strftime('%Y-%m-%d %H:%M'), 'type': 'Deposite', 'Amount': amount}
            )
            return {'status': 'ok'}
            
        except:
            return {'status': 'error', 'msg': 'Some error happened..'}
    
    def deposit(self):
        pass 
       
    def withdraw(self):
        pass    
            
