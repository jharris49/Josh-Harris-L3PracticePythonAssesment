"""This file is collects and outputs different peoples data.

It essentiallly acts like a contact or phone book, holding peoples
names and contact information.
"""

from tkinter import *
from tkinter import messagebox


class Person:
    """The framework that represents a persons attributes.

    This class forms the framework for peoples inrformation
    to be saved as a Person object, including name,
    age, phone status, and phone number.
    """

    def __init__(self, name, age, phone_status, phone_number=None):
        """Framework for the Person class.

        This takes the positional arguments during the
        creation of a Person object and assigns them to
        instance variables so the data is saved and
        can be used later on in the program.

        Parameters:
        name (str) -- the name of a person
        age (int) -- the age of a person
        phone_status (bool) -- if the person has a
        phone or not, true or false
        phone_number (str) -- the phone number of a person
        if they have one (default None)
        """
        self.name = name
        self.age = age
        self.phone_status = phone_status
        self.phone_number = phone_number


class GetDataGUI:
    """Forms the GUI.

    This class forms the graphical user interface
    for the application. It holds methods that manage
    input validation, frame switching,
    person object creation, and widget creation
    and updates.
    """

    def __init__(self, parent):
        """Create Base UI for GUI.

        This creates instance variables for widgets
        and data saving. Lays down the basic UI
        for the GUI, which can then later be adapted
        and changed through the methods in the
        class.
        """

        # Creates empty list for later storage of Person objects.
        self.persons = []
        self.person_counter = 0

        # Creates both frames for GUI, for both data input and output.
        self.data_collection_frame = Frame(parent)
        self.display_data_frame = Frame(parent)
        # Keeps track of current frame, automatically 1 (data collection frame)
        self.current_frame = 1

        self.phone_number_label = Label(
            self.data_collection_frame,
            text="Enter your phone number:"
        )

        # Collects phone number if gridded.
        self.phone_number = StringVar()
        self.phone_number_entry = Entry(
            self.data_collection_frame,
            textvariable=self.phone_number
        )

        self.collecting_data_label = Label(
            self.data_collection_frame,
            text="Collecting Person Data"
        )
        self.collecting_data_label.grid(
            row=0,
            column=0,
            sticky=W,
            padx=20,
            pady=20
        )

        self.name_label = Label(
            self.data_collection_frame,
            text="Name:"
        )
        self.name_label.grid(
            row=1,
            column=0,
            sticky=W,
            padx=20,
            pady=5
        )

        self.age_label = Label(
            self.data_collection_frame,
            text="Age:"
        )
        self.age_label.grid(
            row=2,
            column=0,
            sticky=W,
            padx=20,
            pady=5
        )

        self.phone_label = Label(
            self.data_collection_frame,
            text="Do you have a mobile phone?"
        )
        self.phone_label.grid(
            row=3,
            column=0,
            sticky=W,
            padx=20,
            pady=5
        )

        # Triggers a method that switches to data output frame.
        self.show_button = Button(
            self.data_collection_frame,
            text="Show All",
            command=self.switch_frame,
        )
        self.show_button.grid(
            row=0,
            column=1,
            sticky=W,
            padx=10
        )

        # Collects name
        self.name = StringVar()
        self.name_entry = Entry(
            self.data_collection_frame,
            textvariable=self.name
        )
        self.name_entry.grid(
            row=1,
            column=1,
            sticky=W,
            padx=10
        )

        # Collects age
        self.age = IntVar()
        self.age_entry = Spinbox(
            self.data_collection_frame,
            textvariable=self.age,
            from_=0,
            to=200,
        )
        self.age_entry.grid(
            row=2,
            column=1,
            sticky=W,
            padx=10
        )

        # Value for radio button
        self.mobile_phone = BooleanVar()
        # Sets first value for radiobutton to false
        self.mobile_phone.set(False)

        # Lets the user input if they have a a phone or not
        self.phone_radiobutton_false = Radiobutton(
            self.data_collection_frame,
            variable=self.mobile_phone,
            value=False,
            text="No",
            command=self.check_phone_radiobuttons
        )
        self.phone_radiobutton_false.grid(
            row=3,
            column=1,
            sticky=W,
            padx=10
        )

        # Lets the user input if they have a a phone or not
        self.phone_radiobutton_true = Radiobutton(
            self.data_collection_frame,
            variable=self.mobile_phone,
            value=True,
            text="Yes",
            command=self.check_phone_radiobuttons
        )
        self.phone_radiobutton_true.grid(
            row=4,
            column=1,
            sticky=W,
            padx=10
        )

        # Triggers a method that saves data
        self.enter_data_button = Button(
            self.data_collection_frame,
            text="Enter Data",
            command=self.save_person
        )
        self.enter_data_button.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=20
        )

        self.display_data_label = Label(
            self.display_data_frame,
            text="Displaying Person Data"
        )
        self.display_data_label.grid(
            row=0,
            column=0,
            sticky=W,
            padx=20,
            pady=20
            )

        self.f2_name_label = Label(
            self.display_data_frame,
            text="Name:"
        )
        self.f2_name_label.grid(
            row=1,
            column=0,
            sticky=W,
            padx=20,
            pady=5
        )

        self.f2_age_label = Label(
            self.display_data_frame,
            text="Age:"
        )
        self.f2_age_label.grid(
            row=2,
            column=0,
            sticky=W,
            padx=20,
            pady=5
        )

        self.person_phone_label = Label(
            self.display_data_frame,
            text="(name) has a mobile phone"
        )
        self.person_phone_label.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=20,
            pady=5
        )

        self.f2_phone_number_label = Label(
            self.display_data_frame,
            text="Phone Number:"
        )

        self.person_phone_number_label = Label(
            self.display_data_frame,
            text="(number)"
        )

        # Triggers a method that switches the object that is outputted.
        self.previous_button = Button(
            self.display_data_frame,
            text="Previous",
            command=lambda: self.output_data(-1)
        )
        self.previous_button.grid(
            row=4,
            column=0,
            sticky=W,
            padx=20,
            pady=10
        )

        # Triggers a method that switches to data input frame.
        self.add_person_button = Button(
            self.display_data_frame,
            text="Add New Person",
            command=self.switch_frame,
            anchor=W,
            padx=10
        )
        self.add_person_button.grid(
            row=0,
            column=1,
            sticky=W,
            padx=10
        )

        self.person_name_label = Label(
            self.display_data_frame,
            text="(name)"
        )
        self.person_name_label.grid(
            row=1,
            column=1,
            sticky=W,
            padx=10
        )

        self.person_age_label = Label(
            self.display_data_frame,
            text="(age)"
        )
        self.person_age_label.grid(
            row=2,
            column=1,
            sticky=W,
            padx=10
        )

        # Triggers a method that switches the object that is outputted.
        self.next_button = Button(
            self.display_data_frame,
            text="Next",
            command=lambda: self.output_data(1)
        )
        self.next_button.grid(
            row=4,
            column=1,
            sticky=E,
            padx=20,
            pady=10
        )

        self.data_collection_frame.grid()
      

    def switch_frame(self):
        """Switches frames.
        
        This method switches the frame shown to a user. It controls the toggle
        between the two frames that the program has.
        """

        """Checks if the length of the list is zero. 
        
        Before letting a user switch frame by hittting the save data button
        this checks if the length of the list is zero. If it is zero,
        it prevents that from occuring and shows the user a message.
        """
        if len(self.persons) == 0:
            messagebox.showerror("No Data Saved", "You have not saved any data yet. " \
            "Save data first before trying to view it.")
            self.name_entry.focus_set()
        # Switches frame.
        else:
            # Checks current frame.
            if self.current_frame == 1:
                # Hides data collection frame
                self.data_collection_frame.grid_forget()
                # Reconfigures display data frame through output data
                self.output_data(0)
                # Grids (shows) display data frame so the user can say
                self.display_data_frame.grid()
                # Updates current frame
                self.current_frame = 2
                target_frame = self.display_data_frame
            else:
                # Hides display data frame
                self.display_data_frame.grid_forget()
                # Grids (shows) data collection frame
                self.data_collection_frame.grid()
                # Updates current frame
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
        """Creates a new person object.
        
        This method adds creates a new person object with the inputted data and adds it to the persons list.
        It also resets the UI of the input data frame and displays a messagebox to notify the user that the
        data has been succesfyully saved.
        """
        # Checks if all of the user input is valid, if not it does not create and append a new object to persons
        if self.check_entries():
            self.persons.append(Person(self.name.get(), self.age.get(), 
                                self.mobile_phone.get(), self.phone_number.get().replace(" ", ""))
                            )
            messagebox.showinfo("Data Saved!", "This data has been saved.")
            self.name.set("")
            self.age.set(0)
            self.phone_number.set("")
            self.name_entry.focus_set()


    def output_data(self, status):
        """Gets and outputs data for data display frame.

        This method gets all of the data from a user chosen person
        object and outputs all of the data (instance variables)
        saved to that person.

        Parameters:
        status (int) -- the status of output data, if the user
        wants to output the previous or next object (-1, 0, 1)
        """
        # Adds status to person counter for list index handling
        self.person_counter += status
        """Checks if the length of the persons list is equal to person counter.
        
        If this is true it means that this datapoint is the last one in the list.
        Also checks if less than 0, which means that it is the first object in the
        list. This then triggers an error message to prevent the list index from being
        out of range.
        """
        if len(self.persons) == self.person_counter or self.person_counter < 0 :
            messagebox.showerror("Not more data", "You cannot see anymore data as there "
            "is no more data to display. Try entering more data.")
            # Subtracts status from person counter to keep list index the same once the user hits a button again
            self.person_counter -= status
        else:
            # Gets all instance variables from selected object and sets them to temporary variables
            temp_name = self.persons[self.person_counter].name
            temp_age = self.persons[self.person_counter].age
            temp_mobile_status = self.persons[self.person_counter].phone_status
            temp_phone_number = self.persons[self.person_counter].phone_number

            # Configures previous labels adding the new temporary instance variables
            self.person_name_label.config(
                text=temp_name
            )
            self.person_age_label.config(
                text=temp_age
            )
            
            self.person_phone_label.config(
                text=f"{temp_name} {self.check_mobile(temp_mobile_status)}"
            )

            # Checks if user has phone, and configures more labels accordingly
            if self.check_mobile(temp_mobile_status) == "has a mobile phone":
                self.person_phone_number_label.config(
                    text=temp_phone_number
                )

                self.f2_phone_number_label.grid(
                    row=4,
                    column=0,
                    padx=20,
                    pady=5,
                    sticky=W
                )
                
                self.person_phone_number_label.grid(
                    row=4,
                    column=1,
                    padx=20,
                    pady=5,
                    sticky=W
                )

                self.next_button.grid(
                    row=5,
                    column=1,
                    sticky=E,
                    padx=20,
                    pady=10
                )

                self.previous_button.grid(
                    row=5,
                    column=0,
                    sticky=W,
                    padx=20,
                    pady=10
                )
            
            # Reverts frame back to what it looks like if a person does not have a phone number
            else:
                self.previous_button.grid(
                    row=4,
                    column=0,
                    sticky=W,
                    padx=20,
                    pady=10
                )
                self.next_button.grid(
                    row=4,
                    column=1,
                    sticky=E,
                    padx=20,
                    pady=10
                )

                self.person_phone_number_label.grid_forget()

                self.f2_phone_number_label.grid_forget()



    def check_mobile(self, mobile):
        """Checks if user has a mobile phone.
         
        This method checks if a user has a mobile phone and returns a formatted string to be used in a label.

        Parameters:
        mobile (bool) -- if a user has a mobile phone or not

        Returns:
        a formatted string
        """
        if mobile:
            return "has a mobile phone"
        else:
            return "does not have a mobile phone"


    def check_entries(self):
        """Checks validity of user input.
    
        This method handles all input validation for widgets
        that take user input. Returning a bool based on if the
        entries are valid or not (valid: true, invalid: false)
        which is later used in an if statement. It handles the UI
        if something is invalid and prevents invalid input from
        being saved in a person object.

        Returns:
        bool
        """
        try:
           # Tries to get age, you cannot get age if it is not an int and or contains invalid characters as age is an IntVar.
           self.age.get()
        # Handles error if you cannot get age. Shows a warning.
        except TclError:
            messagebox.showwarning("Invalid Input", "You entered an invalid character as your " \
            "age or phone number, try entering a valid number")
            return False
        
        # Checks if input widgets are left blank and if they are shows a warning. 
        if self.age.get() == 0 or self.name.get().strip() == "":
            messagebox.showwarning("Empty Datapoints", "An entry box is missing some data. " \
            "Please fill out all entries to continue.")
            # Checks what is left blank and shifts users typing (focus) into the blank input widget.
            if self.name_entry.get() == "":
                self.name_entry.focus_set()
            else:
                self.age_entry.focus_set()
            return False
        
        # Checks if the object has a mobile phone.
        if self.mobile_phone.get():
            # Sets objects specifc phone number to a temporary variable.
            phone = self.phone_number.get()
            # Removes all blank and syntac spaces from phone number.
            phone = phone.replace(" ", "")
            # Checks if phone number contains anything but numbers. Shows a warning if it has anything but numbers.
            if not phone.isdigit():
                messagebox.showwarning("Invalid Phone Number", "You have entered an invalid phone number. " \
                "Please ensure that your number does not contain any letters and or special characters.")
                return False
        
        # Checks if age is less than 0 and shows warning if this is true.
        if self.age.get() < 0:
            messagebox.showwarning("Invalid Age", "Please enter a valid age to save.")
            return False 

        # Returns true if all if statements do not run (the data is valid).
        return True
        

    def check_phone_radiobuttons(self):
        """Checks radiobuttons value and formats frame accordingly.

        This method gets the value used in the radiobuttons, checks if it is true or false,
        and then formats the input data frame accordingly.
        """
        # Checks if the user has a mobile phone.
        if self.mobile_phone.get():
            # Formatts frame and widgets if a user has a mobile phone.
            self.phone_number_label.grid(
                row=5,
                column=0,
                padx=20,
                pady=5,
                sticky=W
            )
            self.phone_number_entry.grid(
                row=5,
                column=1,
                padx=10,
                pady=5,
                sticky=W
            )
            self.enter_data_button.grid(
                row=6,
                column=0,
                columnspan=2,
                pady=20,
            )
        # Formats if a user does not have a mobile phone.
        elif not self.mobile_phone.get():
            self.phone_number_label.grid_forget()
            self.phone_number_entry.grid_forget()
            self.enter_data_button.grid(
                row=5,
                column=0,
                columnspan=2,
                pady=20
            )

if __name__ == "__main__":
    root = Tk()
    root.title("GatherInfo")
    app = GetDataGUI(root)
    root.mainloop()