''' import tk and datetime '''
from datetime import datetime
from tkinter import simpledialog
import tkinter.messagebox
import tkinter as tk

# hide root window
root = tk.Tk()
root.withdraw()

# total hours of obligatory labor
TOTALTIME = '08:00'

# Asks the registered work hours
workedTime = simpledialog.askstring(
    'Timesheet+', 'Digite aqui o total de horas \nregistradas em tasks do dia (00:00)')

FORMAT = '%H:%M'  # obviously, formats the number in time stamp format

# subtraction of your worked hours from the total
timeSolo = datetime.strptime(TOTALTIME, FORMAT) - \
    datetime.strptime(workedTime, FORMAT)
timeFinal = timeSolo / 2  # divides the wait hours by the 2 client segments

# Final result messagebox
A = 'Tempo de espera total: ' + str(timeSolo) + ' >> '  # total time result
B = 'Registre em ambos, Super e Eletro:' + \
    str(timeFinal)  # text part for result splitted in 2

# join tex part and number result
ANSWER = A + B

# showinfo only takes 2 arguments
tkinter.messagebox.showinfo('Timesheet', ANSWER)
