def test_fixed_withdraw_at_maturity(self): # 11. ทดสอบการถอนเงินในวันครบกำหนด
    #     """Test withdrawal at maturity period with full interest"""
    #     from datetime import datetime, timedelta
        
    #     # Initial deposit
    #     initial_deposit = 100000
    #     fixed_account = FixedAccount("FIX006", self.tony, 12)  # 12 months period
    #     fixed_account.deposit("COUNTER:001", initial_deposit)
        
    #     # Simulate time passing (12 months)
    #     # Mock the deposit_date to be 12 months ago
    #     fixed_account._FixedAccount__deposit_date = datetime.now() - timedelta(days=365)
        
    #     # Try to withdraw
    #     withdraw_amount = initial_deposit
    #     # FIXME: 
    #     result = fixed_account.withdraw("COUNTER:001", withdraw_amount)
        
    #     # Verify withdrawal success
    #     self.assertEqual(result, "Success", "Withdrawal should be successful")
        
    #     # Check if full interest was applied
    #     transactions = fixed_account.list_transaction()
    #     interest_transaction = [t for t in transactions if str(t).startswith("I-")]
    #     self.assertGreater(len(interest_transaction), 0, 
    #                     "Interest transaction should exist")
        
    #     # Verify full interest rate (2.5% for 12 months)
    #     expected_interest = initial_deposit * 0.025  # Full 2.5% annual rate
    #     actual_interest = float(str(interest_transaction[-1]).split("-")[2])
    #     self.assertAlmostEqual(actual_interest, expected_interest, delta=1, 
    #                         msg="Interest should be calculated at full rate")
        
    #     # Verify final balance after interest and withdrawal
    #     expected_final_balance = initial_deposit + expected_interest - withdraw_amount
    #     self.assertAlmostEqual(fixed_account.balance, expected_final_balance, delta=1,
    #                         msg="Final balance should refle