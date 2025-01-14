classDiagram
    Bank o-- User
    Bank o-- ATMMachine
    
    Bank <-- TransactionChannel 

    User o-- Account
    Account o-- Transaction  

    ATMMachine --> ATMCard
    
    

    
    Counter --|> TransactionChannel
    ATMMachine --|> TransactionChannel
    EDC --|>TransactionChannel

    Account <|-- SavingAccount
    Account <|-- FixedAccount
    Account <|-- CurrentAccount

    Bank o -- EDC
    
    Card <|-- ATMCard
    Card <|-- Debit
    Debit <|-- TravelCard
    Debit <|-- ShoppingCard
    
    class Bank{
        -List~User~ user_list
        -List device_list

    }

    class User{
        -citizen_id
        -name
        -account_list

    }

    class Transaction{
        -type
        -amount
        -before
        -after
        -atm_machine_id
        -tranfer_to
    }

    class Account{
        -before
        -after
        -account_number
        -owner
        -balance
        -transaction_list
        -interest
        -acc_type

        -deposit()
        -withdraw()
        -tranfer()
    }


    class SavingAccount{
        -atm_card
        -debit_card
    }
    class FixedAccount{
        -atleast_deposit_time
        -deposit_date

        -calculate_interest()
    }
    class CurrentAccount{
        -calculate_interest()
    }

    class ATMCard{
        -card_number
        -account
        -pin
        -vat
    }

    class ATMMachine{
        -machine_id
        -balance
        -limit_account

        -insert_card()
        -withdraw()
        -deposit()
        -tranfer()
    }

    class EDC{
        -edc_id
        -owner_current_account
        -owner_name
    }

    class Counter{

    }


    class TransactionChannel{

    }


    