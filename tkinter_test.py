from tkinter import *

# Create a window
root = Tk()
root.title("THE App")

# Create a label with the 'title' of the app
label_with_title = Label(root, text="Welcome to the Best tkinter demonstration program!!!", justify="center")
label_with_title.grid(row=0)

# Create a label and add it to the window using grid()
label_with_colors_and_flow = Label(root, text="Jibun wo sekai sae mo\nkaete shimaesou na\nShunkan ha itsumo sugu soba "
                                              "ni", bg='sea green', fg='chartreuse', wraplength=200, justify="center")
label_with_colors_and_flow.grid()

# Create and set the message text variable
lelouch_quote = StringVar()
lelouch_quote.set("The only ones who should kill, are those who are prepared to be killed.")

# Create the message label and add it to the window using pack()
lelouch_label = Label(root, textvariable=lelouch_quote, wraplength=250)
lelouch_label.grid(row=0, column=0)

# Create a PhotoImage()
kaworu_image = PhotoImage(file='kaworu.png')

# Create a new Label using the PhotoImage and pack it into the GUI
kaworu_label = Label(root, image=kaworu_image)
kaworu_label.grid()

# Create a StringVar() to store text
evangelion_waifu = StringVar()

# Create a text entry field
waifu_entry = Entry(root, textvariable=evangelion_waifu, width=30, bg='yellow', fg='red', justify='center')
waifu_entry.grid()

# Create a second label with longer text and add it to the window using pack()
label2 = Label(root, textvariable=evangelion_waifu, wraplength=150)
label2.grid()

# Create a button
button = Button(root, text="born in a world of strife", bg="red", fg="purple", state="normal")
button.grid()


# Defines the function "hands_up_to_the_sky_lyrics"
def hands_up_to_the_sky_lyrics():
    hands_up_text.set("""Listen up Troublemaker
    How'd you know 'bout my fever""")


# Create a button that calls on "hands up to the sky" function
hands_up_text = StringVar()
hands_up_label = Label(root, textvariable=hands_up_text)
hands_up_button = Button(root, text="hands up to the sky", command=hands_up_to_the_sky_lyrics)
hands_up_label.grid(row=0, column=1)
hands_up_button.grid(row=1, column=1)

# Placeholder for checkbuttons


# Placeholder for radiobuttons

# Run the main window loop
root.mainloop()
