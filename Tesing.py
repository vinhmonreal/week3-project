import unittest
from ROI import Return_on_Investment
   
class Test_Return_on_Investment(unittest.TestCase):
    def test_get_income(self):
        a = Return_on_Investment()
        a.add_income('rent' ,  1000)
        a.add_income('bonus' , 100.8)
        self.assertEqual(a.get_income(), 1100.8)
        b = Return_on_Investment()
        self.assertEqual(b.add_income('rent' , 900j), 0)
    def test_get_expenses(self):
        a = Return_on_Investment()
        a.add_expenses('water' , 100.70 )
        a.add_expenses('HOA' , 100)
        a.add_expenses('Mort', 700)
        self.assertEqual(a.get_expenses(), 900.7)
        b = Return_on_Investment()
        self.assertEqual(b.add_expenses('HOA' , 90j), 0)
    def test_get_cash_flow(self):
        a = Return_on_Investment()
        a.add_income('rent' ,  1000.50)
        a.add_income('bonus' , 100)
        a.add_expenses('water' , 100 )
        a.add_expenses('HOA' , 100)
        a.add_expenses('Mort', 700)
        a.get_expenses()
        a.get_income()
        self.assertEqual(a.get_cashflows(), 200.5)
    def test_get_cash_on_cash(self):
        a = Return_on_Investment()
        a.add_cash_on_cash('Down Payment',40000)
        a.add_cash_on_cash('Closing Cost',5000)
        a.add_cash_on_cash('Misc',2500)
        self.assertEqual(a.get_cash_on_cash(), 47500)
        b = Return_on_Investment()
        self.assertEqual(b.add_cash_on_cash('Down Payment',40000j), 0)
    def test_get_ROI(self):
        a = Return_on_Investment()
        a.add_income('rent' ,  1000)
        a.add_income('bonus' , 100)
        a.add_expenses('water' , 100 )
        a.add_expenses('HOA' , 100)
        a.add_expenses('Mort', 700)
        a.add_cash_on_cash('Down Payment',40000)
        a.add_cash_on_cash('Closing Cost',4000)
        a.add_cash_on_cash('Misc',2400)
        a.get_expenses()
        a.get_income()
        a.get_cash_on_cash()
        self.assertEqual(a.get_ROI(), 5.17) 
        
        
if __name__ == '__main__':
    unittest.main()