import time
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the clock
clock_label = tk.Label(root, font=("Helvetica", 40), fg="black")
clock_label.pack()

# Define the clock update function
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)  # Update every 1000ms (1 second)

# Initialize the clock
update_clock()
root.mainloop()