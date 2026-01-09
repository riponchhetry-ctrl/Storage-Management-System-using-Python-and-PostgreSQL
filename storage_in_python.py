import psycopg2

conn = psycopg2.connect(
    database="ripon",
    host="localhost",
    user="postgres",
    password="password",
    port="5432"
)

cursor = conn.cursor()

while True:
    choice = int(input("\n1 for entry of item \n2 to view the storage \n3 to update storage \n4 to exit....\nEnter your choice:"))

    if choice==1 :
        item_name=input("enter to name of the item:").lower()
        item_quantity=int(input("enter the quantity of the item in kgs:"))
        item_price=int(input("enter the price of the item:"))
        cursor.execute(
            'insert into storage( item_name ,quantity, price ) values (%s, %s, %s);', (item_name ,item_quantity, item_price)
        )
        conn.commit()
        print("\n")
        
    elif choice==2:
        cursor.execute(
            "select * from storage;"
        )
        values = cursor.fetchall()
        print("Name\tQuanity\tPrice")
        for value in values:
            print(f"{value[1]}\t{value[2]}\t{value[3]}")
        print('\n')

    elif choice==3:
        updated_quantity=0
        updated_price=0
        choice_for_update=int(input("enter 1 if you want to change the quantity of the item \n2 if you want to change the price of the item \n3 if you want to change both \n your choice:"))
        name_for_update=input("enter to name of item you want to modify someting about:").lower()

        if choice_for_update == 1 :
            updated_quantity= int(input("enter to updated quantity:"))
            cursor.execute(
                    'update storage set quantity = %s  where item_name = %s;', (updated_quantity, name_for_update)
                )
            conn.commit()
            print('\n')

        elif choice_for_update==2:
            updated_price=int(input("enter the updated price:"))
            cursor.execute(
                "update storage set price= %s  where item_name= %s;", (updated_price, name_for_update))
            conn.commit()
            print('\n')

        elif choice_for_update==3 :
            updated_quantity= int(input("enter to updated quantity:"))
            updated_price=int(input("enter the updated price:"))
            cursor.execute(
                "update storage set quantity= %s, price= %s  where item_name= %s;", (updated_quantity ,updated_price, name_for_update))
            conn.commit()
            print('\n')

        else :
            print("please a valid option")
            print('\n')

    elif choice==4:
        break
    
    else:
        print("please enter a valid option.....")
         
                 
                

        
