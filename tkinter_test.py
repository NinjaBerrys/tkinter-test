# Imports modules
from tkinter import *
import time
import random

# Create a window
root = Tk()
root.title("THE App")

# Create a frame
top_frame = Frame(root)
top_frame.grid(row=0, column=0)

image_frame = Frame(root)
image_frame.grid(row=1, column=0)

eighty_six_frame = Frame(root)
eighty_six_frame.grid(row=1, column=1)

bottom_frame = Frame(root)
bottom_frame.grid(row=2, column=0)

# Create a PhotoImage()
kaworu_image = PhotoImage(file='img/kaworu.png')
ernst_image = PhotoImage(file='img/ernst.png')
satou_image = PhotoImage(file='img/satou.png')
tom_image = PhotoImage(file='img/tom.png')

# Create a label with the 'title' of the app
label_with_title = Label(top_frame, text="Welcome to the Best tkinter demonstration program!!!", justify="center")
label_with_title.grid()

# Create a label and add it to the window using grid()
label_with_colors_and_flow = Label(top_frame,
                                   text="Jibun wo sekai sae mo\nkaete shimaesou na\nShunkan ha itsumo sugu soba "
                                        "ni", bg='sea green', fg='chartreuse', wraplength=200, justify="center")
label_with_colors_and_flow.grid()

# Create and set the message text variable
lelouch_quote = StringVar()
lelouch_quote.set("The only ones who should kill, are those who are prepared to be killed.")

# Create the message label and add it to the window using pack()
lelouch_label = Label(top_frame, textvariable=lelouch_quote, wraplength=250)
lelouch_label.grid()

# Create a new Label using the PhotoImage and pack it into the GUI
anime_label = Label(image_frame, image=kaworu_image)
anime_label.grid()

# Create a StringVar() to store text
evangelion_waifu = StringVar()

# Create a text entry field
waifu_entry = Entry(bottom_frame, textvariable=evangelion_waifu, width=30, bg='yellow', fg='red', justify='center')
waifu_entry.grid()

# Create a second label with longer text and add it to the window using pack()
label2 = Label(bottom_frame, textvariable=evangelion_waifu, wraplength=150)
label2.grid()

# Create a button
button = Button(bottom_frame, text="button that does nothing", bg="red", fg="purple", state="normal")
button.grid()


# Defines the function "hands_up_to_the_sky_lyrics"
def hands_up_to_the_sky_lyrics():
    hands_up_text.set("""Listen up Troublemaker
    How'd you know 'bout my fever""")


# Create a button that calls on "hands up to the sky" function
hands_up_text = StringVar()
hands_up_label = Label(eighty_six_frame, textvariable=hands_up_text)
hands_up_button = Button(eighty_six_frame, text="hands up to the sky", command=hands_up_to_the_sky_lyrics)
hands_up_button.grid(row=0)
hands_up_label.grid(row=1)

# Create a StringVar() for the chosen option
chosen_option = StringVar()

# Create a list of items for the Option Menu
gender = ["man1", "man2", "man3"]

# Create the option menu and place in row 3, column 0
option_menu = OptionMenu(bottom_frame, chosen_option, gender[0], *gender)
option_menu.grid(row=3, column=0, padx=10, pady=5)

# Placeholder for checkbutton


# Placeholder for radiobutton

# Defines the function "image_change"
# image_change = True
# image_list = ["kaworu_image", "ernst_image", "satou_image", "tom_image"]
# while image_change:
#     anime_label.configure("image=random.choice(image_list)")
#     time.sleep(5)

# Run the main window loop
root.mainloop()
