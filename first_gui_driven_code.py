import tkinter as tk
from tkinter import messagebox

def calculate_pay():
    try:
        hourly_rate = float(hourly_rate_entry.get())
        hours_worked = float(hours_worked_entry.get())
        state = state_var.get()

        social_security = 0.062
        weeks = 52

        state_tax_rates = {
            "Florida": 0.0,
            "Texas": 0.0625,
            "New York": 0.06,
            "Alabama": 0.04,
            "Alaska": 0.0,
            "Arizona": 0.056,
            "Arkansas": 0.065,
            "California": 0.0725,
            "Colorado": 0.029,
            "Connecticut": 0.0635,
            "Delaware": 0.0,
            "Georgia": 0.04,
            "Hawaii": 0.04,
            "Idaho": 0.06,
            "Illinois": 0.0625,
            "Indiana": 0.07,
            "Iowa": 0.06,
            "Kansas": 0.065,
            "Kentucky": 0.06,
            "Louisiana": 0.045,
            "Maine": 0.050,
            "Maryland": 0.060,
            "Massachusetts": 0.0625,
            "Michigan": 0.060,
            "Minnesota": 0.0688,
            "Mississippi": 0.070,
            "Missouri": 0.0423,
            "Montana": 0.0,
            "Nebraska": 0.050,
            "Nevada": 0.0685,
            "New Hampshire": 0.0,
            "New Jersey": 0.063,
            "New Mexico": 0.0488,
            "North Carolina": 0.0475,
            "North Dakota": 0.05,
            "Ohio": 0.0575,
            "Oklahoma": 0.0450,
            "Oregon": 0.0,
            "Pennsylvania": 0.060,
            "Rhode Island": 0.070,
            "South Carolina": 0.060,
            "South Dakota": 0.042,
            "Tennessee": 0.07,
            "Utah": 0.061,
            "Vermont": 0.06,
            "Virginia": 0.053,
            "Washington": 0.065,
            "West Virginia": 0.06,
            "Wisconsin": 0.050,
            "Wyoming": 0.040,
            "D.C": 0.06
        

        }

        if state in state_tax_rates:
            state_tax = state_tax_rates[state]
        else:
            messagebox.showerror("Error", "Invalid state entered. Please enter Florida, Texas, or New York.")
            return

        initial_pay = hourly_rate * hours_worked
        withholdings = initial_pay * social_security
        state_tax_amount = initial_pay * state_tax
        final_pay = initial_pay - withholdings - state_tax_amount

        yearly_pay = weeks * final_pay
        bi_weekly_pay = final_pay * 2
        monthly_pay = yearly_pay / 13

        result_label.config(text=f"Weekly Pay: {final_pay:.2f}\nBi-Weekly Pay: {bi_weekly_pay:.2f}\nMonthly Pay: {monthly_pay:.2f}\nYearly Pay: {yearly_pay:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numerical values.")

# Create the main window
root = tk.Tk()
root.title("Pay Calculator")

# Create and place widgets
hourly_rate_label = tk.Label(root, text="Hourly Rate:")
hourly_rate_label.pack()
hourly_rate_entry = tk.Entry(root)
hourly_rate_entry.pack()

hours_worked_label = tk.Label(root, text="Hours Worked:")
hours_worked_label.pack()
hours_worked_entry = tk.Entry(root)
hours_worked_entry.pack()

state_label = tk.Label(root, text="State:")
state_label.pack()
state_var = tk.StringVar()
state_dropdown = tk.OptionMenu(root, state_var, "Florida" , "Texas" , "New York" , "Alabama" , "Alaska" , "Arizona" , "Arkansas" , "California", "Colorado" , "Connecticut" , "Delaware" , "Georgia" , 
                               "Hawaii" , "Idaho" , "Illinois" , "Indiana" , "Iowa" , "Kansas" , "Kentucky" , "Louisiana" , "Maine" , "Maryland" , "Massachusetts" , "Michigan" , "Minnesota" , 
                               "Mississippi" , "Missouri" , "Montana" , "Nebraska" , "Nevada" , "New Hampshire" , "New Jersey" , "New Mexico" , "North Carolina" , "North Dakota" , "Ohio" , "Oklahoma" , 
                               "Oregon" , "Pennsylvania" , "Rhode Island" , "South Carolina" , "South Dakota" , "Tennessee" , "Utah" , "Vermont" , "Virginia" , "Washington" , "West Virginia" , "Wisconsin" , "Wyoming" , "D.C")
state_dropdown.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_pay)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
