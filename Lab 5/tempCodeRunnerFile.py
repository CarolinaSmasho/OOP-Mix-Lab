def test_fixed_withdraw_before_maturity(self): # 8. ทดสอบการถอนเงินก่อนวันครบกำหนด 
        """Test withdrawal before maturity period with reduced interest"""
        from datetime import datetime, timedelta
        
        # Initial deposit
        initial_deposit = 100000
        fixed_account = FixedAccount("FIX003", self.tony, 12)  # 12 months period
        fixed_account.deposit("COUNTER:001", initial_deposit)
        
        # Simulate time passing (6 months)
        # Mock the deposit_date to be 6 months ago
        fixed_account._FixedAccount__deposit_date = datetime.now() - timedelta(days=180)
        
        # Try to withdraw
        withdraw_amount = 50000
        result = fixed_account.withdraw("COUNTER:001", withdraw_amount)
        
        # Verify withdrawal success
        self.assertEqual(result, "Success", "Withdrawal should be successful")
        
        # Check if reduced interest was applied
        transactions = fixed_account.list_transaction()
        interest_transaction = [t for t in transactions if str(t).startswith("I-")]
        self.assertGreater(len(interest_transaction), 0, 
                        "Interest transaction should exist")
        
        # Verify reduced interest rate (should be around 1.25% for 6 months)
        # Base rate is 2.5% per year, so 6 months should be approximately half
        expected_interest = initial_deposit * 0.0125  # Approximately half of 2.5%
        actual_interest = float(str(interest_transaction[-1]).split("-")[2])
        self.assertAlmostEqual(actual_interest, expected_interest, delta=1, 
                            msg="Interest should be calculated at reduced rate")