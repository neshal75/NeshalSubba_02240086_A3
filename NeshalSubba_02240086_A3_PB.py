import unittest
from NeshalSubba_02240086_A3_PA import BankAccount, InvalidInputError, TransferError

class TestBankAccount(unittest.TestCase):
    """Unit test suite for the BankAccount class."""

    def setUp(self):
        """Set up sample accounts for testing."""
        self.owner = BankAccount("Owner", 1000)
        self.friend = BankAccount("Friend", 500)

    def test_deposit_valid_amount(self):
        """Test depositing a valid positive amount."""
        self.owner.deposit_money(250)
        self.assertEqual(self.owner.balance, 1250)

    def test_deposit_invalid_negative_amount(self):
        """Test depositing a negative amount should raise InvalidInputError."""
        with self.assertRaises(InvalidInputError):
            self.owner.deposit_money(-100)

    def test_withdraw_valid_amount(self):
        """Test withdrawing a valid amount."""
        self.owner.money_withdraw(300)
        self.assertEqual(self.owner.balance, 700)

    def test_withdraw_exceed_balance(self):
        """Test withdrawing more than available balance should raise TransferError."""
        with self.assertRaises(TransferError):
            self.owner.money_withdraw(1500)

    def test_transfer_valid(self):
        """Test a valid money transfer between accounts."""
        self.owner.money_transfer(200, self.friend)
        self.assertEqual(self.owner.balance, 800)
        self.assertEqual(self.friend.balance, 700)

    def test_transfer_invalid_amount(self):
        """Test transferring more than available balance should raise TransferError."""
        with self.assertRaises(TransferError):
            self.owner.money_transfer(2000, self.friend)

    def test_top_up_valid(self):
        """Test topping up a valid mobile number with valid amount."""
        self.owner.top_up_mobile("12345678", 100)
        self.assertEqual(self.owner.balance, 900)

    def test_top_up_invalid_number_length(self):
        """Test topping up an invalid mobile number should raise InvalidInputError."""
        with self.assertRaises(InvalidInputError):
            self.owner.top_up_mobile("123", 50)

    def test_top_up_non_digit_number(self):
        """Test topping up a non-digit mobile number should raise InvalidInputError."""
        with self.assertRaises(InvalidInputError):
            self.owner.top_up_mobile("abcd5678", 50)

    def test_top_up_insufficient_balance(self):
        """Test topping up with an amount greater than balance should raise TransferError."""
        with self.assertRaises(TransferError):
            self.owner.top_up_mobile("12345678", 5000)

    def test_zero_deposit(self):
        """Test depositing zero should raise InvalidInputError."""
        with self.assertRaises(InvalidInputError):
            self.owner.deposit_money(0)

    def test_zero_withdrawal(self):
        """Test withdrawing zero should raise TransferError."""
        with self.assertRaises(TransferError):
            self.owner.money_withdraw(0)

    def test_negative_transfer(self):
        """Test transferring a negative amount should raise TransferError."""
        with self.assertRaises(TransferError):
            self.owner.money_transfer(-100, self.friend)

    def test_invalid_phone_and_amount_combo(self):
        """Test topping up with invalid phone and negative amount."""
        with self.assertRaises(InvalidInputError):
            self.owner.top_up_mobile("abc123", -50)

if __name__ == "__main__":
    unittest.main()

