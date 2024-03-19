from tkinter import *
from tkinter import messagebox

# הגדרת נתונים

tables = [
    {"id": 1, "capacity": 2, "is_available": False},
    {"id": 2, "capacity": 4, "is_available": False},
    {"id": 3, "capacity": 6, "is_available": False},
    {"id": 4, "capacity": 2, "is_available": False},
    {"id": 5, "capacity": 8, "is_available": False},
    {"id": 6, "capacity": 2, "is_available": True},
    {"id": 7, "capacity": 2, "is_available": True},
    {"id": 8, "capacity": 6, "is_available": False},
    {"id": 9, "capacity": 4, "is_available": True},
    {"id": 10, "capacity": 4, "is_available": True},
    {"id": 11, "capacity": 4, "is_available": False},
    {"id": 12, "capacity": 6, "is_available": True},
    {"id": 13, "capacity": 4, "is_available": True},
    {"id": 14, "capacity": 2, "is_available": False},
    {"id": 15, "capacity": 8, "is_available": True},
    {"id": 16, "capacity": 4, "is_available": True},
    {"id": 17, "capacity": 4, "is_available": False},
    {"id": 18, "capacity": 6, "is_available": True},
]


menu_items = {
    "First dishes": [
        {"name": "Green Salad", "price": 15},
        {"name": "Tomato Soup", "price": 20},
        {"name": "Meat Tartar", "price": 38},
    ],
    "Main dishes": [
        {"name": " Fish&Chips", "price": 37},
        {"name": "Tomato Souce Pasta", "price": 41},
        {"name": "Hamburger", "price": 64},
    ],
    "Desserts": [
        {"name": "Cheese Cake", "price": 25},
        {"name": "Lemon Pie", "price": 30},
        {"name": "IceCream", "price": 20},
    ],
    "Drinks": [
        {"name": "Mineral Water", "price": 7},
        {"name": "Orange juice", "price": 15},
        {"name": "Cola", "price": 12},
    ],
}


def check_availability():
       # קבלת מספר סועדים מהלקוח
    num_of_guests = int(input("Wellcome !, table for how much people ?"))

    # בדיקה אם יש שולחן פנוי מתאים
    available_table = False
    for table in tables:
        if table["capacity"] >= num_of_guests and table["is_available"]:
            available_table = True
            break

    # הצגת הודעה מתאימה
    if available_table:
        print(f"there is a table for {num_of_guests} guests. Here, have a sit and a manu. ")
        show_menu()
        
    else:
        print(f"unfortunately,is no table avialble for {num_of_guests} guests right now, try agian later. ")
        exit()

def show_menu():
    # Create frames for each dish category
    appetizers_frame = LabelFrame(root, text="Appetizers")
    main_courses_frame = LabelFrame(root, text="Main Courses")
    desserts_frame = LabelFrame(root, text="Desserts")
    drinks_frame = LabelFrame(root, text="Drinks")

    # Pack the frames horizontally, adjusting padding as needed
    appetizers_frame.pack(side=LEFT, padx=8, pady=10)
    main_courses_frame.pack(side=LEFT, padx=8, pady=10)
    desserts_frame.pack(side=LEFT, padx=8, pady=10)
    drinks_frame.pack(side=LEFT, padx=8, pady=10)
    
    # Add "Done" button with margins
    done_button = Button(root, text="Done", command=show_bill, font=("Arial", 12))
    done_button.pack(side=TOP, anchor=E)
    
    # Add buttons within each frame
    for category, items in menu_items.items():
        frame = LabelFrame(root, text=category)
        frame.pack(fill="both", expand=False)  # Allow frames to expand

        for item in items:
            button = Button(frame, text=item["name"], command=lambda item=item: add_to_order(item))
            button.pack(side=TOP, padx=2, pady=2)  # Pack vertically, fill horizontally, add padding

    # Add "Done" button with margins
    done_button = Button(root, text="Done", command=show_bill, font=("Arial", 12))
    done_button.pack(side=TOP, anchor=E)

def add_to_order(item):
    # הוספת פריט להזמנה וסכימת מחיר
    global total_price, order_list
    total_price += item["price"]
    order_list.append(item)
    # הצגת פריט שהוזמן
    list_box.insert(END, f"{item['name']} - {item['price']} ILS")

def show_order_details():
    global order_list
    # יצירת מחרוזת עם פרטי ההזמנה
    order_text = "Your Order:\n\n"
    for item in order_list:
        order_text += f"{item['name']} - {item['price']} ILSח\n"
    
    # הצגת פרטי ההזמנה בחלון נפרד
    messagebox.showinfo("Order details: ", order_text)

def calculate_total_price():
    global order_list
    total_price = 0
    for item in order_list:
        total_price += item["price"]
    return total_price

def show_bill():
    global total_price
    # חישוב סכום כולל
    total_price = calculate_total_price()
    
    # יצירת מחרוזת עם פרטי ההזמנה
    order_text = "Your Order : \n\n"
    for item in order_list:
        order_text += f"{item['name']} - {item['price']} ILS\n"
    
    # הצגת חשבון בחלון נפרד
    messagebox.showinfo("Bill", f"""
    

    {order_text}

    Final price: {total_price} ILS
    
    Thank You And GoodBye :) !
    """)
    exit()

# משתנים גלובליים
total_price = 0
order_list = []

# ממשק משתמש
root = Tk()
root.title("מסעדה")


# כפתור בדיקת זמינות
check_availability_button = Button(root, text="Check for Table", command=check_availability)
check_availability_button.pack()

# רשימת פריטים שהוזמנו
list_box = Listbox(root,width=27, height=10)
list_box.pack()

# כפתור "סיימתי"

root.mainloop()