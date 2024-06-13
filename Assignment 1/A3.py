import tkinter as tk
from tkinter import ttk, messagebox,filedialog
import os

class User_profile:
    
    def __init__(self) :
        
        
        # creat Main Title
        self.user_form = tk.Tk()
        self.user_form.title("User Profile Form")  
        self.user_form.geometry("800x500") 
        self.user_screen_width = self.user_form.winfo_screenwidth()
        self.user_screen_height = self.user_form.winfo_screenheight()
        
        self.backgroud_frame = tk.Frame(self.user_form,width=self.user_screen_width,height=self.user_screen_height ,bg="#000929")
        self.backgroud_frame.pack()
        
        self.left_frame = tk.Frame(self.user_form, bg="#00072D",width=self.user_screen_width // 6 ,height=self.user_screen_height)
        self.left_frame.pack(side=tk.LEFT)
         
        
        self.Profile_label = tk.Label(self.user_form, text="User Profile Form")
        self.Profile_label.pack()
        self.Profile_label.place(x=400,y=30, anchor="center")
        self.Profile_label.config(bg="#155f80")
        
        self.user_label1 = tk.Label(self.user_form,text="Enter First Name:")
        self.user_label1.pack()
        self.user_label1.place(x=80,y=70,anchor="center")
        
        self.user_label2 = tk.Label(self.user_form,text="Enter Last Name:")
        self.user_label2.pack()
        self.user_label2.place(x=80,y=100,anchor="center")
        
        self.user_label3 = tk.Label(self.user_form,text="Enter Mobile Number:")
        self.user_label3.pack()
        self.user_label3.place(x=80,y=130,anchor="center")

        self.user_label4 = tk.Label(self.user_form,text="Select Profile Photo: No Profile Photo")
        self.user_label4.pack()
        self.user_label4.place(x=150,y=170,anchor="center")    
        
        self.user_label5 = tk.Label(self.user_form,text="Height (cm) :")
        self.user_label5.pack()
        self.user_label5.place(x=70,y=310,anchor="center")     
           
        # Create Enter Line
        
        self.user_label1 = tk.Entry(self.user_form,text="")
        self.user_label1.insert(0,"")
        self.user_label1.pack(side="right")
        self.user_label1.place(x=350, y=70, anchor="center")   
        
        self.user_label2 = tk.Entry(self.user_form,textvariable="")
        self.user_label2.pack(side="right")
        self.user_label2.place(x=350, y=100, anchor="center")   
        
        self.user_label3 = tk.Entry(self.user_form,textvariable="")
        self.user_label3.pack(side="right")
        self.user_label3.place(x=350, y=130, anchor="center")   
        
        self.user_label5 = tk.Entry(self.user_form,textvariable="")
        self.user_label5.pack()
        self.user_label5.place(x=350,y=310,anchor="center")  
        
    # Create Gender
        self.user_label6 = tk.Label(self.user_form,text="Gender :")
        self.user_label6.pack()
        self.user_label6.place(x=50,y=250,anchor="center")   
        
        self.Gender_user = tk.StringVar()
        self.Gender_user.set("Male")

        
        
    # Create Button 
        self.photo_button = ttk.Button(self.user_form,text="select Photo", style="Rounded.TButton", command=self.Get_photo)
        self.photo_button.pack()
        self.photo_button.place(x=180, y=200, anchor="center")
        
        self.G_button1 = tk.Radiobutton(self.user_form,text="Male" ,value="Male",variable=self.Gender_user)
        self.G_button1.pack()
        self.G_button1.place(x=150,y=250, anchor="center")
        
        self.G_button2 = tk.Radiobutton(self.user_form,text="Female" ,value="Female",variable=self.Gender_user)
        self.G_button2.pack()
        self.G_button2.place(x=160,y=280, anchor="center")
        
        self.submit_button = ttk.Button(self.user_form,text="Submit", style="Rounded.TButton", command=self.show_Msg)
        self.submit_button.pack()
        self.submit_button.place(x=350,y=350, anchor="center")
        
        
    def show_Msg(self):
        First_Name = self.user_label1.get()
        Last_name = self.user_label2.get()
        Mo_number = self.user_label3.get()
        Gender = self.Gender_user.get()
        height = self.user_label5.get()
        
        print(f"First Name : {First_Name}")
        print(f"Last Name : {Last_name}")
        print(f"Mobile Number : {Mo_number}")
        print(f"Gender: {Gender}")
        print(f"Height : {height}")
        
    def msg(self):
        messagebox.showinfo(self.user_form,self.show_Msg)
    
                
        
        
        
    def Get_photo(self):
        self.file_path = filedialog.askopenfilename(title="Select Photo",filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    
    
        
        
             
        
        
        
    def run(self):
        self.user_form.mainloop()
        
        
if __name__=="__main__":
    app = User_profile()
    app.run()