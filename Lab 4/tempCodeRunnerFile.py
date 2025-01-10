
print(f"ATM machine balance before: {atm_machine.get_balance()}")
print("Attempting to withdraw 250,000 baht...")
result = atm_machine.withdraw(account, 250000)
print(f"Expected result: ATM has insufficient funds")
print(f"Actual result: {result}")
print(f"ATM machine balance after: {atm_machine.get_balance()}")
print("-------------------------")