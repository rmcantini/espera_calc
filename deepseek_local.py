import math
from datetime import datetime, timedelta
from tkinter import (
    Tk,
    ttk,
    messagebox,
    simpledialog,
    LEFT,
    X
)
from tkinter.ttk import Frame, Label, Entry, Button

def center_window(window):
    """Centers the given window on the screen."""
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"+{x}+{y}")

def create_custom_style():
    """Creates and applies custom styling for the application."""
    style = ttk.Style()
    
    # Configure styles for Apple visual guidelines
    style.configure(
        "CustomLabel.TLabel",
        font=(None, 14),
        foreground="#202020",
        background="#f5f5f5"
    )
    
    style.configure(
        "CustomButton.TButton",
        padding=(10, 5),
        font=(None, 12),
        foreground="#ffffff",
        background="#0a84bb",
        bordercolor="#0a76a8",
        relief="flat"
    )
    
    style.map("CustomButton.TButton", 
              background=[("active", "#0075b2"), ("!focus", "#0a84bb")])

def create_input_frame(root, label_text):
    """Creates a styled input frame with a label and entry field."""
    frame = ttk.Frame(root)
    frame.pack(pady=5)
    
    Label(frame, text=label_text, style="CustomLabel.TLabel").pack(side=LEFT, padx=5)
    
    return frame

class WorkTimeCalculator:
    """A class to handle the work time calculator functionality."""
    
    def __init__(self, root):
        self.root = root
        self.worked_hours_entry = None
        self.clients_entry = None
        self.results_label = None
        
        # Set up styles
        create_custom_style()
        
        # Create main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(pady=10)
        
        # Input fields
        self.create_input_fields()
        
        # Buttons
        self.create_buttons()
    
    def create_input_fields(self):
        """Creates and organizes input fields."""
        inputs_frame = LabelFrame(
            self.main_frame, 
            text="Inputs",
            padding=(5, 10)
        )
        inputs_frame.pack(padx=10, pady=5, expand=True)
        
        # Worked Hours
        worked_hours_frame = create_input_frame(inputs_frame, "Worked Hours (HH:MM)")
        self.worked_hours_entry = Entry(worked_hours_frame, width=8)
        self.worked_hours_entry.pack(side=LEFT, padx=5)
        
        # Number of Clients
        clients_frame = create_input_frame(inputs_frame, "# of Clients")
        self.clients_entry = Entry(clients_frame, width=8)
        self.clients_entry.pack(side=LEFT, padx=5)
    
    def create_buttons(self):
        """Creates and organizes buttons."""
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.pack(pady=10)
        
        # Calculate Button
        calculate_button = Button(
            buttons_frame,
            text="Calculate",
            style="CustomButton.TButton",
            command=self.calculate
        )
        calculate_button.pack(side=LEFT, padx=5)
        
        # Clear Button
        clear_button = Button(
            buttons_frame,
            text="Clear",
            style="CustomButton.TButton",
            command=self.clear_inputs
        )
        clear_button.pack(side=LEFT, padx=5)
    
    def calculate(self):
        """Handles the calculation of work time."""
        try:
            # Total hours of obligatory labor (8 hours)
            total_time = datetime.strptime("08:00", "%H:%M")

            # Asks the registered work hours
            worked_time = datetime.strptime(
                simpledialog.askstring(
                    "Timesheet+",
                    "Digite aqui o total de horas registradas em tasks do dia (00:00)",
                ),
                "%H:%M",
            )

            # Ask how many clients were worked for
            num_clients = simpledialog.askinteger(
                "Timesheet+",
                "Digite aqui o número de clientes trabalhados",
                minvalue=1,
                maxvalue=100,
            )

            # Subtraction of your worked hours from the total
            time_solo = total_time - worked_time

            # Divides the wait hours by the number of clients and round up
            time_final = time_solo / num_clients
            time_in_minutes = time_final.total_seconds() / 60
            time_final_rounded = timedelta(minutes=math.ceil(time_in_minutes))

            # Final result messagebox
            answer = (
                f"Tempo de espera total {time_solo}. \n"
                f"Registre cada cliente com {time_final_rounded}."
            )

            messagebox.showinfo("Timesheet", answer)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_inputs(self):
        """Resets all input fields and results."""
        self.worked_hours_entry.delete(0, 'end')
        self.clients_entry.delete(0, 'end')
        if self.results_label:
            self.results_label.destroy()
        self.results_label = None

if __name__ == "__main__":
    root = Tk()
    WorkTimeCalculator(root)
    center_window(root)
    root.mainloop()
