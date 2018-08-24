import sys
import re
import sqlite3
import datetime
conn = sqlite3.connect('atm.db',timeout=10)
cr = conn.cursor()

now = datetime.datetime.now()
from os import system, name
def clear():
 
    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')


n=now.strftime("%Y-%m-%d %H:%M:%S")


x=1
y=1

conn.execute('''INSERT INTO customerdetails VALUES(158611, 411,788000,'06-07-2018 22:21:04')''')
conn.commit()
conn.execute('''INSERT INTO cust VALUES(1234, 555,78000,'06-07-2018 22:21:04')''')
conn.commit()

print ("        ****** WELL COME TO BANK ******     ")
print ("=============================================")
print ("Please insert your card")
card_no = int(input("enter the card no."))
d=cr.execute('''select cardno FROM customerdetails''')
#fetch = cr.fetchall()
for i in d:
    if card_no ==i[1]:
        print('card accepted')
    else:
        print('rej')
    pin_no = int(input("Please enter your pin number to the keypad: "))
    print ("==============================================")
    #p = [7894,1230,4588]
    cr.execute('''select pinno FROM customerdetails''')
    fetch1 = cr.fetchone()
    if pin_no == fetch1[0]:
        print('welcome user')

        while x==1:
            print("     \nSELECT TRANSACTION    \n")
            print("1. Deposit ")
            print("2. Transfer ")
            print("3. Pin Change ")
            print("4. Cash Withdraw")
            print("5. Balance Inquiry ")
            print("6. card statement ")
            print("7. Exit ")
            ch =int(input("Enter your choose: "))
            if ch==1:
                while y==1:
                    print("a : ADD TO YOUR SAVING ACCOUNT    ")
                    print("b : BACK TO PREVIOUS")
        
                    m=input("Enter your choice: ")
                    if m=='a':
                        print("------ YOU CAN DEPOSITE UPTO 10000rs. ONLY -----")
                        p=int(input(" TO CONFIRM DEPOSIT ENTER PIN   " ))
                        add_baln = int(input("enter the amount you want to deposit  "))
                        if add_baln <=10000:
                            cr.execute('''select balance FROM customerdetails''')
                            fetch3 = cr.fetchone()
                            deposit = add_baln + fetch3[0]
                            newb=deposit
                            cr.execute('''select pinno FROM customerdetails''')
                            f = cr.fetchone()
                            if p == fetch1[0]:
                                print('DEPOSIT SUCCESSFUL')
                            else:
                                print('enter valid pin')
                # cr.execute('''update customerdetails set balance = ? where pinno = ?''',(newb,f))

                            print('YOUR ACCOUNT BALANCE \n AFTER DEPOSITE',deposit)
                            cr.execute('''update customerdetails set balance = ?,date = ? where pinno = ?''',(newb,n,p))
                            conn.commit()
                
                        else:
                            print(" give a valid amount")
                    
                    

                        
                        
                        if m=='b':
                            sys.exit(1)
                
                
                        m=input("would you want to cont then press y: ")
                        if m=='y':
                            continue
                        else:
                            break  
                
                clear()
                continue

            if ch==2:
                #to knw from where to transfer
                

                while y==1:
                    print("ac : account base transfer")
                    print("cc : card to card")
                
                    m=input("Enter your choice: ")
                    if m=='ac':
                        p=int(input(" TO CONFIRM TRANSACTION account no   " ))
                        cr.execute('''select cardno FROM customerdetails''')
                        f = cr.fetchone()
                        if p == f[0]:
                            print('........')
                        else:
                            print("error")
                        cr.execute('''select balance FROM customerdetails''')
                        fetch2 = cr.fetchone()
                
                        g=int(input("Enter the amount to TRANSFER: "))
                        if g <= fetch2[0]:
                            print('wait transaction is loading')
                            up= cr.execute('''update customerdetails set balance = balance-?,date =? where cardno = ?''',(g,n,p))
                            conn.commit()
                            print("successful, check your balance")
                        else:
                            print("insufficient amount")
                        a=int(input("  ENTER ACC_no TO WHOM TRANSFER  " ))

                        cr.execute('''select cardno FROM cust''')
                        i = cr.fetchone()
                        if a == i[0]:
                            print('welcome')
                            l=int(input("Enter the confirm amount to transfer: "))
                            cr.execute('''select balance FROM cust''')
                            fetch3 = cr.fetchone()
                            if l <= fetch3[0]:
                                deposit = l + fetch3[0] 
                                newb=deposit
                                cr.execute('''update cust set balance = ?,date =? where cardno = ?''',(newb,n,l))
                                conn.commit()
                            else:
                                print("rrr")  
                        else:
                            print("error")
                        b=input("WANT TO CHECK YOUR REMAINING BALANCE ? (press y)   ")
                        if b=='y':
                            cr.execute('''select balance FROM customerdetails''')
                            fetch2 = cr.fetchone()
                            balance = fetch2[0]
                            print("BALANCE \n Rs",balance)
                            
                        else:
                            print("rrr")
                        
                    
                        print("\nsuccessful\n")
                    if m=='cc':
                        p=int(input(" TO CONFIRM TRANSACTION ENTER CARD_NO   " ))
                        cr.execute('''select cardno FROM customerdetails''')
                        f = cr.fetchone()
                        if p == f[0]:
                            print('........')
                        else:
                            print("error")
                        cr.execute('''select balance FROM customerdetails''')
                        fetch4 = cr.fetchone()
                
                        g=int(input("Enter the amount to TRANSFER: "))
                        if g <= fetch4[0]:
                            print('wait transaction is loading')
                            up= cr.execute('''update customerdetails set balance = balance-?,date =? where cardno = ?''',(g,n,p))
                            conn.commit()
                            print("successful, check your balance")
                        else:
                            print("insufficient amount")
                        a=int(input("  ENTER CARD_NO TO WHOM TRANSFER  " ))

                        cr.execute('''select cardno FROM cust''')
                        i = cr.fetchone()
                        if a == i[0]:
                            print('welcome')
                            l=int(input("Enter the confirm amount to transfer: "))
                            cr.execute('''select balance FROM cust''')
                            fetch5 = cr.fetchone()
                            if l <= fetch5[0]:
                                deposit = l + fetch5[0] 
                                newb=deposit
                                cr.execute('''update cust set balance = ?,date =? where cardno = ?''',(newb,n,l))
                                conn.commit()
                            else:
                                print("rrr")  
                        else:
                            print("error")
                        b=input("WANT TO CHECK YOUR REMAINING BALANCE ? (press y)   ")
                        if b=='y':
                            cr.execute('''select balance FROM customerdetails''')
                            fetch4 = cr.fetchone()
                            balance = fetch4[0]
                            print("BALANCE \n Rs",balance)
                        
                    

                    m=input("Press 'y' to cont: ")
                    if m=='y':
                        continue
                    else:
                        break  
                clear()
                continue

            if ch==3:
                while y==1:
                    print("a: ADD New Pin Number")
                    print("b: exit")
                    ch=input("enter your choice  ")
                    if ch=='a':
                        crd = int(input(" enter the card no. to confirm change  "))
                        cr.execute('''select cardno FROM customerdetails''')
                        fetch = cr.fetchone()
                        if crd ==fetch[0]:
                            print('card accepted')
                        else:
                            print('card rejected')

                        p=int(input("enter old pin no :"))
                        cr.execute('''select pinno FROM customerdetails''')
                        f = cr.fetchone()
                        if p == fetch1[0]:
                            m=int(input("enter NEW PIN NO :"))
                            cr.execute('''update customerdetails set pinno = ? where cardno = ?''',(m,crd))
                            conn.commit()
                            print("update successfully")
                        else:
                            break

                    m=input("Press 'y' to cont: ")
                    if m=='y':
                        continue
                    else:
                        break  
        
                clear()
                continue

            if ch==4:
                while y==1:
                    print("chose option for cash withdraw")
                    print("a : saving acc")
                    print("b : BACK TO PREVIOUS")
                
                    m=input("Enter your choice: ")
                    if m=='a':
                        p=int(input(" TO CONFIRM WITHDRAW ENTER PIN   " ))
                        cr.execute('''select pinno FROM customerdetails''')
                        f = cr.fetchone()
                        if p == fetch1[0]:
                            print('welcome')
                        else:
                            break
                # cr.execute('''select pinno FROM customerdetails''')
                
                        cr.execute('''select balance FROM customerdetails''')
                        fetch2 = cr.fetchone()
                
                        g=int(input("Enter the amount to withdraw: "))
                        if g <= fetch2[0]:
                            print('wait transaction is loading')
                            up= cr.execute('''update customerdetails set balance = balance-?,date = ? where pinno = ?''',(g,n,p))
                            conn.commit()
                            print("successful, check your balance")

                        else:
                            print("insufficient amount")
                        
                            
                    
                    if m=='b':
                        sys.exit(1)
                    
                    m=input("Press 'y' to cont: ")
                    if m=='y':
                        continue
                    else:
                        break  
                clear()
                continue

            if ch==5:
                while y==1:
                    print("\nYOUR Account Balance Details............ \n")
                    print("a :BALANCE DETAILS")
                    print("b : BACK TO PREVIOUS")
                    m=input("enter your choice  ")
                    if m=='a':
                        print("****************LOADING*********")
                        cr.execute('''select balance FROM customerdetails''')
                        fetch2 = cr.fetchone()
                        balance = fetch2[0]
                        print("BALANCE \n Rs",balance)

                    if m=='b':
                        sys.exit(1)
                    #     balance = current_ac[0]
                    #     print("BALANCE in your current accnt \n Rs",balance)
                    #     # i=0
                    #     # while i < len(current_ac):
                    #     #     print(current_ac[i],end=" ")
                    #     #     i+=1

                    m=input("\nPress 'y' to cont: ")
                    if m=='y':
                        continue
                    else:
                        break  

                clear()
                continue



            if ch==6:
                while y==1:
                    print("\nYOUR Account  Details............ \n")
                    print("a : ACCOUNT DETAILS")
                    print("b : BACK")
                    m=input("enter your choice  ")
                    if m=='a':
                        print("****************LOADING*********")
                        ob=cr.execute('''select * FROM customerdetails''')
                        # fetch2 = cr.fetchone()
                        # d = fetch2[0]
                        # print("YOUR ACCOUNT DETAILS IS HERE",d)
                        # rows = cr.fetchall()
        
                        # for row in rows:
                        #     print(row)
                        print(type(ob))
                        for mydata in ob:
                            print('cardno:',mydata[0],' ','pinno:',mydata[1],' ','balance:',mydata[2],'  date:',mydata[3])

                    if m=='b':
                        sys.exit(1)
                    m=input("\nPress 'y' to cont: ")
                    if m=='y':
                        continue
                    else:
                        break
                    

                clear()
                continue
            if ch==7:
                sys.exit(1)

    else:
        print('enter valid pin')

# pin_no = int(input("Please enter your pin number to the keypad: "))
# print ("==============================================")
# #p = [7894,1230,4588]
# cr.execute('''select pinno FROM customerdetails''')
# fetch1 = cr.fetchone()
# if pin_no == fetch1[0]:
#     print('welcome user')
# else:
#     print('enter valid pin')
