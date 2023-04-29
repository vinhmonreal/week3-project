
class Return_on_Investment():
    my_dict = {
        'income' : {},
        'expenses' : {},
        'cash_on_cash' : {},
    }

    cash_flow_sum = None
    income_sum = None
    expenses_sum = None
    cash_on_cash_sum = None
    roi = None

    def add_income(self, key, value):
        try:
            value = float(value)
            self.my_dict['income'][key] = value
        except:
            print('Error...invalid value')
            return 0
            
    def get_income(self):
        self.income_sum = sum(self.my_dict['income'].values())
        print(f'Total income: ${self.income_sum }\n')
        return self.income_sum 
    
    def add_expenses(self, key, value):
        try:
            value = float(value)
            self.my_dict['expenses'][key] = value
        except:
            print('Error...invalid value')
            return 0
            
    def get_expenses(self):
        self.expenses_sum = sum(self.my_dict['expenses'].values())
        print(f'Total Expenses: ${self.expenses_sum}\n')
        return self.expenses_sum
    
    def get_cashflows(self):
        if self.income_sum != None and self.expenses_sum != None:
            self.cash_flow_sum = sum(self.my_dict['income'].values()) - sum(self.my_dict['expenses'].values())
            print(f'Cash flow: ${self.cash_flow_sum}\n')
            return self.cash_flow_sum
        else:
            print('Error...empty incomes or empty expenses')
            return 0
        
    def add_cash_on_cash(self, key, value):
        try:
            value = float(value)
            self.my_dict['cash_on_cash'][key] = value
        except:
            print('Error...invalid value')
            return 0
        
    def get_cash_on_cash(self):
        self.cash_on_cash_sum = sum(self.my_dict['cash_on_cash'].values()) 
        print(f'Total investment: ${self.cash_on_cash_sum}\n')
        return self.cash_on_cash_sum
    
    def get_ROI(self):
        if self.my_dict['cash_on_cash'] != {} and self.my_dict['income'] != {} and self.my_dict['expenses'] != {}:
            self.roi = round((sum(self.my_dict['income'].values()) - sum(self.my_dict['expenses'].values())) * 12 / sum(self.my_dict['cash_on_cash'].values()) * 100, 2)
            print(f'ROI: {self.roi} %\n')
            return self.roi
        else:
            print('Error...empty incomes or empty expenses or empty cash on cash')
            return 0
  







