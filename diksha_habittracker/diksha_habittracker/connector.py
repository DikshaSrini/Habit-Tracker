import mysql.connector
mycon = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "Pizzaiscool_03", database = "habittracker")
if mycon.is_connected() == True:
    print ("Successfully Connected")
cursor = mycon.cursor()

def mood():
    cursor.execute("select text from entry_entry")
    row1 = cursor.fetchall()
    number_of_entries = len(row1)
    for i in range(number_of_entries):
        for emotion in row1[i]:
            if 'Happy' in emotion:
                print("Happy - Great Day!")
            elif 'Sad' in emotion:
                print("Sad - It's okay to be sad! Go listen to some music!")
            elif 'Exhausted' in emotion:
                print("Exhausted - Go have some coffee or ice cream!")
            elif  'Bored' in emotion:
                print("Bored - Try new things!")
            elif 'Excited' in emotion:
                print("Excited - Hooray")    
            else:
                print("If you're feeling confused or cant identify your emotions, take some time to introspect!")

def breakfast():
    cursor.execute("select text from entry_entry")
    row2 = cursor.fetchall()
    number_of_entries = len(row2)
    for i in range(number_of_entries):
        for bf in row2[i]:
            if 'Chocolate and strawberry pancakes' in bf:
                print("Chocolate and strawberry pancakes - Yummy!")
            elif 'Idly' in bf:
                print("Idly - Not my favourite food!")    
            else:
                print("Breakfast is the most important meal, hope you had a fulfilling breakfast!")
        
def lunch():
    cursor.execute("select text from entry_entry")
    row3 = cursor.fetchall()
    number_of_entries = len(row3)
    for i in range(number_of_entries):
        for lu in row3[i]:
            if 'Roti and paneer' in lu:
                print("Roti and paneer - Ooh North Indian food!")
            elif 'Salad' in lu:
                print("Salad - Healthy choice today!")    
            else:
                print("Hope you had full lunch to have energy for the rest of the day!")
   
def dinner():
    cursor.execute("select text from entry_entry")
    row4 = cursor.fetchall()
    number_of_entries = len(row4)
    for i in range(number_of_entries):
        for di in row4[i]:
            if 'Pasta' in di:
                print("Pasta - Italian's favourite!")
            elif 'Curd rice' in di:
                print("Curd Rice - Meh, just curd rice!")    
            else:
                print("Hope you had light dinner to be able to rest easily!")
    
def meditation():
    cursor.execute("select text from entry_entry")
    row5 = cursor.fetchall()
    number_of_entries = len(row5)
    for i in range(number_of_entries):
        for med in row5[i]:
            if 'Meditated' in med:
                print("Meditation Done - Peaceful!")
            elif 'No meditation done' in med:
                print("Meditation Not Done - Go Relax!")    
            else:
                print("Enter Done/Not completed")

def reading():
    cursor.execute("select text from entry_entry")
    row6 = cursor.fetchall()
    number_of_entries = len(row6)
    for i in range(number_of_entries):
        for rd in row6[i]:
            if 'Read' in rd:
                print("Reading Done - Insightful")
            elif 'Did not' in rd:
                print("Reading Not Done - Get some knowledge")    
            else:
                print("Enter Done/Not completed")

def workout():
    cursor.execute("select text from entry_entry")
    row7 = cursor.fetchall()
    number_of_entries = len(row7)
    for i in range(number_of_entries):
        for wk in row7[i]:
            if 'Worked out' in wk:
                print("Workout Done - Your day is complete!")
            elif 'Not done' in wk:
                print("Workout Not Done - It is a slow process but quitting won't speed it up!")    
            else:
                print("Enter Done/Not completed")

while (1):
    print('''Menu
        1.Message for your mood
        2.Message for your breakfast
        3.Message for your lunch
        4.Message for your dinner
        5.Message for your meditation
        6.Message for your reading
        7.Message for your workout
        8.Exit''')
    ch = int(input("Enter Choice: "))
    if (ch == 1):
        mood()
    elif (ch == 2):
        breakfast()
    elif (ch == 3):
        lunch()
    elif (ch == 4):
        dinner()
    elif (ch == 5):
        meditation()
    elif (ch == 6):
        reading()
    elif (ch == 7):
        workout()
    elif (ch == 8):
        break
    else:
        print("Invalid Input")





    



