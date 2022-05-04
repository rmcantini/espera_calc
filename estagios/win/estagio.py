# import tk and datetime
from datetime import datetime
from tkinter import Tk, simpledialog
import tkinter.messagebox
import tkinter as tk

# hide root window
root = tk.Tk()
root.withdraw()

# total hours of obligatory labor
totalTime = '06:00'

# Asks the registered work hours
workedTime = simpledialog.askstring(
    'Timesheet+', 'Digite aqui o total de horas \nregistradas em tasks do dia (00:00)')
print = (workedTime)

format = '%H:%M'  # obviously, formats the number in time stamp format

# subtraction of your worked hours from the total
timeSolo = datetime.strptime(totalTime, format) - \
    datetime.strptime(workedTime, format)
timeFinal = timeSolo / 2  # divides the wait hours by the 2 client segments

# Final result messagebox
a = 'Tempo de espera total: ' + str(timeSolo) + ' >> '  # total time result
b = 'Registre em ambos, Super e Eletro:' + \
    str(timeFinal)  # text part for result splited in 2

# join tex part and number result
answer = a + b

# showinfo only takes 2 arguments
tkinter.messagebox.showinfo('Timesheet', answer)
