import smtplib
menu = True
while menu:
    print("""\u001b[32m

                        _ __                                                 
  ___  ____ ___  ____ _(_) /  _________  ____ _____ ___  ____ ___  ___  _____
 / _ \/ __ `__ \/ __ `/ / /  / ___/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/
/  __/ / / / / / /_/ / / /  (__  ) /_/ / /_/ / / / / / / / / / / /  __/ /    
\___/_/ /_/ /_/\__,_/_/_/  /____/ .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/     
                               /_/                                           
  \u001b[31m  1. gmail
    2. yahoo
    3. outlook
    4. icloud
    5. AOL
    0. exit
    """)
    menu = input("select option: ")
    #gmail server
    if menu =="1":
        strt = True
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        # authenication
        acc = input("your account name: ")
        password = input("password: ")
        contact = input("email to send to: ")
        msg = input("your message: ")

        server.login(acc, password)
        # spammer
        while strt:
            server.sendmail(acc, contact, msg)

        server.quit()



        #yahoo
    elif menu == "2":
        strt = True
        server = smtplib.SMTP_SSL("smtp.yahoo.com", 465)
        #authenication
        acc = input("your account name: ")
        password = input("password: ")
        contact = input("email to send to: ")
        msg = input("your message: ")

        server.login(acc, password)

        while strt:
            server.sendmail(acc, contact, msg)

        server.quit()



        #outlook

    elif menu == "3":
        strt = True
        server = smtplib.SMTP_SSL("smtp.office365.com", 587)
        # authenication
        acc = input("your account name: ")
        password = input("password: ")
        contact = input("email to send to: ")
        msg = input("your message: ")

        server.login(acc, password)

        while strt:
            server.sendmail(acc, contact, msg)

        server.quit()


        #icloud
    elif menu == "4":
        strt = True
        server = smtplib.SMTP_SSL("smtp.mail.me.com", 587)
        # authenication
        acc = input("your account name: ")
        password = input("password: ")
        contact = input("email to send to: ")
        msg = input("your message: ")

        server.login(acc, password)

        while strt:
            server.sendmail(acc, contact, msg)
    elif menu == "5":
        strt = True
        server = smtplib.SMTP_SSL("smtp.aol.com", 587)
        # authenication
        acc = input("your account name: ")
        password = input("password: ")
        contact = input("email to send to: ")
        msg = input("your message: ")

        server.login(acc, password)

        while strt:
            server.sendmail(acc, contact, msg)


    elif menu == "0":
        break

    elif menu != "":
        print("please select valid option")


