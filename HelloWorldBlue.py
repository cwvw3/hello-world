import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello, World!")
root.geometry("400x200")  # Set the window sizepy
root.configure(bg="white")

# Create a frame to center the textbox
frame = tk.Frame(root, bg="black")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create the textbox
textbox = tk.Label(frame, text="Hello, World!", bg="green", fg="white", font=("Arial", 20), padx=20, pady=10)
textbox.pack()

# Run the application
root.mainloop()