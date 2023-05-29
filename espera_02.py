"""#import tk and datetime"""
from datetime import datetime
from tkinter import simpledialog
import tkinter.messagebox
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

    # subtraction of your worked hours from the total
    time_solo = datetime.strptime(total_time, format_h) - datetime.strptime(
        worked_time, format_h
    )
    time_final = time_solo / 2  # divides the wait hours by the 2 client segments

    # Final result messagebox
    answer = f"Tempo de espera total {time_solo}. \nRegistre ambos, \
Super e Eletro, com {time_final} cada."

    # showinfo only takes 2 arguments
    tkinter.messagebox.showinfo("Timesheet", answer)


# Calls the thing
main()
