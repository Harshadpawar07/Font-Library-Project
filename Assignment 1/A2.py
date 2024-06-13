import tkinter as tk
from tkinter import filedialog

class UserProfileForm:
    def __init__(self, master):
        self.master = master
        self.master.title("User Profile Form")

        self.create_widgets()

    def create_widgets(self):
        # Name
        self.label_name = tk.Label(self.master, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="e", padx=10, pady=5)

        self.entry_name = tk.Entry(self.master)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        # Photo
        self.label_photo = tk.Label(self.master, text="Photo:")
        self.label_photo.grid(row=1, column=0, sticky="e", padx=10, pady=5)

        self.photo_path = tk.StringVar()
        self.entry_photo = tk.Entry(self.master, textvariable=self.photo_path, state="disabled")
        self.entry_photo.grid(row=1, column=1, padx=10, pady=5)

        self.button_browse = tk.Button(self.master, text="Browse", command=self.browse_photo)
        self.button_browse.grid(row=1, column=2, padx=5, pady=5)

        # Gender
        self.label_gender = tk.Label(self.master, text="Gender:")
        self.label_gender.grid(row=2, column=0, sticky="e", padx=10, pady=5)

        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")

        self.radio_male = tk.Radiobutton(self.master, text="Male", variable=self.gender_var, value="Male")
        self.radio_male.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.radio_female = tk.Radiobutton(self.master, text="Female", variable=self.gender_var, value="Female")
        self.radio_female.grid(row=2, column=1, padx=10, pady=5, sticky="e")

        # Submit Button
        self.button_submit = tk.Button(self.master, text="Submit", command=self.submit_form)
        self.button_submit.grid(row=3, column=1, pady=10)

    def browse_photo(self):
        file_path = filedialog.askopenfilename(title="Select Photo", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.photo_path.set(file_path)

    def submit_form(self):
        name = self.entry_name.get()
        photo_path = self.photo_path.get()
        gender = self.gender_var.get()

        print(f"Name: {name}")
        print(f"Photo Path: {photo_path}")
        print(f"Gender: {gender}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserProfileForm(root)
    root.mainloop()
