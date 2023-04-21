
class Return_on_Investment():
    
    income = {}
    expenses = {}
    cash_on_cash = {}
    cash_flow = None
    income_total = None
    expenses_total = None
    roi = None
    cash_on_cash_total = None

    def driver(self):
        while True:
            res_income_name = input('What is your income? or enter done when done\n').lower()
            if res_income_name == 'done':
                break
            try:
                res_income_ammount = int(input('What is the ammount?\n'))
                self.income[res_income_name] = int(res_income_ammount)
            except:
                print('Please enter valid number of ammount')
        print(self.income)
        while True:
            res_expenses_name = input('What is your expense? or enter done when done\n').lower()
            if res_expenses_name == 'done':
                break
            try:
                res_expenses_ammount = int(input('What is the ammount?\n'))
                self.expenses[res_expenses_name] = int(res_expenses_ammount)
            except:
                print('Please enter valid number of ammount')
        print(self.expenses)
        while True:
            res_cash_on_cash_name = input('What is your cash on cash expense? or enter done when done\n').lower()
            if res_cash_on_cash_name == 'done':
                break
            try:
                res_cash_on_cash_ammount = int(input('What is the ammount?\n'))
                self.cash_on_cash[res_cash_on_cash_name] = int(res_cash_on_cash_ammount)
            except:
                print('Please enter valid number of ammount')
        print(self.cash_on_cash)
        self.get_income()
        self.get_expenses()
        self.get_cashflows()
        self.get_cash_on_cash()
        self.get_ROI()   
    def get_income(self):
        self.income_total = sum(self.income.values())
        print(f'Total income: ${self.income_total }\n')
        return self.income_total 
    def get_expenses(self):
        self.expenses_total = sum(self.expenses.values())
        print(f'Total Expenses: ${self.expenses_total}\n')
        return self.expenses_total
    def get_cashflows(self):
        if self.income_total != None and self.expenses_total != None:
            self.cash_flow = self.income_total - self.expenses_total
            print(f'Cash flow: ${self.cash_flow}\n')
            return self.cash_flow
        else:
            message = 'Error...invalid type due to empty income or empty expense'
            print(message)
            return message
    def get_cash_on_cash(self):
        self.cash_on_cash_total = sum(self.cash_on_cash.values()) 
        print(f'Total investment: ${self.cash_on_cash_total}\n')
        return self.cash_on_cash_total
    def get_ROI(self):
        if self.cash_flow != None and self.cash_on_cash_total != None and self.cash_on_cash_total != 0:
            self.roi = self.cash_flow * 12 / self.cash_on_cash_total * 100
            print(f'ROI: {self.roi} %\n')
            return self.roi
        else:
            message = 'Error...Cash on Cash is zero'
            print(message)
            return message

# my = Return_on_Investment()
# my.driver()
