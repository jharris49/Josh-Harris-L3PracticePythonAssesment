from tkinter import *
from tkinter import messagebox

class Person:
    def __init__(self, name, age, phone_status, phone_number = None):
        self.name = name 
        self.age = age
        self.phone_status = phone_status
        self.phone_number = phone_number

class GetDataGUI:
    def __init__(self, parent):
        self.persons = []
        self.person_counter = 0

        self.data_collection_frame = Frame(parent)
        self.display_data_frame = Frame(parent)
        self.current_frame = 1

        self.phone_number_label = Label(
            self.data_collection_frame,
            text = "Enter your phone number:"
        )

        self.phone_number = StringVar()
        self.phone_number_entry = Entry(
            self.data_collection_frame,
            textvariable = self.phone_number
        )

        self.collecting_data_label = Label(
            self.data_collection_frame,
            text = "Collecting Person Data"
        )
        self.collecting_data_label.grid(
            row = 0, 
            column = 0, 
            sticky = W, 
            padx = 20, 
            pady = 20
        )

        self.name_label = Label(
            self.data_collection_frame,
            text = "Name:"
        )
        self.name_label.grid(
            row = 1, 
            column = 0,  
            sticky = W, 
            padx = 20,
            pady = 5
        )

        self.age_label = Label(
            self.data_collection_frame,
            text = "Age:"
        )
        self.age_label.grid(
            row = 2, 
            column = 0,  
            sticky = W, 
            padx = 20,
            pady = 5
        )

        self.phone_label = Label(
            self.data_collection_frame,
            text = "Do you have a mobile phone?"
        )
        self.phone_label.grid(
            row = 3, 
            column = 0,  
            sticky = W,
            padx = 20,
            pady = 5
        )

        self.show_button = Button(
            self.data_collection_frame,
            text = "Show All",
            command = self.switch_frame,
        )
        self.show_button.grid(
            row = 0, 
            column = 1, 
            sticky = W,
            padx = 10
        )

        self.name = StringVar()
        self.name_entry = Entry(
            self.data_collection_frame,
            textvariable = self.name
        )
        self.name_entry.grid(
            row = 1,
            column = 1, 
            sticky = W,
            padx = 10
        )

        self.age = IntVar()
        self.age_entry = Spinbox(
            self.data_collection_frame,
            textvariable = self.age,
            from_ = 0,
            to = 200,
        )
        self.age_entry.grid(
            row = 2, 
            column = 1, 
            sticky = W,
            padx = 10
        )

        self.mobile_phone = BooleanVar()
        self.mobile_phone.set(False)

        self.phone_radiobutton_false = Radiobutton(
            self.data_collection_frame,
            variable = self.mobile_phone,
            value = False,
            text = "No",
            command = self.check_phone_radiobuttons
        )
        self.phone_radiobutton_false.grid(
            row = 3, 
            column = 1, 
            sticky = W,
            padx = 10
        )

        self.phone_radiobutton_true = Radiobutton(
            self.data_collection_frame,
            variable = self.mobile_phone,
            value = True,
            text = "Yes",
            command = self.check_phone_radiobuttons
        )
        self.phone_radiobutton_true.grid(
            row = 4,
            column = 1, 
            sticky = W,
            padx = 10
        )

        self.enter_data_button = Button(
            self.data_collection_frame,
            text = "Enter Data",
            command = self.save_person
        )
        self.enter_data_button.grid(
            row = 5, 
            column = 0,
            columnspan = 2,
            pady = 20
        )


        self.display_data_label = Label(
            self.display_data_frame,
            text = "Displaying Person Data"
        )
        self.display_data_label.grid(
            row = 0, 
            column = 0, 
            sticky = W, 
            padx = 20, 
            pady = 20
            )

        self.f2_name_label = Label(
            self.display_data_frame,
            text = "Name:"
        )
        self.f2_name_label.grid(
            row = 1, 
            column = 0,  
            sticky = W, 
            padx = 20,
            pady = 5
        )

        self.f2_age_label = Label(
            self.display_data_frame,
            text = "Age:"
        )
        self.f2_age_label.grid(
            row = 2, 
            column = 0,  
            sticky = W, 
            padx = 20,
            pady = 5
        )

        self.person_phone_label = Label(
            self.display_data_frame,
            text = "(name) has a mobile phone"
        )
        self.person_phone_label.grid(
            row = 3, 
            column = 0, 
            columnspan = 2, 
            padx = 20,
            pady = 5
        )

        self.f2_phone_number_label = Label(
            self.display_data_frame,
            text = "Phone Number:"
        )

        self.person_phone_number_label = Label(
            self.display_data_frame,
            text = "(number)"
        )

        self.previous_button = Button(
            self.display_data_frame,
            text = "Previous",
            command = lambda:self.output_data(-1)
        )
        self.previous_button.grid(
            row = 4, 
            column = 0, 
            sticky = W,
            padx = 20,
            pady = 10
        )

        self.add_person_button = Button(
            self.display_data_frame,
            text = "Add New Person",
            command = self.switch_frame,
            anchor = W,
            padx = 10
        )
        self.add_person_button.grid(
            row = 0, 
            column = 1, 
            sticky = W,
            padx = 10
        )

        self.person_name_label = Label(
            self.display_data_frame,
            text = "(name)"
        )
        self.person_name_label.grid(
            row = 1, 
            column = 1,  
            sticky = W, 
            padx = 10
        )

        self.person_age_label = Label(
            self.display_data_frame,
            text = "(age)"
        )
        self.person_age_label.grid(
            row = 2, 
            column = 1,  
            sticky = W, 
            padx = 10
        )

        self.next_button = Button(
            self.display_data_frame,
            text = "Next",
            command = lambda:self.output_data(1)
        )
        self.next_button.grid(
            row = 4, 
            column = 1, 
            sticky = E,
            padx = 20,
            pady = 10
        )

        self.data_collection_frame.grid()
      


    def switch_frame(self):
        if len(self.persons) == 0:
            messagebox.showerror("No Data Saved", "You have not saved any data yet. Save data first before trying to view it.")
            self.name_entry.focus_set()
        else:
            if self.current_frame == 1:
                self.data_collection_frame.grid_forget()
                self.output_data(0)
                self.display_data_frame.grid()
                self.current_frame = 2
                target_frame = self.display_data_frame
            else:
                self.display_data_frame.grid_forget()
                self.data_collection_frame.grid()
                self.current_frame = 1
                target_frame = self.data_collection_frame

            """
            AI code below in order to fix issues with macOS preventing frames from being redrawn
            correctly. 
            """
            target_frame.tkraise()             # Pull to front
            target_frame.update_idletasks()    # Redraw the widgets
            target_frame.focus_force()         # Grab keyboard focus
            
            # This is the "Magic" line for macOS: 
            # It tells the window to refresh its visual state immediately.
            target_frame.master.update()
            """
            End of AI code. 
            """

    def save_person(self):
        if self.check_entries():
            self.persons.append(Person(self.name.get(), self.age.get(), self.mobile_phone.get(), self.phone_number.get().replace(" ", "")))
            messagebox.showinfo("Data Saved!", "This data has been saved.")
            self.name.set("")
            self.age.set(0)
            self.phone_number.set("")
            self.name_entry.focus_set()

    def output_data(self, status):
        self.person_counter += status
        if len(self.persons) == self.person_counter or self.person_counter < 0 :
            messagebox.showerror("Not more data", "You cannot see anymore data as there is no more data to display. Try entering more data.")
            self.person_counter -= status
        else:
            temp_name = self.persons[self.person_counter].name
            temp_age = self.persons[self.person_counter].age
            temp_mobile_status = self.persons[self.person_counter].phone_status
            temp_phone_number = self.persons[self.person_counter].phone_number

            self.person_name_label.config(
                text = temp_name
            )
            self.person_age_label.config(
                text = temp_age
            )
            
            self.person_phone_label.config(
                text = f"{temp_name} {self.check_mobile(temp_mobile_status)}"
            )

            if self.check_mobile(temp_mobile_status) == "has a mobile phone":
                self.person_phone_number_label.config(
                    text = temp_phone_number
                )

                self.f2_phone_number_label.grid(
                    row = 4,
                    column = 0,
                    padx = 20,
                    pady = 5,
                    sticky = W
                )
                
                self.person_phone_number_label.grid(
                    row = 4,
                    column = 1,
                    padx = 20,
                    pady = 5,
                    sticky = W
                )

                self.next_button.grid(
                    row = 5, 
                    column = 1, 
                    sticky = E,
                    padx = 20,
                    pady = 10
                )

                self.previous_button.grid(
                    row = 5, 
                    column = 0, 
                    sticky = W,
                    padx = 20,
                    pady = 10
                )
            else:
                self.previous_button.grid(
                    row = 4, 
                    column = 0, 
                    sticky = W,
                    padx = 20,
                    pady = 10
                )
                self.next_button.grid(
                    row = 4, 
                    column = 1, 
                    sticky = E,
                    padx = 20,
                    pady = 10
                )

                self.person_phone_number_label.grid_forget()

                self.f2_phone_number_label.grid_forget()




    def check_mobile(self, mobile):
        if mobile:
            return "has a mobile phone"
        else:
            return "does not have a mobile phone"
        
    def check_entries(self):
        try:
           self.age.get()
        except TclError:
            messagebox.showwarning("Invalid Input", "You entered an invalid character as your age or phone number, try entering a valid number")
            return False 
        
        if self.age.get() == 0 or self.name.get().strip() == "":
            messagebox.showwarning("Empty Datapoints", "An entry box is missing some data. Please fill out all entries to continue.")
            if self.name_entry.get() == "":
                self.name_entry.focus_set()
            else:
                self.age_entry.focus_set()
            return False
        
        if self.mobile_phone.get():
            phone = self.phone_number.get()
            phone = phone.replace(" ", "")
            if not phone.isdigit():
                messagebox.showwarning("Invalid Phone Number", "You have entered an invalid phone number. Please ensure that your number does not contain any letters and or special characters.")
                return False
            
        if self.age.get() < 0:
            messagebox.showwarning("Invalid Age", "Please enter a valid age to save.")
            return False 
        return True
        
            


    def check_phone_radiobuttons(self):
        if self.mobile_phone.get():
            self.phone_number_label.grid(
                row = 5,
                column = 0,
                padx = 20,
                pady = 5,
                sticky = W
            )
            self.phone_number_entry.grid(
                row = 5,
                column = 1,
                padx = 10,
                pady = 5,
                sticky = W
            )
            self.enter_data_button.grid(
                row = 6, 
                column = 0,
                columnspan = 2,
                pady = 20,
            )
        elif not self.mobile_phone.get():
            self.phone_number_label.grid_forget()
            self.phone_number_entry.grid_forget()
            self.enter_data_button.grid(
                row = 5, 
                column = 0,
                columnspan = 2,
                pady = 20
            )

if __name__ == "__main__":
    root = Tk()
    root.title("GatherInfo")
    app = GetDataGUI(root)
    root.mainloop()