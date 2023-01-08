import PIL
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage 
import sqlite3
import random
from tkinter import Tk, Label
from PIL import Image, ImageTk
# connect to the database
db = sqlite3.connect('online_food_delivery.db')

# create a cursor object for executing SQL commands
cursor = db.cursor()

# create the main window
login_window = tk.Tk()
# create the login function
# create the login window

login_window.title('Login Page')
login_window.geometry('1166x718')
#login_window.state('zoomed')
login_window.resizable(0,0)
#=======================================================================
#============================backgroundimage===========================
#======================================================================
bg_frame = Image.open('background1.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(login_window, image=photo)
bg_panel.image = photo
bg_panel.pack(fill='both', expand='yes')
# ====== Login Frame =========================
label_frame = tk.Frame(login_window, bg='#040405',width=950,height=600)
label_frame.place(x=100, y=60)
#=======================================================================
#=======================================================
#======================================================================
txt = "WELCOME"
heading = Label(label_frame, text=txt, font=('yu gothic ui',25, "bold"),bg="#040405",
                     fg='white',
                     bd=5,
                     relief=tk.FLAT)
heading.place(x=80, y=30, width=300,height=30)
#=======================================================================
# ============ Left Side Image===============================================
#=====================================================================
side_image = Image.open('vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(label_frame,image=photo, bg='#040405')
side_image_label.image = photo
side_image_label.place(x=5, y=100)
#======================================================================
# ============ Sign InImage=============================================
#======================================================================
sign_in_image = Image.open('hyy.png')
photo = ImageTk.PhotoImage(sign_in_image)
sign_in_image_label = Label(label_frame, image=photo,bg='#040405')
sign_in_image_label.image = photo
sign_in_image_label.place(x=620, y=130)

#=======================================================================
# ============ Sign In label=============================================
#=======================================================================
sign_in_label = Label(label_frame, text="Sign In",bg="#040405", fg="white",
                            font=("yu gothic ui", 17, "bold"))
sign_in_label.place(x=650, y=240)



#======================================================================
#============================username==================================
#======================================================================
username_label = Label(label_frame,text="Username",bg="#040405", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
username_label.place(x=550, y=300)
username_entry = tk.Entry(label_frame,highlightthickness=0,relief=tk.FLAT, bg="#040405",fg="#6b6a69",
                            font=("yu gothic ui ", 12, "bold"))
username_entry.place(x=580, y=335, width=270)
username_line = tk.Canvas(label_frame,width=300, height=2.0,bg="#bdb9b1",highlightthickness=0)
username_line.place(x=550, y=359)
# ===== Username icon =========
username_icon = Image.open('username_icon.png')
photo = ImageTk.PhotoImage(username_icon)
username_icon_label = Label(label_frame,image=photo,bg='#040405')
username_icon_label.image = photo
username_icon_label.place(x=550, y=332)

#=======================================================================
#============================password==================================
#======================================================================
password_label = Label(label_frame,text="Password",bg="#040405", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
password_label.place(x=550, y=380)
password_entry = tk.Entry(label_frame,highlightthickness=0,relief=tk.FLAT, bg="#040405",fg="#6b6a69",
                            font=("yu gothic ui", 12, "bold"), show="*")
password_entry.place(x=580, y=416, width=244)
password_line = tk.Canvas(label_frame,width=300, height=2.0,bg="#bdb9b1",highlightthickness=0)
password_line.place(x=550, y=440)
# ======== Password icon ================
password_icon = Image.open('password_icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(label_frame,image=photo,bg='#040405')
password_icon_label.image = photo
password_icon_label.place(x=550, y=414)

# create the login button
lgn_button = Image.open('btn1.png')
photo = ImageTk.PhotoImage(lgn_button)
lgn_button_label = Label(label_frame,image=photo, bg='#040405')
lgn_button_label.image = photo
lgn_button_label.place(x=550, y=450)
login = tk.Button(lgn_button_label,text='LOGIN', font=("yugothic ui", 13, "bold"),width=25, bd=0,
                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=lambda: check_login(username_entry.get(), password_entry.get()))
login.place(x=20, y=10)
#=======================================================================
#============================Forgotpassword============================
#======================================================================
forgot_button = tk.Button(label_frame, text="Forgot Password ?",
                            font=("yu gothic ui", 13, "bold underline"), fg="white", relief=tk.FLAT,
                            activebackground="#040405"
                            , borderwidth=0, background="#040405", cursor="hand2")
forgot_button.place(x=630, y=510)

# =========== Sign Up ==================================================
sign_label = Label(label_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                        relief=tk.FLAT, borderwidth=0, background="#040405", fg='white')
sign_label.place(x=550, y=560)
signup_img = PIL.Image.open(r"register.png")
img = ImageTk.PhotoImage(signup_img)
signup_button_label = tk.Button(label_frame,image=img, bg='#98a65d', cursor="hand2",
                                  borderwidth=0, background="#040405", activebackground="#040405",command=lambda:register(login_window))
signup_button_label.place(x=670, y=555, width=111,height=35)

def register(login_window):
    # create the register window
    register_window = tk.Toplevel(login_window)
    register_window.title('Register')
    
    # create the username and password labels and entry fields
    username_label = tk.Label(register_window, text='Username:')
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()
    
    password_label = tk.Label(register_window, text='Password:')
    password_label.pack()
    password_entry = tk.Entry(register_window, show='*')
    password_entry.pack()  

    kinhto_label = tk.Label(register_window, text='Κινητό:')
    kinhto_label.pack()
    kinhto_entry = tk.Entry(register_window)
    kinhto_entry.pack()

    email_label = tk.Label(register_window, text='Email:')
    email_label.pack()
    email_entry = tk.Entry(register_window)
    email_entry.pack()

    onoma_label= tk.Label(register_window, text='Όνομα:')
    onoma_label.pack()
    onoma_entry= tk.Entry(register_window)
    onoma_entry.pack()

    epitheto_label= tk.Label(register_window, text='Επώνυμο:')
    epitheto_label.pack()
    epitheto_entry= tk.Entry(register_window)
    epitheto_entry.pack()
    
    # create the register button
    register_button = tk.Button(register_window, text='Register', command=lambda: create_account(username_entry.get(), password_entry.get(),onoma_entry.get(),epitheto_entry.get(),email_entry.get(),kinhto_entry.get()))
    register_button.pack()

# create the create account function
    def create_account(username, password, onoma, epitheto,email,kinhto):
        incoming_messages = 0
        rating = 0
        id_pelath = random.randint(10000,99999)
        cursor.execute(f'INSERT INTO ΠΕΛΑΤΗΣ(username, password,"ID Πελάτη","Κινητό","Email","Εισερχόμενα Μηνύματα","Rating","Όνομα","Επώνυμο") VALUES("{username}","{password}","{id_pelath}","{kinhto}","{email}","{incoming_messages}","{rating}","{onoma}","{epitheto}")')
        db.commit()
        register_window.destroy()



# create the check login function
def check_login(username, password):
    if (username == "admin" and password == "admin"):
        # create the administrator menu
        admin_menu = tk.Toplevel(login_window)
        admin_menu.title('Administrator Menu')
        
        # create the search entry and label
        search_label = tk.Label(admin_menu, text='Where:')
        search_entry = tk.Entry(admin_menu)
        search_label.pack()
        search_entry.pack()

        equals_label = tk.Label(admin_menu, text='equals to:')
        equals_entry = tk.Entry(admin_menu)
        equals_label.pack()
        equals_entry.pack()

        # create the sort entry and label
        sort_label = tk.Label(admin_menu, text='Sort:')
        sort_entry = tk.Entry(admin_menu)
        sort_label.pack()
        sort_entry.pack()

        # create the radio buttons for the sort order
        sort_order = tk.StringVar()
        sort_ascending_button = tk.Radiobutton(admin_menu, text='Ascending', variable=sort_order, value='ASC')
        sort_descending_button = tk.Radiobutton(admin_menu, text='Descending', variable=sort_order, value='DESC')
        sort_ascending_button.pack()
        sort_descending_button.pack()

        
        tickets_button = tk.Button(admin_menu, text='TICKETS', command=lambda: view_table('TICKET', search_entry.get(),equals_entry.get(), sort_entry.get(), sort_order.get()))
        tickets_button.pack()
        
        distributions_button = tk.Button(admin_menu, text='ΔΙΑΝΟΜΕΙΣ', command=lambda: view_table('ΔΙΑΝΟΜΕΑΣ', search_entry.get(),equals_entry.get() ,sort_entry.get(), sort_order.get()))
        distributions_button.pack()
        
        available_products_button = tk.Button(admin_menu, text='ΔΙΑΘΕΣΙΜΟΤΗΤΑ', command=lambda: view_table('ΔΙΑΤΙΘΕΤΑΙ', search_entry.get(),equals_entry.get() , sort_entry.get(), sort_order.get()))
        available_products_button.pack()
        
        customer_addresses_button = tk.Button(admin_menu, text='ΔΙΕΥΘΥΝΣΕΙΣ ΠΕΛΑΤΩΝ', command=lambda: view_table('ΔΙΕΥΘΥΝΣΗ ΠΕΛΑΤΗ', search_entry.get(),equals_entry.get() , sort_entry.get(), sort_order.get()))

        customer_orders_button = tk.Button(admin_menu, text='ΠΑΡΑΓΓΕΛΙΕΣ', command=lambda: view_table('ΠΑΡΑΓΓΕΛΙΑ', search_entry.get(),equals_entry.get() , sort_entry.get(), sort_order.get()))
        customer_orders_button.pack()
        
        customers_button = tk.Button(admin_menu, text='ΠΕΛΑΤΕΣ', command=lambda: view_table('ΠΕΛΑΤΗΣ', search_entry.get(),equals_entry.get() , sort_entry.get(), sort_order.get()))
        customers_button.pack()
        
        stores_button = tk.Button(admin_menu, text='ΚΑΤΑΣΤΗΜΑΤΑ', command=lambda: view_table('ΚΑΤΑΣΤΗΜΑ', search_entry.get(),equals_entry.get() , sort_entry.get(), sort_order.get()))
        stores_button.pack()
        
        products_button = tk.Button(admin_menu, text='ΚΑΤΗΓΟΡΙΑ ΠΡΟΙΟΝΤΟΣ', command=lambda: view_table('ΠΡΟΙΟΝ', search_entry.get(),equals_entry.get() , sort_entry.get(), sort_order.get()))
        products_button.pack()
        
        average_costs = tk.Button(admin_menu, text='Average Costs', command=lambda: get_avg_costs())
        average_costs.pack()

        logout_button = tk.Button(admin_menu, text='Logout', command=admin_menu.destroy)
        logout_button.pack()

    else:
        # check if the username and password are correct
        cursor.execute(f'SELECT "ID Πελάτη" FROM ΠΕΛΑΤΗΣ WHERE username="{username}" AND password="{password}"')
        account = cursor.fetchone()
        
        if account:
            # create the customer menu
            customer_menu = tk.Toplevel(login_window)
            customer_menu.title('Customer Menu')
            customer_id = account[0]
            # create the buttons for each option
            view_orders_button = tk.Button(customer_menu, text='View Orders', command=lambda: view_history(customer_id))
            view_orders_button.pack()
            
            place_order_button = tk.Button(customer_menu, text='Place Order', command=lambda:place_order(username))
            place_order_button.pack()
            
            logout_button = tk.Button(customer_menu, text='Logout', command=customer_menu.destroy)
            logout_button.pack()
        else:
            # create the error window
            error_window = tk.Toplevel(login_window)
            error_window.title('Error')
            
            # create the error label
            error_label = tk.Label(error_window, text='Invalid username or password. Please try again')
            error_label.pack()
            
            # create the dismiss button
            dismiss_button = tk.Button(error_window, text='Dismiss', command=error_window.destroy)
            dismiss_button.pack()

# create the view table function
def view_table(table_name, search_criteria=None,equalsto=None,sort_column=None, sort_order=None):
    # execute a SELECT statement to retrieve the data from the table
    query = 'SELECT * FROM ' + table_name
    if search_criteria:
        query += ' WHERE ' + f'"{search_criteria}"' + '=' + f'"{equalsto}"'
    
    # Add the sort criteria to the ORDER BY clause, if specified
    if sort_column:
        query += ' ORDER BY ' + f'"{sort_column}"'
        if sort_order:
            query += ' ' + sort_order
    
    cursor.execute(query)
    # retrieve the data from the cursor object
    data = cursor.fetchall()
    
    # create a new window to display the data
    table_window = tk.Toplevel(login_window)
    table_window.title(table_name)
    
    # create a canvas widget to hold the table
    canvas = tk.Canvas(table_window)
    canvas.pack(side='left', fill='both', expand=True)
    
    # create a frame to hold the table labels
    frame = tk.Frame(canvas)
    frame.pack()
    
    # create a vertical scrollbar for the canvas
    scrollbar = tk.Scrollbar(table_window, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')
    
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # bind the frame to the canvas scroll area
    canvas.create_window((0,0), window=frame, anchor='nw')
    
    if data:
        # display the data in the table
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                label = tk.Label(frame, text=cell, font=('Arial', 12))
                label.grid(row=i+1, column=j, sticky='nsew')
            
    # configure the grid layout
    for i in range(len(data)):
        frame.grid_columnconfigure(i, weight=1)
        
    # update the canvas scrollregion
    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))

def view_history(customer_id):
    # create the history window
    history_window = tk.Toplevel(login_window)
    history_window.title('Order History')
    history_window.geometry('800x600')
    
    # execute the query and retrieve the results
    cursor.execute(f'SELECT DISTINCT "ID Παραγγελίας","ID Πελάτη","Κατηγορία","Όνομα","Κόστος" FROM ΠΑΡΑΓΓΕΛΙΑ NATURAL JOIN ΠΕΛΑΤΗΣ WHERE "ID Πελάτη"="{customer_id}"')
    results = cursor.fetchall()

    # create a label for each column in the table
    tk.Label(history_window, text='Order ID').grid(row=0, column=0)
    tk.Label(history_window, text='Customer ID').grid(row=0, column=1)
    tk.Label(history_window, text='Product').grid(row=0, column=2)
    tk.Label(history_window, text='Restaurant').grid(row=0, column=3)
    tk.Label(history_window, text='Cost').grid(row=0, column=4)

    # display the data in the table
    for i, row in enumerate(results):
        for j, cell in enumerate(row):
            tk.Label(history_window, text=cell).grid(row=i+1, column=j)





    
    

# create the place order function
def place_order(username):
    # create the place order window
    global order_window 
    order_window = tk.Toplevel(login_window)
    order_window.title('Place Order')

    # create the product selection dropdown menu
    product_label = tk.Label(order_window, text='Select a product:')
    product_label.pack()
    product_var = tk.StringVar(order_window)
    product_var.set('Select a product')
    product_dropdown = tk.OptionMenu(order_window, product_var, *get_product_names())
    product_dropdown.pack()
    
    # create the function to populate the restaurant dropdown menu with the restaurants that offer the selected product
    def get_restaurants(event,a,b):
        # clear the restaurant dropdown menu
        menu_list.delete(0,'end')
        # retrieve the restaurants that offer the selected product
        cursor.execute(f'SELECT DISTINCT "Όνομα","Κόστος" FROM ΔΙΑΤΙΘΕΤΑΙ NATURAL JOIN ΚΑΤΑΣΤΗΜΑ NATURAL JOIN ΠΡΟΙΟΝ WHERE "Κατηγορία"="{product_var.get()}"')
        results = cursor.fetchall()
        # add the restaurants to the dropdown menu
        for result in results:
            menu_list.insert('end', f'{result[0]} ({result[1]:.2f} €)')
        return result[0]
    # bind the get_restaurants function to the productdropdownmenu
    product_var.trace('w', get_restaurants)
    
    # create the restaurant selection dropdown menu
    # create the menu display list box
    menu_label = tk.Label(order_window, text='Select a restaurant:')
    menu_label.pack()
    global menu_list 
    menu_list= tk.Listbox(order_window)
    menu_list.pack()
    summary_list = tk.Listbox(order_window)
    summary_list.pack()
    summary_list.insert(tk.END)
    
    # create the add to order button
    add_button = tk.Button(order_window, text='Add to Order', command=lambda: add_to_order(order_window,summary_list))
    add_button.pack()
    # create the order summary label
    summary_label = tk.Label(order_window, text='Order Summary:')
    summary_label.pack()
    # create the order summary list box
    # create the submit order button
    
    
    submit_button = tk.Button(order_window,text='Submit Order',command=lambda:submit_order(summary_list,username,payment_method_var.get(),get_restaurants))
    submit_button.pack()
    # create the payment method selection dropdown menu
    payment_method_label = tk.Label(order_window, text='Select a payment method:')
    payment_method_label.pack()
    payment_method_var = tk.StringVar(order_window)
    payment_method_var.set('Select a payment method')
    payment_method_dropdown = tk.OptionMenu(order_window, payment_method_var, 'Μετρητά', 'Κάρτα', 'Paypal')
    payment_method_dropdown.pack()

    # create the function to populate the menu list box withtheitems from the selected restaurant


def add_to_order(order_window, summary_list):
    # retrieve the selected items from the menu list box
    selection = menu_list.curselection()
    for index in selection:
        item = menu_list.get(index)
        summary_list.insert(tk.END, item)


# create the function to submitthe order
def submit_order(summary_list, username, payment_method,get_restaurants):
    # retrieve the order items from the summary list
    order_items = {}
    for i in range(summary_list.size()):
        item = summary_list.get(i)
        if item in order_items:
            order_items[item] += 1
        else:
            order_items[item] = 1
    
    # retrieve the customer's ID
    cursor.execute(f'SELECT "ID Πελάτη" FROM ΠΕΛΑΤΗΣ WHERE Username="{username}"')
    customer_id = cursor.fetchone()[0]
    
    id_paraggelias = random.randint(1000000000,9999999999)
    id_dianomea = random.randint(1,9)
    xronos_paradwshs = random.randint(10,50)
    
    # create a new order in the database
    cursor.execute(f'insert into ΠΑΡΑΓΓΕΛΙΑ("ID Παραγγελίας","ID Καταστήματος","Χρόνος Παράδοσης","Τρόπος πληρωμής","ID Διανομέα","ID Πελάτη") values ("{id_paraggelias}","{get_restaurants}","{xronos_paradwshs}","{payment_method}","{id_dianomea}","{customer_id}")')
    db.commit()
    
    # clear the order summary and close the order window
    summary_list.delete(0, tk.END)
    order_window.destroy()

# create the function to cancelthe order

# create the function toretrieve the names of theproductsin the database
def get_product_names():
    cursor.execute('SELECT DISTINCT "Κατηγορία" FROM ΠΡΟΙΟΝ')
    results = cursor.fetchall()
    return [result[0] for result in results]
# create the function to retrieve the names oftherestaurants in the database
def get_restaurant_names():
    cursor.execute('SELECT DISTINCT "Όνομα" FROM ΚΑΤΑΣΤΗΜΑ')
    results = cursor.fetchall()
    return [result[0] for result in results]

def get_avg_costs():
    cursor.execute('SELECT "Όνομα",avg("Κόστος") as mesos_oros FROM ΚΑΤΑΣΤΗΜΑ NATURAL JOIN ΔΙΑΤΙΘΕΤΑΙ Group by "Όνομα"')
    data = cursor.fetchall()


    table_window = tk.Toplevel(login_window)
    
    if data:
    # display the data in the table
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                label = tk.Label(table_window, text=cell, font=('Arial', 12))
                label.grid(row=i+1, column=j, sticky='nsew')
            
    # configure the grid layout
    for i in range(len(data)):
        table_window.grid_columnconfigure(i, weight=1)
# run the main loop
login_window.mainloop()




