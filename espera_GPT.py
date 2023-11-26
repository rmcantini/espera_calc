"""import tk and datetime"""

from datetime import datetime
from tkinter import simpledialog, messagebox
import tkinter as tk


def main():
    """The big one function to encapsulate them all"""
    # hide root window
    root = tk.Tk()
    root.withdraw()

    # total hours of obligatory labor
    total_time = "08:00"

    # Asks the registered work hours
    worked_time = simpledialog.askstring(
        "Timesheet+",
        "Digite aqui o total de horas \nregistradas em tasks do dia (00:00)",
    )
    print(worked_time)

    format_h = "%H:%M"  # obviously, formats the number in time stamp format

    # Ask how many clients were worked for
    num_clients = simpledialog.askinteger(
        "Timesheet+",
        "Digite aqui o número de clientes trabalhados",
        min_value=1,
        max_value=100,
    )
    print(num_clients)

    # subtraction of your worked hours from the total
    time_solo = datetime.strptime(total_time, format_h) - datetime.strptime(
        worked_time, format_h
    )

    # divides the wait hours by the number of clients
    time_final = time_solo / num_clients

    # Final result messagebox
    answer = (
        f"Tempo de espera total {
            time_solo}. \nRegistre cada cliente com {time_final}."
    )

    # showinfo only takes 2 arguments
    messagebox.showinfo("Timesheet", answer)


# Calls the thing
main()
