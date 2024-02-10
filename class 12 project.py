import csv, mysql.connector
from datetime import date

#connection with sql
connection=mysql.connector.connect(host="localhost", user="root",passwd="admin")
cursor=connection.cursor()

#creating a new database
cursor.execute("create database if not exists project")
cursor.execute("use project")
cursor.execute("create table if not exists roomdbms(roomno bigint,vacancy varchar(10))")

#to insert data of rooms into sql table roomdbms and csv file room.csv
rfile=open('room.csv','w',newline='\n')
w=csv.writer(rfile)
w.writerows([[101,'yes'],[102,'yes'],[103,'no'],[104,'yes'],[201,'yes'],[202,'no'],[203,'no'],[204,'no'],[301,'no'],[302,'no']])
rfile.close()
count=0
while count==0:
    cursor.execute("select count(*) from roomdbms")
    data=cursor.fetchall()
    if data[0][0]==10:
        count=1
    if data[0][0]==0:
        cursor.execute("insert into roomdbms values(101,'yes'),(102,'yes'),(103,'no'),(104,'yes'),(201,'yes'),(202,'no'),(203,'no'),(204,'no'),(301,'no'),(302,'no')")
        count=1

#to insert guest details into sql table hoteldbmsdbms
cursor.execute("create table if not exists hoteldbms(Guest_name varchar(20),mobile_no bigint(10),date_of_arrival date,date_of_departure date,room_no int(4))")
connection.commit()
         
#to write data into a csv file
def g_checkin():
    a=int(input('enter the no of entries: '))
    for i in range(a):
        file=open('Silver guest Entry.csv','w',newline='\n')
        w=csv.writer(file)
        w.writerow(['Guest name','mobile no','date of arrival','date of departure','room no'])
        file.close()
        gname=input('enter name:')
        mno=int(input('enter mobile no: '))
        da=date.today()
        dd=input('enter date of departure in YYYY-MM-DD format:')
        roomverify='yes'
        while roomverify=='yes':
            rno=int(input('enter room no: '))
            rlist=[[101,'yes'],[102,'yes'],[103,'no'],[104,'yes'],[201,'yes'],[202,'no'],[203,'no'],[204,'no'],[301,'no'],[302,'no']]
            for j in range(0,len(rlist)):
                if rlist[j][0]==rno:
                    if rlist[j][1]=='yes':
                        rfile=open('room.csv','w',newline='\n')
                        file=open('Silver guest Entry.csv','w',newline='\n')
                        w=csv.writer(file)
                        print("room you choose is available......    records are getting inserted......")
                        for k in rlist:
                            if k[0]==int(rno):
                                k[1]='no'
                                print(rlist)
                        rw=csv.writer(rfile)
                        rw.writerows(rlist)
                        s=[gname,mno,da,dd,rno]
                        w.writerow(s)
                        file.close()
                        rfile.close()
                        print("successfully inserted values")
                        roomverify=input("Press enter to continue")  
                    else:
                        print("the room is already occupied.... the list of rooms are: ")
                        print(data)
                        roomverify=input("Do you want to enter a new room number to look for?")

#to read data from the file
def g_read():
    file=open('Silver guest Entry.csv','r',newline='\n')
    w=csv.reader(file)
    for i in w:
          print(i)
    file.close()
    
#to add more data into the csv file
def g_append():
    file=open('Silver guest Entry.csv','a',newline='\n')
    w=csv.writer(file)
    a=int(input('enter the no of entries: '))
    for i in range(a):     
        gname=input('enter your name:')
        mno=int(input('enter mobile no: '))
        da=date.today()
        dd=input('enter date of departure:')
        roomverify='yes'
        while roomverify=='yes':
            rno=int(input('enter room no: '))
            for j in range(len(data)):
                if data[j][0]==rno:
                    if data[j][1]=='yes':
                        print("room you choose is available......    records are getting inserted......")
                        query="update roomdbms set vacancy='no' where roomno={}".format(rno)
                        cursor.execute(query)
                        s=[gname,mno,da,dd,rno]
                        w.writerow(s)
                        connection.commit()
                        print("successfully inserted values")
                        roomverify=input("Press enter to continue")
                    else:
                        print("the room is already occupied.... the list of rooms are: ")
                        print(data)
                        roomverify=input("Do you want to enter a new room number to look for?")

# to search for a particular guest entry
def g_search():
    file=open("Silver guest Entry.csv","r")
    r=csv.reader(file)
    i=input('enter the name to be searched:')
    for l in r:
       if l[0]==i:
           print("data you requested: ",l)
    file.close()

#to enter values in a sql table
def sql_enter():
    a=int(input('enter the no of entries: '))
    cursor.execute("select * from roomdbms")
    data=cursor.fetchall()
    for row in data:
        print(row)
    for i in range(a):
        gname=input('enter your name:')
        mno=int(input('enter mobile no: '))
        da=input('enter date of arrival:')
        dd=date.today()
        roomverify='yes'
        while roomverify=='yes':
            rno=int(input('enter room no: '))
            for j in range(len(data)):
                if data[j][0]==rno:
                    if data[j][1]=='yes':
                        print("room you choose is available......    records are getting inserted......")
                        query="update roomdbms set vacancy='no' where roomno={}".format(rno)
                        cursor.execute(query)
                        query="insert into hoteldbms values(%s,%s,%s,%s,%s)"
                        s=(gname,mno,da,dd,rno)
                        cursor.execute(query,s)
                        connection.commit()
                        roomverify=input("successfully inserted values....  Press enter to continue")
                    else:
                        print("the room is not available....  the list of rooms are: \n",data)
                        roomverify=input("Do you want to enter a new room number to look for?")
    
#to read the values from the sql table
def sql_read():
    cursor.execute("select * from hoteldbms;")
    data=cursor.fetchall()
    for row in data:
        print("\nThe values inserted are;\n",row)

#to search the values from the sql table
def sql_search():
    cursor.execute("select * from hoteldbms;")
    data=cursor.fetchall()
    gname=input("Enter the name of the guest to be searched: ")
    for i in data:
        if i[0]==gname:
            print("\nthe details of the guest you were searching for is: \n",i)
        
#to delete the values from the sql table
def sql_delete():
    userverify='yes'
    while userverify=='yes':
        gname=input('enter name:')
        mno=int(input('enter mobile no: '))
        cursor.execute("select * from hoteldbms;")
        data=cursor.fetchall()
        for i in data:
            if i[0]==gname and i[1]==mno:
                print("...... guest found......")
                query="delete from hoteldbms where Guest_name={} and mobile_no={}".format(gname,mno)
                roomno=i[4]
                query="update roomdbms set vacancy='yes' where roomno={}".format(roomno)
                cursor.execute(query)
                connection.commit()
                userverify=input("successfully deleted guest....  Press enter to continue")
            else:
                print("\nthe guest does'nt exist ....  ")
                userverify=input("Write 'yes' if you wish to try again --->")
             
correction='yes'
while correction=='yes':
    print("\n----------------------------------------------------------------\n\n")
    print('''          Welcome to HOTEL SILVERBROOKE\n
                Guest Management System\n\n
    ------>>>>> Created by \n
                Hariharan Bhaskaran
                12-B  CBSE
    ----------------------------------------------------------------\n\n''')   
    dchoice=input("Please Enter the database you want to use csv or sql: ")
    if dchoice in ['csv','Csv','CSV']:
        count=0
        while count!=5:
            print("Choose the options according to your needs.\n")
            print('Write  1 ------>>>  To  create a csv file and check in a guest')
            print('Write  2 ------>>>  To check the guest database')
            print('Write  3 ------>>>  To Search for a guest and find their information')
            print('Write  4 ------>>>  To add guest details on the existing csv file')
            print('Write  5 ------>>>  Exit the program')
            count=int(input('Enter the option number:'))
            if count!=5:
                if count==1:
                    g_checkin()
                if count==2:
                    g_read()
                if count==3:
                    g_search()
                if count==4:
                    g_append()
            if count==5:
                correction='no'
                print('''\nThank you for using\n
HOTEL SILVERBROOKE Guest Management System\n
We would always try to improve our services!\n\nSee you later :)
\n........................\n''')               
    if dchoice in ['sql','Sql','SQL']:
        count=0
        while count!=5:
            print("Choose the options according to your needs.\n")
            print('Write  1 ------>>>  To Check in a guest')
            print('Write  2 ------>>>  To check the guest database')
            print('Write  3 ------>>>  To Search for a guest and find their information')
            print('Write  4 ------>>>  To Check out a guest')
            print('Write  5 ------>>>  Exit the program')
            count=int(input('Enter the option number:'))
            if count!=5:
                if count==1:
                    sql_enter()
                if count==2:
                    sql_read()
                if count==3:
                    sql_search()
                if count==4:
                    sql_delete()
            if count==5:
                correction='no'
                print('''/nThank you for using\n
HOTEL SILVERBROOKE Guest Management System\n
We would always try to improve our services!\n
See you later :) \n\n
        ........................\n''')
                correction='no'
    else:
        correction=input("Please enter yes if you wish to continue")
        if correction!='yes':
            print('''Thank you for using\n
HOTEL SILVERBROOKE Guest Management System\n
We would always try to improve our services!\n
See you later :) \n\n........................\n''') 
