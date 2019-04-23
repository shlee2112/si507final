# SI507project_tests.py

from SI507project_tools import *
import unittest


class StepOne(unittest.TestCase):

	def setUp(self):
		self.dollar = Dollar(1)
		self.pound = Pound(1)
		self.yuan = Yuan(1)
		self.dollar_mult = Dollar(12)

	def test_subclasses_instance_of_currency(self):

		self.assertIsInstance(self.dollar, Currency,"Testing that an instance of Dollar is an instance of a subclass of Currency") # Because you had to define this in such a way that it inherited from Currency -- it is possible for it not to be in the submitted code, hence the test
		self.assertIsInstance(self.pound, Currency,"Testing that an instance of Pound is an instance of a subclass of Currency")
		self.assertIsInstance(self.yuan, Currency,"Testing that an instance of Yollar is an instance of a subclass of Currency")

	# Testing the three Currencies
	def test_dollar_constructor(self):
		self.assertEqual(self.dollar.base_rate, 1, "Testing that dollar's base_rate (that is, the base rate in the Currency class) is 1")
		self.assertEqual(self.dollar_mult.base_rate, 1,"Testing that even with multiple dollar representation in an instance, the base rate is still 1")

	def test_dollar_rate(self):
		self.assertEqual(Dollar.rate, 20, "Testing that Dollar's rate is 20")
		self.assertEqual(self.dollar_mult.rate, 20, "Testing that rate is set correctly for a dollar instance")

	def test_dollar_unit_name(self):
		self.assertEqual(Dollar.unit_name, "Dollar", "Testing that Dollar's unit name is correct")

	def test_dollar_str(self):
		hundred_dollars = Dollar(100)
		self.assertEqual(self.dollar.__str__(), "1 Dollar", "Testing string method on Dollar class") # Note that this is an example of testing a string method -- can't test things printed, but can test things returned, and this is how you invoke __str__ !
		self.assertEqual(hundred_dollars.__str__(), "100 Dollars", "Testing string method on Dollar class")


	def test_pound_constructor(self):
		self.assertEqual(self.pound.base_rate, 1, "Testing that pound constructor works properly")

	def test_pound_rate(self):
		self.assertEqual(Pound.rate, 15,"Testing that pound's rate is correct")

	def test_pound_unit_name(self):
		self.assertEqual(Pound.unit_name, "Pound", "Testing pound's unit name")

	def test_pound_str(self):
		hundred_pounds = Pound(100)
		self.assertEqual(self.pound.__str__(), "1 Pound", "Testing Pound's string method")
		self.assertEqual(hundred_pounds.__str__(), "100 Pounds", "Testing Pound's string method")


	def test_yuan_constructor(self):
		self.assertEqual(self.yuan.base_rate, 1, "Testing base rate of Yuan class (does it inherit from Currency correctly)")

	def test_yuan_rate(self):
		self.assertEqual(Yuan.rate, 8,"Testing that Yuan rate is correct")

	def test_yuan_unit_name(self):
		self.assertEqual(Yuan.unit_name, "Yuan","Testing that Yuan unit name is correct")

	def test_yuan_str(self):
		hundred_yuan = Yuan(100)
		self.assertEqual(self.yuan.__str__(), "1 Yuan","Testing Yuan string method")
		self.assertEqual(hundred_yuan.__str__(), "100 Yuan","Testing Yuan string method")

	# Testing conversion
	def test_currency_conversion(self):
		self.assertEqual(self.yuan.conversion(Pound).__str__(), "0.5333333333333333 Pound", "Testing currency conversion with Yuan to Pound")
		self.assertEqual(self.pound.conversion(Dollar).__str__(), "0.75 Dollar","Testing currency conversion with Pound to Dollar")

	def tearDown(self):
		del(self.dollar)
		del(self.pound)
		del(self.yuan)

class StepTwo(unittest.TestCase):

	def setUp(self):
		self.jpMorgan = Bank("J.P.Morgan", Dollar, 10000)
		self.bearsterns = Bank("Bear Sterns", Dollar)
		self.bankOfChina = Bank("Bank of China", Yuan, 10000)

	def test_bank_constructor_name(self):
		self.assertEqual(self.jpMorgan.name, "J.P.Morgan", "Testing Bank constructor")
		self.assertEqual(self.bearsterns.name, "Bear Sterns", "Testing Bank constructor")

	def test_bank_default_constructor(self):
		self.assertTrue(self.bearsterns.current_account.value == 0,"Testing that default initial value from Bank constructor is 0")

	def test_bank_constructor_unit(self):
		self.assertTrue(issubclass(self.jpMorgan.unit, Currency), "Testing that Bank's unit is a subclass of Currency - Dollar, Yuan, or Pound")
		self.assertEqual(self.jpMorgan.unit, Dollar, "Testing an instance of Bank's setting of its unit in constructor, e.g. Dollar")
		self.assertEqual(self.bankOfChina.unit, Yuan, "Testing an instance of Bank's setting of its unit in constructor, e.g. Yuan")

	def test_bank_constructor_current_account(self):
		self.assertEqual(self.jpMorgan.current_account.value, 10000, "Testing value of bank from constructor's invocation")
		self.assertEqual(self.bankOfChina.current_account.value, 10000,"Testing value of bank from constructor's invocation")

	def test_bank_str(self):
		self.assertEqual(self.jpMorgan.__str__(),
			"J.P.Morgan Bank holds the Dollar currency and currently holds 10000 of Dollar","Testing string method of Bank")

		self.assertEqual(self.bankOfChina.__str__(),
			"Bank of China Bank holds the Yuan currency and currently holds 10000 of Yuan","Testing string method of Bank")

	def test_bank_deposit(self):
		d = Dollar(1)
		y = Yuan(1)
		self.assertEqual(self.bankOfChina.deposit(d), 'ERROR: cannot deposit that currency.',"Testing deposit of wrong currency")
		self.assertEqual(self.bankOfChina.deposit(y), 'successful deposit',"Testing successful deposit")
		self.assertEqual(self.bankOfChina.deposit(100), 'ERROR: cannot deposit that currency.',"Testing invalid deposit")

	def tearDown(self):
		del(self.jpMorgan)
		del(self.bearsterns)
		del(self.bankOfChina)

if __name__ == "__main__":
    unittest.main(verbosity=2)
