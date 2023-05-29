import math
from datetime import datetime, timedelta
from tkinter import simpledialog, messagebox


def main():
    root = simpledialog.Tk()
    root.withdraw()

    # Total hours of obligatory labor
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


if __name__ == "__main__":
    main()
