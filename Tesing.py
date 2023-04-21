import unittest
from ROI import Return_on_Investment
   
class Test_Return_on_Investment(unittest.TestCase):
    def test_get_income(self):
        a = Return_on_Investment()
        a.income = {'rent' : 1000 , 'bonus' : 100}
        self.assertEqual(sum(a.income.values()),1100)
        b = Return_on_Investment()
        b.income = {'rent' : 2000 , 'bonus' : 300}
        self.assertEqual(sum(b.income.values()),2300)
    def test_get_expenses(self):
        a = Return_on_Investment()
        a.expenses = {'water' : 100 , 'HOA' : 100, 'Mort': 700}
        self.assertEqual(sum(a.expenses.values()),900)
        b = Return_on_Investment()
        b.expenses = {'water' : 50 , 'HOA' : 90, 'Mort': 700}
        self.assertEqual(sum(b.expenses.values()),840)
    def test_get_cash_flow(self):
        a = Return_on_Investment()
        a.income_total = 1000
        a.expenses_total = 800
        a.get_cashflows()
        self.assertEqual(a.cash_flow, 200)
    def test_get_cash_on_cash(self):
        a = Return_on_Investment()
        a.cash_on_cash = {'Down Payment':40000, 'Closing Cost' : 5000, 'Misc':2500}
        self.assertEqual(sum(a.cash_on_cash.values()), 47500)
    def test_get_ROI(self):
        a = Return_on_Investment()
        a.cash_flow = 200
        a.cash_on_cash_total = 50000
        a.get_ROI()
        self.assertEqual(a.roi, 4.8) 
    def test_zero_cash_on_cash(self):
        a = Return_on_Investment()
        a.cash_flow = 200
        self.assertEqual(a.get_ROI(), 'Error...Cash on Cash is zero') 
        b = Return_on_Investment()
        b.income_total = None
        b.expenses_total = None
        self.assertEqual(b.get_cashflows(),'Error...invalid type due to empty income or empty expense') 
        
        
if __name__ == '__main__':
    unittest.main()