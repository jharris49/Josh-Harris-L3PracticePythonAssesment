from tkinter import *
from tkinter import messagebox



class GetDataGUI:
    def __init__(self, parent):

        self.collecting_data_label = Label(
            parent,
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
            parent,
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
            parent,
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
            parent,
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
            parent,
            text = "Show All"
        )
        self.show_button.grid(
            row = 0, 
            column = 1, 
            sticky = W,
            padx = 10
        )

        self.first_name = StringVar()
        self.first_name_entry = Entry(
            parent,
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
            parent,
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
            parent,
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
            parent,
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
            parent,
            text = "Enter Data"
        )
        self.enter_data_button.grid(
            row = 5, 
            column = 0,
            columnspan = 2,
            pady = 20
        )


        self.display_data_label = Label(
            parent,
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
            parent,
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
            parent,
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
            parent,
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
            parent,
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
            parent,
            text = "Add New Person",
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
            parent,
            text = "(name)"
        )
        self.person_name_label.grid(
            row = 1, 
            column = 1,  
            sticky = W, 
            padx = 10
        )

        self.person_age_label = Label(
            parent,
            text = "(age)"
        )
        self.person_age_label.grid(
            row = 2, 
            column = 1,  
            sticky = W, 
            padx = 10
        )

        self.next_button = Button(
            parent,
            text = "Next"
        )
        self.next_button.grid(
            row = 4, 
            column = 1, 
            sticky = E,
            padx = 20,
            pady = 10
        )

if __name__ == "__main__":
    root = Tk()
    root.title("GatherInfo")
    app = GetDataGUI(root)
    root.mainloop()