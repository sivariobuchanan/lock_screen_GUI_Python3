import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("600x440")
app.title('solour V1.0.0')


def button_function():
    key1 = "rick"
    key2 = "morty"

    # Get the entered key1 and key2 from the entry fields
    entered_key1 = entry1.get()
    entered_key2 = entry2.get()

    # Check if the entered credentials match the expected credentials
    if entered_key1 == key1 and entered_key2 == key2:
        app.destroy()  # destroy current window and creating new one
        w = customtkinter.CTk()
        w.geometry("1280x720")
        w.title('Welcome')

        # Create a canvas widget and display the image on it
        canvas = tkinter.Canvas(w, width=800, height=600)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open("3.jpg"))
        canvas.create_image(500, 10, image=img)

        ll1 = customtkinter.CTkLabel(master=w, text="STILL BUILDING THIS PAGE", font=('Century Gothic', 60))
        ll1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        w.mainloop()
    else:
        # Display an error message if the credentials don't match
        tkinter.messagebox.showerror("WARNING!!!", "INVALID KEYS! ")


img1 = ImageTk.PhotoImage(Image.open("1.png"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

# creating custom frame
frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Amateurs hack systems, professionals hack people"
                            , font=('Merriweather', 10))
l2.place(x=38, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='key1', show="*")
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='key2', show="*")
entry2.place(x=50, y=165)

# Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="ACCESS", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

# You can easily integrate authentication system

app.mainloop()
