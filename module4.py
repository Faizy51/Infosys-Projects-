 

import cx_Oracle

conn = cx_Oracle.connect('mod3/1234')
c = conn.cursor()





 
"""*****************************************************************************
                            CLASS USED IN PROJECT
*****************************************************************************"""
''' 
class account(object):
    def __init__(s):
        s.acno=0
        s.name=""
        s.deposit=0
        s.type=""
 
    def create_account(s):  #function to get data from user
        name=raw_input("\n\nEnter the name of the account holder: ")
        s.name=name.capitalize()
        type=raw_input("\nEnter type of the account (C/S): ")
        s.type=type.upper()
        s.deposit=input("\nEnter initial amount\n(>=500 for Saving and >=1000 for Current): ")
         
    def show_account(s):    #function to show data on screen
        print "\nAccount No. :", s.acno
        print "\nAccount holder name: ", s.name
        print "\nType of account", s.type
        print "\nBalance amount: ", s.deposit
 
    def modify(s):          #function to get new data from user
        print "\nAccount No. : ", s.acno
        s.name=raw_input("\n\nEnter the name of account holder: ")
        type=raw_input("\n\nEnter type of account (C/S): ")
        s.type=type.upper()
        s.deposit=input("\nEnter the amount: ")
 
    def dep(s,x):           #function to accept amount and add to balance
        s.deposit+=x
 
    def draw(s,x):          #function to accept amount and subtract from balance amount
        s.deposit-=x
 
    def report(s):          #function to show data in tabular format
        print "%-10s"%s.acno,"%-20s"%s.name,"%-10s"%s.type,"%-6s"%s.deposit
 
    def retacno(s):         #function to return account number
        return s.acno
 
    def retdeposit(s):      #function to return balance amount 
        return s.deposit
 
    def rettype(s):         #function to return type of account
        return s.type
 
''' 
"""*****************************************************************************
                    FUNCTION TO GENERATE ACCOUNT NUMBER
*****************************************************************************"""
 
def gen_acno():
    try:
        inFile=open("account2.dat","rb")
        outFile=open("text2.dat","wb")
        n=inFile.read()
        n=int(n)
        while True:
            n+=1
            outFile.write(str(n))
            inFile.close()
            outFile.close()
            os.remove("account2.dat")
            os.rename("text2.dat","account2.dat")
            yield n
             
    except IOError:
        print "I/O error occured"
 
 
"""*****************************************************************************
                    FUNCTION TO WRITE RECORD IN BINARY FILE
*****************************************************************************"""
 
def write_account():
    try:
        ac=account()
        outFile=open("account.dat","ab")
        ch=gen_acno()
        ac.acno=ch.next()
        ac.create_account()
        pickle.dump(ac,outFile)
        outFile.close()
        print "\n\n Account Created Successfully"
        print "\n\n YOUR ACCOUNT NUMBER IS: ",ac.retacno()
    except:
        pass
 
 
"""*****************************************************************************
                FUNCTION TO DISPLAY ACCOUNT DETAILS GIVEN BY USER
*****************************************************************************"""
 
def display_sp(n):
    flag=0
    try:
        sql = "select balance from account where accno=:num"
        res = c.execute(sql,{'num':n})
        cur_bal = res.fetchall()
        print("BALANCE DETAILS\n")
        print("\n")
        print(n+"\t"+cur_bal)
                 
    except Exception:
        print ("\n\nException occured")
 
 
"""*****************************************************************************
                        FUNCTION TO MODIFY RECORD OF FILE
*****************************************************************************"""
 
def modify_account(n):
    found=0
    try:
        op = input("\n\nDo u want to change email?(y/n)")
        if op=='n':
            break
        elif op=='y':
            em = input("\nEnter new Email Id : ")
            sql = "update customers set email=:email where accno=:num"
            res = c.execute(sql,{'email':em,'num':n})
            if !res:
                print("\ncouldn't update")
            else:
                print ("\n\n\tRecord Updated")
        else:
            print("\nInvalid i/p")

    except Exception:
        print ("\nException occurred")


 
 
"""*****************************************************************************
                    FUNCTION TO DELETE RECORD OF FILE
*****************************************************************************"""
 
def delete_account(n):
    found=0
 
    try:
        sql = "delete from account,customers where accno=:num"
        res = c.execute(sql,{'num':n})
        if(!res):
            print("\ncouldn't delete")
        else:
            print ("\n\n\tRecord Deleted ..")
        found=1

    except IOError:
        if found==0:
            print "\n\nRecord Not Found"
        print ("\n\nException occurred")
 

"""*****************************************************************************
                    FUNCTION TO DISPLAY ALL ACCOUNT DETAILS
*****************************************************************************"""
 
def display_all():
    print ("\n\n\tACCOUNT HOLDER LIST\n\n")
    print (60*"=")
    print ("%-10s"%"A/C No.","%-20s"%"Name","%-10s"%"email")
    print (60*"=","\n")
    try:
        res = c.excecute("select *from customers")
        for row in res:
            print(row[4]+"\t"+row[2]+"\t"+row[3]+"\n")
        names = res.fetchall()
        print(names)
                  
    except Exception:
        print ("\nException occurred")
 
 
"""*****************************************************************************
            FUNCTION TO DEPOSIT/WITHDRAW AMOUNT FOR GIVEN ACCOUNT
*****************************************************************************"""
 
def deposit_withdraw(n,option):
    found=0
 
    try:
        sql = "SELECT distinct accno from customers"
        c.execute(sql)
        for row in cur.fetchone():
            if row[4] == n:
                cust_name = row[2]
                break;
        if cust_name == NULL:
            print("\nAccount number invalid")
            return
        if option==1:
            am = input("\nEnter amount to be deposited")
            sql = "select balance from account where accno=:num"
            res = c.execute(sql,{'num':n})
            cur_bal = res.fetchall()
            cur_bal+=am
            sql = 'update account set balance=:num where accno=:no'
            res = c.execute(sql,{'num':cur_bal,'no':n})
            print("\nYour current balance is "+cur_bal+"\n")
        elif option==2:
            am = input("\nEnter amount to be withdrawn")
            sql = "select balance from account where accno=:num"
            res = c.execute(sql,{'num':n})
            cur_bal = res.fetchall()
            if cur_bal-am >= 500:
                cur_bal-=am
                sql = 'update account set balance=:num where accno=:no'
                res = c.execute(sql,{'num':cur_bal,'no':n})
            else:
                print("\nInsufficient Balance")
            print("\nYour current balance is "+cur_bal+"\n")
        else:
            print("\ninvalid option")

        
    except Exception, e:
        logging.warning('DB exception: %s' % e)
        self.set_status(500)
        return


"""*****************************************************************************
                        INTRODUCTORY FUNCTION
*****************************************************************************"""


def transfer_amount(f,t,a):
    sql = 'select balance from account where accno=:num'
    res1 = c.execute(sql,{'num':f})
    sql = 'select balance from account where accno=:num'
    res2 = c.execute(sql,{'num':t})
    if(res1-a)>=500:
        res1-=a
        res2+=a
    else:
        print("\n\nInsufficient funds")
    sql = 'update account set balance=:bal where accno=:num'
    res3 = c.execute(sql,{'bal':res1,'num':f})
    sql = 'update account set balance=:bal where accno=:num'
    res4 = c.execute(sql,{'bal':res2,'num':t})
    if !res3 and !res4:
        print("\ncouldn't transfer")

 
 
"""*****************************************************************************
                        INTRODUCTORY FUNCTION
*****************************************************************************"""
 
def intro():
    print "\n\n\tBANK"
    print "\n\tMANAGEMENT"
    print "\n\n\nMADE BY : FAIZYY"
    print "\nCOLLEGE : BNMIT"
 

 
"""*****************************************************************************
                        SIGN IN FUNCTION
*****************************************************************************"""
def sign_in():
    name = input("Enter your name: ")
    pwd = input("Enter your password")
    cur = conn.cursor()
    cur.execute("select *from customers")
    for row in cur.fetchone():
        if row[2] == name and row[1] == pwd:
            print("sign in successful")
            flag = 1
    if flag == 1:
        while True:
            print 3*"\n",60*"="
            print ("""SUB MENU
         
            1. Deposit Amount
            2. Withdraw Amount
            3. Balance Enquiry
            4. All Account Holder List
            5. Close An Account
            6. Modify An Account
            7. Transfer Money
            8. Exit
            """)
                 
            try:
                ch=input("Enter Your Choice(1~8): ")
                 
                if ch==1:
                    num=input("\n\nEnter Account Number: ")
                    deposit_withdraw(num,1)
         
                elif ch==2:
                    num=input("\n\nEnter Account Number: ")
                    deposit_withdraw(num,2)

                elif ch==3:
                    num=input("\n\nEnter Account Number: ")
                    display_sp(num)
         
                elif ch==4:
                    display_all()

                elif ch==5:
                    num=input("\n\nEnter Account Number: ")
                    delete_account(num)

                elif ch==6:
                    num=input("\n\nEnter Account Number: ")
                    modify_account(num)

                elif ch==7:
                    from_ac=input("\n\nEnter FROM Account Number: ")
                    to_ac = input("\n\nEnter TO Account Number: ")
                    amount = input("\n\nEnter amount to be transferred: ")
                    transfer_amount(from_ac,to_ac,amount)

                elif ch==8:
                    break;

                else:
                    print ("Input correcr choice...(1-8)")

            except NameError:
                print ("Input correct choice...(1-8)")
        
                


 
"""*****************************************************************************
                        THE MAIN FUNCTION OF PROGRAM
*****************************************************************************"""
 
intro()


while True:
    print 3*"\n",60*"="
    print """MAIN MENU
 
    1. Sign up
    2. Sign in
    3. Quit
    """
    try:
        ch=input("Enter Your Choice(1~3): ")
        if ch==1:
            write_account()
        elif ch==2:
            sign_in()
        elif ch==3:
            break
        else:
            print ("Input correcr choice...(1-3)")
            
''' 
while True:
    print 3*"\n",60*"="
    print """MAIN MENU
 
    1. New Account
    2. Deposit Amount
    3. Withdraw Amount
    4. Balance Enquiry
    5. All Account Holder List
    6. Close An Account
    7. Modify An Account
    8. Exit
    """
 
    try:
        ch=input("Enter Your Choice(1~8): ")
        if ch==1:
            write_account()
         
        elif ch==2:
            num=input("\n\nEnter Account Number: ")
            deposit_withdraw(num,1)
 
        elif ch==3:
            num=input("\n\nEnter Account Number: ")
            deposit_withdraw(num,2)
 
        elif ch==4:
            num=input("\n\nEnter Account Number: ")
            display_sp(num)
 
        elif ch==5:
            display_all()
 
        elif ch==6:
            num=input("\n\nEnter Account Number: ")
            delete_account(num)
         
        elif ch==7:
            num=input("\n\nEnter Account Number: ")
            modify_account(num)
 
        elif ch==8:
            break
 
        else:
            print "Input correcr choice...(1-8)"
 
    except NameError:
        print "Input correct choice...(1-8)"
 
 '''
c.close()
conn.close()

input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")
 
"""*****************************************************************************
                END OF PROJECT
*****************************************************************************"""
