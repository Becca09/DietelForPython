import unittest

from classworks.account import account


class AccountTest(unittest.TestCase):

    def test_that_account_can_be_created(self):
        account1 = account.Account("deola", "12345")
        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        account1 = account.Account("Tolani", "12345")
        name = account1.name
        self.assertEqual("Tolani", name)

    def test_that_account_can_deposit(self):
        account1 = account.Account("Tolani", "12345")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)

    def test_that_negative_deposit_raises_error(self):
        account1 = account.Account("Wale", "12345")
        account1.deposit(500)

        self.assertRaises(ValueError, account1.deposit, -1000)
        self.assertEqual(500, account1.balance)

    def test_that_money_can_be_withdrawn_test(self):
        account1 = account.Account("Wale", "12345")
        account1.deposit(5000)

        account1.withdraw(2000)
        self.assertEqual(3000, account1.balance)

    def test_that_negative_withdrawal_raises_error(self):
        account1 = account.Account("Wale", "12345")
        account1.deposit(300)

        self.assertRaises(ValueError, account1.withdraw, -300)
        self.assertEqual(300, account1.balance)

    def test_that_withdrawal_above_balance_raises_error(self):
        account1 = account.Account("Wale", "12345")
        account1.deposit(1200)

        self.assertRaises(ValueError, account1.withdraw, 10000)
        self.assertEqual(1200, account1.balance)

    def test_that_money_can_be_be_transferred(self):
        account1 = account.Account("Wale", "12345")
        account2 = account.Account("Femi", "12345")

        account1.deposit(3000)
        account1.transfer(1000, account2)

        self.assertEqual(2000, account1.balance)
        self.assertEqual(1000, account2.balance)

    def test_that_account_can_load_airtime(self):
        account1 = account.Account("Femi", "12345")
        account1.deposit(3000)
        account1.load_airtime(300)

        self.assertEqual(2700, account1.balance)


if __name__ == '__main__':
    unittest.main()
