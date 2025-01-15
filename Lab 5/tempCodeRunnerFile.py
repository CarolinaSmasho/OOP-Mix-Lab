hor_account_merchant_payment(self): # 18. ทดสอบการชำระเงินผ่านบัญชีของ Thor ผ่าน EDC (ไม่มีเงินคืน)
        """Test merchant payment through EDC for Thor's account (no cashback)"""
        # Get EDC machine
        edc = self.bank.search_edc_machine("EDC001")
        self.assertIsNotNone(edc, "EDC machine should exist")
        
        # Initial balances
        merchant_initial = self.thanos_current.balance
        thor_initial = self.thor_savings.balance
        payment_amount = 1000
        
        # Process payment
        # First verify card
        card_verification = edc.swipe_card(self.thor_travel_card, "9012")
        self.assertEqual(card_verification, "Success", "Card verification should succeed")
        
        # Then make payment
        payment_result = edc.pay(self.thor_travel_card, payment_amount)
        
        # Verify payment success
        self.assertEqual(payment_result, "Success", "Payment should be successful")
        
        # Check merchant account balance
        expected_merchant_balance = merchant_initial + payment_amount
        self.assertEqual(self.thanos_current.balance, expected_merchant_balance,
                        "Merchant balance should increase by payment amount")
        
        # Check Thor's account balance - should not include cashback
        expected_thor_balance = thor_initial - payment_amount
        self.assertEqual(self.thor_savings.balance, expected_thor_balance,
                        "Thor's balance should