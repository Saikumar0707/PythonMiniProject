
'''
Banking Management System Mini Project
User has to enter below information to login
    User Name / Accouht Holder name
    Account number as the key used in Dictonary
    Password stored in the nested Dictonary as metadata

# User has 4 chance or options to do banking:
    Bank Balance
    Credit amount
    Debit amount
    Mini Statement
'''
# Data set used
Accountholders =  ["Sai","Kumar","Kiran","Sagar"]

Usersdata = {1001:{1001:"Sai","Metadata":{"Password":"Sai123","BankBal":500000,"Stmt":{}}},
        1002:{1002:"Kumar","Metadata":{"Password":"Kumar123","BankBal":500000,"Stmt":{}}},
        1003:{1003:"Kiran","Metadata":{"Password":"Kiran123","BankBal":500000,"Stmt":{}}},
        1004:{1004:"Sagar","Metadata":{"Password":"Sagar123","BankBal":500000},"Stmt":{}}}

Username= input("Enter user Name: ")

if(Username in Accountholders):
    print("Welcome to My Bank " + Username + " !!")
    #print(Usersdata)

    accountnumber = int(input("Enter Account Number for verification: "))
 
    userdata_keys = list(Usersdata.keys())
    #print(userdata_keys)

    if(accountnumber in userdata_keys):
        print("Thank you for the Confirmation !")
        
        userpassword = str(input("Please Enter Password to Personal Banking: "))
        
        if(Usersdata[accountnumber]["Metadata"]["Password"] == userpassword): # check for password
            print("You have successfully logged into My Bank")
            
            for choices in range(4): # User can access & check all 4 options with one time login
                userselection = input("Please select transaction \n"
                + "1. Bank Balance \n"
                + "2. Credit/Deposit Amount \n"
                + "3. Debit/Withdraw Amount \n"
                + "4. Mini Statement \n"
                + "5. Do Nothing  :")
                
                if(len(userselection)>0 and int(userselection)<=5):
                    userselection = int(userselection)
                    
                    if(userselection == 5): # in case user dont have to access metadata
                        print("Thank you for banking with us")
                        break ## Break if user dont want to do any banking action
                    
                    elif(userselection == 1): # Bank Balance
                            print("Your Bank Balance is "+ str(Usersdata[accountnumber]["Metadata"]["BankBal"]))
                    
                    elif(userselection == 2): # Credit
                            creditamount = int(input("Enter amount to credit/deposit: "))
                            updatedcreditamount = Usersdata[accountnumber]["Metadata"]["BankBal"] + creditamount
                            Usersdata[accountnumber]["Metadata"]["BankBal"] = updatedcreditamount
                            #below condition is for statement
                            #Usersdata[accountnumber]["Metadata"]["Stmt"] = {"Credit":creditamount}
                            Usersdata[accountnumber]["Metadata"]["Stmt"].update({"Credit":creditamount})
                            Usersdata = Usersdata
                            #print(creditamount)
                            print("Amount credited "+str(creditamount)+" Your New Bank Balance is "+ str(Usersdata[accountnumber]["Metadata"]["BankBal"]))
                            #print(Usersdata)
                    
                    elif(userselection == 3): # Debit
                            debitamount = int(input("Enter amount to Debit/Withdraw: "))
                            updateddebitamount = Usersdata[accountnumber]["Metadata"]["BankBal"] - debitamount
                            Usersdata[accountnumber]["Metadata"]["BankBal"] = updateddebitamount
                            #below condition is for statement
                            Usersdata[accountnumber]["Metadata"]["Stmt"].update({"Debit":debitamount})
                            Usersdata = Usersdata
                            print(debitamount)
                            print("Amount debited "+str(debitamount)+" Your New Bank Balance is "+ str(Usersdata[accountnumber]["Metadata"]["BankBal"]))
                            #print(Usersdata)
                    
                    elif(userselection == 4): # Statement
                            print(Usersdata)
                            Usersdata = Usersdata
                            print("Your last two transactions \n "+ str(Usersdata[accountnumber]["Metadata"]["Stmt"]))
                
                                
                else:
                    print("Select a valid option") # if user selects a invalid option
        
        else:
            print("Please retry with correct Password") # if user enter wrong password
    
    else:
        print("Please retry with correct account number") # if user enter wrong account number

else:
    print("Please retry with correct Account Holder Name") # if user enter wrong user name
