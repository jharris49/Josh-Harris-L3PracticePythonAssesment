from tkinter import *
from tkinter import messagebox



class GetDataGUI:
    def __init__(self, parent):
        self.data_collection_frame = Frame(parent)
        self.display_data_frame = Frame(parent)
        self.current_frame = 1
        
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
            text = "First name:"
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
            command = self.switch_frame
        )
        self.show_button.grid(
            row = 0, 
            column = 1, 
            sticky = W,
            padx = 10
        )

        self.first_name = StringVar()
        self.first_name_entry = Entry(
            self.data_collection_frame,
            textvariable = self.first_name
        )
        self.first_name_entry.grid(
            row = 1,
            column = 1, 
            sticky = W,
            padx = 10
        )

        self.age = IntVar()
        self.age_entry = Entry(
            self.data_collection_frame,
            textvariable = self.age
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
            text = "No"
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
            text = "Yes"
        )
        self.phone_radiobutton_true.grid(
            row = 4,
            column = 1, 
            sticky = W,
            padx = 10
        )

        self.enter_data_button = Button(
            self.data_collection_frame,
            text = "Enter Data"
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
            text = "First name:"
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

        self.previous_button = Button(
            self.display_data_frame,
            text = "Previous"
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
            text = "Next"
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
        if self.current_frame == 1:
            self.data_collection_frame.grid_forget()
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
        


if __name__ == "__main__":
    root = Tk()
    root.title("GatherInfo")
    app = GetDataGUI(root)
    root.mainloop()