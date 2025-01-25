import csv
import tkinter as tk
from tkinter import *

CSV_FIELDS = [
    "first_number",
    "second_number",
    "added_together",
    "subtracted",
    "multiplied_together",
    "divided",
]


def calculate_and_save(first_number, second_number):
    try:
        first_number = float(first_number)
        second_number = float(second_number)

        addition = first_number + second_number
        subtraction = first_number - second_number
        multiplication = first_number * second_number
        division = first_number / second_number

        result_label.config(text=f"Addition: {addition} Subtraction: {subtraction}\nMultiplication: {multiplication} Division: {division}")

        rows = [
            first_number,
            second_number,
            addition,
            subtraction,
            multiplication,
            division,
        ]

        filename = "./../data/results.csv"

        # append to the csv file
        with open(filename, "a", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(rows)

    except ValueError:  # user input validation
        error_label.config(text="SYNTAX ERROR! Please insert valid numbers.")
    except ZeroDivisionError:
        error_label.config(text="MATH ERROR! Can't divide by zero.")
    except FileNotFoundError:  # if we can't find the csv file => create one
        with open(filename, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(CSV_FIELDS)
            csv_writer.writerow(rows)


# GUI
master = tk.Tk()
master.title("Simple Calculator")
master.minsize(720, 300)

tk.Label(master, text="First Number").grid(row=0, column=1, padx=20, pady=10)
tk.Label(master, text="Second Number").grid(row=0, column=2, padx=20, pady=10)

entry_first_number = tk.Entry(master)
entry_first_number.grid(row=1, column=1, padx=20)

entry_second_number = tk.Entry(master)
entry_second_number.grid(row=1, column=2, padx=20)

error_label = tk.Label(master, text="", fg="red")
error_label.grid(row=2, column=0, columnspan=4, padx=10)

result_label = tk.Label(master, text="", fg="green")
result_label.grid(row=2, column=0, columnspan=4, padx=10)

tk.Button(
    master,
    text="Calculate",
    command=lambda: [
        result_label.config(text=""),
        error_label.config(text=""),
        calculate_and_save(entry_first_number.get(), entry_second_number.get()),
    ],
).grid(row=4, column=0, columnspan=4, pady=20)

master.mainloop()
