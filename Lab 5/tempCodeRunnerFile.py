aw_over_limit(self): # 3. ทดสอบการถอนเงินเกินจำนวนที่กำหนด
        # Initial balance check
        initial_balance = self.steve_savings.balance
        
        # Attempt withdrawal
        withdraw_amount = 60000  # Over 50,000 limit
        result = self.atm1.insert_card(self.steve_shopping_card, "5678")
        
        # Verify card insertion
        self.assertNotEqual(result, "Error", "Card verification should succeed")
        
        # Perform withdrawal and verify result
        withdraw_result = self.atm1.withdraw(result, withdraw_amount)
        self.assertIn("Error", withdraw_result, 
                     "Should return error for withdrawal over limit")
        
        # Verify balance unchanged
        self.assertEqual(self.steve_savings.balance, initial_balance, 
                        "Balance shoul