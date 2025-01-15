nt_large_withdrawal(self): # 13. ทดสอบการถอนเงินในจำนวนมากในบัญชีกระแสรายวัน
        """Test large withdrawal from current account (no limit unlike savings)"""
        # Initial setup
        initial_balance = self.thanos_current.balance
        large_withdrawal = 100000  # Amount larger than savings account limit
        
        # Perform withdrawal via counter
        result = self.counter.withdraw(
            self.thanos_current,
            large_withdrawal,
            self.thanos_current.account_no,
            self.thanos.citizen_id
        )
        
        # Verify withdrawal success
        self.assertEqual(result, "Success", 
                        "Large withdrawal should be successful for current account")
        
        # Check balance update
        expected_balance = initial_balance - large_withdrawal
        self.assertEqual(self.thanos_current.balance, expected_balance,
                        f"Balance should be {expected_balance}")
        
        # Verify transaction record
        transactions = self.thanos_current.list_transaction()
        latest_transaction = transactions[-1]
        self.assertIn("W-COUNTER:", str(latest_transaction),
                    "Transaction should be recorded as counter w