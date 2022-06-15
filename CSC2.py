#import tkinter so we can make a GUI
from tkinter import*

# quit subroutine

def quit():
    main_window.destroy()

# print details of all the variables


def print_julies_tracker():
    #there are the global variables that are used
    global j_ames, total_entries, name_count
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
    if len(entry_item_hired()) == 0:
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










