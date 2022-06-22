#import tkinter so we can make a GUI
from tkinter import*

# quit subroutine

def quit():
    main_window.destroy()

# print details of all the variables


def print_julies_tracker():
    #there are the global variables that are used
    global j_names, total_entries, name_count
    name_count=0
    #create the column headings
    Label(main_window, font=("Helvetica 10 bold"), text="Row").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Item Hired").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="No Items Hired").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Receipt Number").grid(column=4, row=7)

    # add each item in the list into its own row
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(julies_tracker[name_count][0])).grid(column=1, row=name_count+8)
        Label(main_window, text=(julies_tracker[name_count][1])).grid(coulmn=2, row=name_count+8)
        Label(main_window, text=(julies_tracker[name_count][2])).grid(column=3, row=name_count+8)
        Label(main_window, text=(julies_tracker[name_count][3])).grid(column=4, row=name_count+8)
        name_count += 1

# Check the inputs are all valid

def check_inputs():
    # these are the global variables that are used
    global julies_tracker, entry_name, entry_item_hired, entry_no_items_hired, entry_receipt_number
    input_check = 0
    Label(main_window, text="              ").grid(column=2, row=0)
    Label(main_window, text="              ").grid(column=2, row=1)
    Label(main_window, text="              ").grid(column=2, row=2)
    Label(main_window, text="              ").grid(column=2, row=3)
    # Check that name is not blank, set error if blank
    if len(entry_name.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=0)
        input_check = 1
    # Check that item hired is not blank, set error text if blank
    if len(entry_item_hired.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=1)
    # Check the number of items is not blank and between 1 and 500, set error text if blank
    if (entry_no_items_hired().isdigit()):
        if int(entry_no_items_hired()) < 1 or int(entry_no_items_hired.get()) > 500:
            Label(main_window, fg="red", text="1-500 only") .grid(column=2, row=2)
            input_check = 1

        else:
            Label(main_window, fg="red", text="1-500 only") .grid(column=2, row=2)
            input_check = 1
        # Check that receipt number is not blank, set error if if blank
        if len(entry_receipt_number.get()) == 0:
            Label(main_window, fg="red", text="Required") .grid(column=2, row=3)
            input_check = 1
        if input_check == 0:
            append_name()

# add the next items in list


def append_name():
    # these are the global variables that are used
    global julies_tracker, entry_name, entry_item_hired, entry_no_items_hired, entry_receipt_number
    # append each item to its own area of the list
    julies_tracker.append([entry_name.get(), entry_item_hired.get(), entry_no_items_hired.get(), entry_receipt_number()])
    
    # clear the boxes
    entry_name.delete(0, 'end')
    entry_item_hired.delete(0, 'end')
    entry_no_items_hired.delete(0, 'end')
    entry_receipt_number.delete(0, 'end')
    total_entries += 1

# delete a row from the list

def delete_row():
     # these are the global variables that are used
     global julies_tracker, delete_item, total_entries, name_count
     # find which row is to be deleted and delete it
     del julies_tracker[int(delete_item.get())]
     total_entries = total_entries - 1
     delete_item.delete(0, 'end')
     # clear the last item displayed on the GUI
     Label(main_window, text="           ").grid(column=0, row=name_count+7)
     Label(main_window, text="           ").grid(column=1, row=name_count+7)
     Label(main_window, text="           ").grid(column=2, row=name_count+7)
     Label(main_window, text="           ").grid(column=3, row=name_count+7)
     Label(main_window, text="           ").grid(column=4, row=name_count+7)
     # print all the items in the list
     print_julies_tracker()

# create the buttons and labels


def setup_buttons():
    # these are the global variables that are used
    global julies_tracker, entry_name, entry_item_hired, entry_no_item_hired, entry_receipt_number, total_entries, delete_item
    # create all the empty and default labels, buttons and entry boxes. Put them in correct grid location
    Label(main_window, text="Name"). grid(column=0, row=0, sticky=E)
    entry_name = Entry(main_window)
    entry_name.grid(column=1, row=0)
    Label(main_window, text="Item Hired"). grid(column=0, row=1, sticky=E)
    entry_item_hired = Entry(main_window)
    entry_item_hired.grid(column=1, row=1)
    Button(main_window, text="Exit", command=quit, width=10) .grid(column=4, row=0, sticky=E)
    Button(main_window, text="Append Details", command=check_inputs).grid(column=3, row=1)
    Button(main_window, text="Print Details", command=print_julies_tracker, width=10).grid(column=4, row=1, sticky=E)
    Label(main_window, text="No Items Hired") .grid(column=0, row=2, sticky=E)
    entry_no_item_hired = Entry(main_window)
    entry_no_item_hired.grid(column=1, row=2)
    delete_item = Entry(main_window)
    delete_item.grid(column=4, row=2)
    Label(main_window, text="Receipt Number"). grid(column=0,row=3, sticky=E)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=1, row=3)
    Button(main_window, text="Delete Row", command=delete_row, width=10) .grid(column=4, row=3, sticky=E)
    Label(main_window, text="           ").grid(column=2, row=0)


 # start the program running

def main():
     # these are the global versions that are used
     global main_window
     global julies_tracker, entry_name, entry_item_hired, entry_no_item_hired, entry_receipt_number, total_entries
     # create empty list for camp details and empty variables for entries in list
     julies_tracker = []
     total_entries = 0
     # create the GUI
     main_window = Tk()
     setup_buttons()
     main_window.mainloop()

main()












