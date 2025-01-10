class Transaction:
    def __init__(self,type, amount, atm_id,before,after):
        self.__type = type
        self.__amount = amount
        self.__before = before
        self.__after = after
        self.__atm_machine_id = atm_id
        self.__tranfer_to = ''
    def set_tranfer(self, value):
        self.__tranfer_to = value
    @property
    def type(self):
        return self.__type
    @property
    def amount(self):
        return self.__amount
    @property
    def before(self):
        return self.__before
    @property
    def after(self):
        return self.__after
    @property
    def atm_machine_id(self):
        return self.__atm_machine_id
    @property
    def tranfer_to(self):
        return self.__tranfer_to
    
class User:
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__acount_list = []
    
    def add_account(self, account):
        self.__acount_list.append(account)

    @property
    def account_list(self):
        return self.__acount_list
    @property
    def citizen_id(self):
        return self.__citizen_id
    @property
    def name(self):
        return self.__name

class Account:
    def __init__(self, account_number: str, owner: User):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = 0
        self.__atm_card =""
        self.__transaction_list = []
        self.__limit = 40000
        self.__before=''
        self.__after=''

    def append_transaction(self, transaction):
        self.__transaction_list.append(transaction)
    @property
    def before(self):
        return self.__before
    def set_before(self,value):
        self.__before =value
    @property
    def after(self):
        return self.__after
    def set_after(self,value):
        self.__after =value
    @property
    def account_number(self):
        return self.__account_number
    @property
    def owner(self):
        return self.__owner
    @property
    def balance(self):
        return self.__balance
    def get_balance(self):
        return self.__balance
    @property
    def atm_card(self):
        return self.__atm_card
    @property
    def transaction_list(self):
        return self.__transaction_list
    @property
    def limit(self):
        return self.__limit
    
    

    def set_balance(self, balance):
        self.__balance = balance
    def add_atm_card(self, atmcard):
        self.__atm_card=atmcard
    def set_bank(self, bank):
        self.__bank = bank
    def deposit(self, atmmachine,amount):
        if  amount >0:
            self.set_before(self.__balance)
            self.__balance += amount
            self.set_after(self.__balance)
            newtransaction = Transaction("D", amount, atmmachine.machine_id,self.before, self.after)
            self.__transaction_list.append(newtransaction)
            return "success"
        else:
            return "error"
        
    def withdraw(self, atmmachine, amount):
        if self.__balance >  amount >0:
            self.set_before(self.__balance)
            self.__balance -= amount
            self.set_after(self.__balance)
            newtransaction = Transaction("W", amount, atmmachine.machine_id,self.before,self.after)
            self.__transaction_list.append(newtransaction)
            return "success"
        else:
            return "error"
            
    def tranfer(self, atmmachine, destaccount, amount):
        if self == self and self.__balance > amount > 0:
            sum = destaccount.balance + amount
            self.set_before(self.__balance)
            self.__balance -= amount
            self.set_after(self.__balance)
            destaccount.set_balance(sum)
            newtransaction = Transaction("TW", amount, atmmachine.machine_id, self.before, self.after)
            newtransaction.set_tranfer = self.owner
            self.__transaction_list.append(newtransaction)
            newtransaction2 = Transaction("TD", amount, atmmachine.machine_id,self.before,destaccount.balance)
            destaccount.append_transaction(newtransaction2)
            return "success"
        else:
            return "error"


class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str = '1234'):
        self.__card_number=card_number
        self.__account=account
        self.__pin = pin
        self.__vat =''

    @property
    def card_number(self):
        return self.__card_number
    @property
    def account(self):
        return self.__account
    @property
    def pin(self):
        return self.__pin
    @property
    def vat(self):
        return self.__vat

class ATMMachine:
    def __init__(self, machine_id: str, initial_amount: float = 1000000):
        self.__machine_id = machine_id
        self.__balance = initial_amount

    def insert_card(self,cardnumber, pin):
        try:
            for user in bank.user_list:
                for account in user.account_list:
                    if account.atm_card.card_number == cardnumber:
                        if account.atm_card.pin == int(pin):
                            return account
                        else:
                            return "Invalid Pin"
                    
            return "None"
        except:
            return "None"

    def withdraw(self,account, amount):
        if amount > self.balance:
            return "ATM has insufficient funds"
        elif amount > account.limit:
            return "Exceeds daily withdrawal limit of 40,000 baht"
        else:
            status = account.withdraw(self, amount)
            if status == "success":
                self.__balance -= amount
            elif status == "error":
                pass
    
    def deposit(self, account, amount):
        status = account.deposit(self,amount)
        if status == "success":
            self.__balance += amount
        elif status == "error":
            pass

    def tranfer(self,account,amount ,destaccount):
        if amount > account.balance:
            return "Not enough money"
        else:
            status = account.tranfer(self,destaccount, amount)
            if status == "success":
                self.__balance -= amount
            elif status == "error":
                pass
    @property
    def machine_id(self):
        return self.__machine_id
    @property
    def balance(self):
        return self.__balance
        


class Bank:
    def __init__(self):
        self.__user_list=[]
        self.__atm_list=[]
    def add_user(self, user):
        self.__user_list.append(user)
    def add_atm_machine(self, atm):
        self.__atm_list.append(atm)
    def print(self):
        return "Helo"
    @property
    def atm_list(self):
        return self.__atm_list
    @property
    def user_list(self):
        return self.__user_list
    def get_atm(self, value):
        for x in self.__atm_list:
            if value == x.machine_id:
                return x
        return "ATM not found"

##################################################################################

# กำหนดให้ ชื่อคลาส (Class Name) ต้องเป็น Pascal case เช่น BankAccount
# กำหนดให้ ชื่อ instance และ variables ใดๆ ต้องเป็น snake case เช่น my_book
# กำหนดให้ เมื่อรับพารามิเตอร์เข้าใน method ต้องทำ validate data type และกรอบของค่า parameter ก่อนใช้เสมอ
# กำหนดให้ method ที่จัดการข้อมูลใด ต้องอยู่ในคลาสนั้น และพยายามอย่า access attribute นอกคลาส

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, หมายเลข ATM , จำนวนเงิน]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm ={'1001':1000000,'1002':200000}

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance ของผู้ใช้ โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง
# TODO :   ต้อง validate ข้อมุลทุกอย่าง ก่อนสร้าง instance ใดๆ

def init_prog() :
    newbank = Bank()
    accountlist=[]
    for x in user:
        name = user[x][0]
        accnum = user[x][1]
        atmnum= user[x][2]
        accmoney = user[x][3]

        newuser = User(citizen_id=x, name=name)
        newacc = Account(account_number=accnum, owner=newuser)
        newatmcard = ATMCard(atmnum, newacc, 1234)

        newacc.set_balance(accmoney)
        newacc.add_atm_card(newatmcard)
        newacc.set_bank(newbank)
        newuser.add_account(newacc)   
        newbank.add_user(newuser)
    for x in atm:
        newatm = ATMMachine(x,atm[x])
        newbank.add_atm_machine(newatm)
    return newbank

bank = init_prog()

# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
output = bank.atm_list[0].insert_card(bank, bank.user_list[0].account_list[0].atm_card)
output = "{atmnum} {accnum} {status}".format(
atmnum = bank.user_list[0].account_list[0].atm_card.card_number ,
accnum = bank.user_list[0].account_list[0].account_number ,
status = bank.atm_list[0].insert_card(bank, bank.user_list[0].account_list[0].atm_card))
print(output)
print("---------------------------")

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
output = bank.atm_list[1].insert_card(bank, bank.user_list[1].account_list[0].atm_card)
print(output)
output ="Hermione account before test : {amount}".format(amount = bank.user_list[1].account_list[0].balance)
print(output)
output =bank.user_list[1].account_list[0].deposit(bank.atm_list[1], 1000)
print(output)
output ="Hermione account after test : {amount}".format(amount = bank.user_list[1].account_list[0].balance)
print(output)
print("---------------------------")

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
output = bank.atm_list[1].insert_card(bank, bank.user_list[1].account_list[0].atm_card)
print(output)
output ="Hermione account before test : {amount}".format(amount = bank.user_list[1].account_list[0].balance)
print(output)
output =bank.user_list[1].account_list[0].deposit(bank.atm_list[1], -1)
print(output)
output ="Hermione account after test : {amount}".format(amount = bank.user_list[1].account_list[0].balance)
print(output)
print("---------------------------")

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
output = bank.atm_list[1].insert_card(bank, bank.user_list[1].account_list[0].atm_card)
print(output)
output ="Hermione account before test : {amount}".format(amount = bank.user_list[1].account_list[0].balance)
print(output)
output =bank.user_list[1].account_list[0].withdraw(bank.atm_list[1], 500)
print(output)
output ="Hermione account after test : {amount}".format(amount = bank.user_list[1].account_list[0].balance)
print(output)
print("---------------------------")

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
output = bank.atm_list[1].insert_card(bank, bank.user_list[1].account_list[0].atm_card)
print(output)
output ="Hermione account before test : {amount}".format(amount = bank.user_list[1].account_list[0].balance)
print(output)
output =bank.user_list[1].account_list[0].withdraw(bank.atm_list[1], 2000)
print(output)
output ="Hermione account after test : {amount}".format(amount = bank.user_list[1].account_list[0].balance)
print(output)
print("---------------------------")

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
output = bank.atm_list[1].insert_card(bank, bank.user_list[0].account_list[0].atm_card)
print(output)
output ="Hermione account before test : {amount}".format(amount = bank.user_list[1].account_list[0].balance)
output2 ="Harry account before test : {amount}".format(amount = bank.user_list[0].account_list[0].balance)
print(output)
print(output2)
output =bank.user_list[0].account_list[0].tranfer(bank.atm_list[1], bank.user_list[1].account_list[0],10000)
print(output)
output ="Hermione account after test : {amount}".format(amount = bank.user_list[1].account_list[0].balance)
output2 ="Harry account after test : {amount}".format(amount = bank.user_list[0].account_list[0].balance)
print(output)
print(output2)
print("---------------------------")


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : TD-ATM:1002-10000-11500
output = bank.user_list[1].account_list[0].transaction_list[0]
output = "{type}-ATM:{ATM_ID}-{before}-{after}".format(
    type = bank.user_list[1].account_list[0].transaction_list[0].type ,
    ATM_ID = bank.user_list[1].account_list[0].transaction_list[0].atm_machine_id ,
    before =  bank.user_list[1].account_list[0].transaction_list[0].before,
    after =  bank.user_list[1].account_list[0].transaction_list[0].after,
)
for x in bank.user_list[1].account_list[0].transaction_list:
    output = "{type}-ATM:{ATM_ID}-{before}-{after}".format(
        type = x.type ,
        ATM_ID = x.atm_machine_id ,
        before =  x.amount,
        after =  x.after,
    )

    print(output)
print("---------------------------")

# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
atm_machine = bank.get_atm('1001')
test_result = atm_machine.insert_card('12345', '9999')  # ใส่ PIN ผิด
print(test_result)
print("---------------------------")
# ผลที่คาดหวัง
# Invalid PIN

# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)
atm_machine = bank.get_atm('1001')
account = atm_machine.insert_card('12345', '1234')  # PIN ถูกต้อง
harry_balance_before = account.balance
print(harry_balance_before)

print(f"Harry account before test: {harry_balance_before}")
print("Attempting to withdraw 45,000 baht...")
result = atm_machine.withdraw(account, 45000)
print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
print(f"Actual result: {result}")
print(f"Harry account after test: {account.get_balance()}")
print("-------------------------")

# Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ
atm_machine = bank.get_atm('1002')  # สมมติว่าตู้ที่ 2 มีเงินเหลือ 200,000 บาท
account = atm_machine.insert_card('12345', '1234')
print("Test case #10 : Test withdrawal when ATM has insufficient funds")
print(f"ATM machine balance before: {atm_machine.balance}")
print("Attempting to withdraw 250,000 baht...")
result = atm_machine.withdraw(account, 250000)
print(f"Expected result: ATM has insufficient funds")
print(f"Actual result: {result}")
print(f"ATM machine balance after: {atm_machine.balance}")
print("-------------------------")



