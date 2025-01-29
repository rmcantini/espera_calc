import tkinter as tk
from tkinter import messagebox

def center_window(window):
    """Center any window on the screen"""
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'+{x}+{y}')

def parse_hhmm_to_minutes(time_str):
    """Convert HH:MM format to total minutes"""
    try:
        hours, minutes = map(int, time_str.split(':'))
        if minutes < 0 or minutes >= 60:
            return None
        return hours * 60 + minutes
    except:
        return None

def format_minutes_to_hhmm(total_minutes):
    """Convert total minutes to HH:MM format"""
    total_minutes = round(total_minutes)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours:02d}:{minutes:02d}"

def show_results():
    # Get input values
    worked_time = hours_entry.get().strip()
    clients = clients_entry.get().strip()
    
    # Validate inputs
    try:
        worked_minutes = parse_hhmm_to_minutes(worked_time)
        if worked_minutes is None:
            raise ValueError("Invalid time format")
            
        num_clients = int(clients)
        if num_clients <= 0:
            raise ValueError("Invalid client number")
            
        # Calculate values
        standby_minutes = max(0, 480 - worked_minutes)  # 8 hours = 480 minutes
        avg_minutes = worked_minutes / num_clients
        
        # Format results
        total_worked = format_minutes_to_hhmm(worked_minutes)
        standby_time = format_minutes_to_hhmm(standby_minutes)
        avg_time = format_minutes_to_hhmm(avg_minutes)
        
        # Create results window
        result_window = tk.Toplevel(root)
        result_window.title("Work Report")
        
        # Create result text
        result_text = (
            f"Work Summary:\n\n"
            f"Total available time: 08:00\n"
            f"Total worked time:   {total_worked}\n"
            f"Clients served:      {num_clients}\n"
            f"Average per client:  {avg_time}\n"
            f"Standby time:        {standby_time}"
        )
        
        # Display results
        tk.Label(result_window, text=result_text, font=("Arial", 12), 
                justify=tk.LEFT, padx=24, pady=24).pack()
        
        # Center the results window
        center_window(result_window)
        
    except ValueError as e:
        messagebox.showerror("Error", 
            "Invalid input:\n"
            "- Work time must be in HH:MM format\n"
            "- Clients must be a positive integer")


# Create main window
root = tk.Tk()
root.title("Work Time Calculator")

# Create main container
main_frame = tk.Frame(root, padx=24, pady=24)
main_frame.pack(expand=False)

# Create widgets
tk.Label(main_frame, text="Work Time Calculator", 
        font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(main_frame, text="Worked Time (HH:MM):").grid(row=1, column=0, sticky=tk.W, pady=5)
hours_entry = tk.Entry(main_frame)
hours_entry.grid(row=1, column=1, pady=5)

tk.Label(main_frame, text="Number of Clients:").grid(row=2, column=0, sticky=tk.W, pady=5)
clients_entry = tk.Entry(main_frame)
clients_entry.grid(row=2, column=1, pady=5)

submit_btn = tk.Button(main_frame, text="Calculate", command=show_results, 
                      bg="#4CAF50", fg="white", padx=10)
submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

# Center the main window after initial setup
center_window(root)

root.mainloop()
