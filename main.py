"""
    Phone Witnessing Tool App
    Raymond Hernandez
    November 30, 2020

"""

import tkinter as tk
import webbrowser
import re
from tkinter import Tk
# from PIL import Image
# from PIL import ImageTk


class PhoneTool:

    def __init__(self, root):
        self.root = root
        self.root.geometry("375x300")
        self.root.resizable(False, False)

        self.query = tk.StringVar()
        self.choice = tk.StringVar()
        self.choice.set("PeopleSearchNumber")
        self.site = self.choice.get()

        root.title("Phone Witnessing Tool 1.1")
        root.grid_columnconfigure((0, 1), weight=1)

        # img1 = Image.open("fastpeoplesearch.gif")
        # img1 = img1.resize((120, 30), Image.ANTIALIAS)
        # img_fastpeoplesearch = ImageTk.PhotoImage(img1)
        #
        # img2 = Image.open("forebears.gif")
        # img2 = img2.resize((120, 30), Image.ANTIALIAS)
        # img_forebears = ImageTk.PhotoImage(img2)
        #
        # icon1 = tk.Label(root, image=img_fastpeoplesearch)
        # icon1.image = img_fastpeoplesearch
        # icon1.grid(row=6, column=0, sticky='e')
        #
        # icon2 = tk.Label(root, image=img_forebears)
        # icon2.image = img_forebears
        # icon2.grid(row=6, column=1, sticky='w')

        tk.Label(root, text="Phone Witnessing Tool", font=("Calibri", 18, "bold"), pady=15).grid(row=0, columnspan=2)
        tk.Label(root, text="2020 raymondhernandez@outlook.com", font=("Helvetica", 10)).grid(row=7, columnspan=2, pady=5)
        tk.Label(root, text="Data parsed from:\nFastPeopleSearch.com\nForebears.io", wraplength=370, font=("Helvetica", 10)).grid(row=5, columnspan=3, pady=5)

        tk.LabelFrame(root, height=20).grid(row=4)

        tk.Button(root, text="Search", width=10, command=self.search_button, font=("Helvetica", 12)).grid(row=3, column=0, padx=5, pady=10, sticky='e')
        tk.Button(root, text="Clear", width=10, command=self.clear_button, font=("Helvetica", 12)).grid(row=3, column=1, padx=5, pady=10, sticky='w')

        self.search_field = tk.Entry(root, width=30, textvariable=self.query, font=("Helvetica", 12), justify="center")
        self.search_field.grid(row=1, columnspan=2, padx=5, pady=5)

        tk.Radiobutton(root, text="Check Phone", variable=self.choice, value="PeopleSearchNumber",
                       command=self.selected_site, font=("Helvetica", 12)).\
            grid(row=2, column=0, sticky='e', padx=1, pady=1)
        # tk.Radiobutton(root, text="Check Name", variable=self.choice, value="PeopleSearchName",
        #                command=self.selected_site, font=("Helvetica", 10)). \
        #     grid(row=2, column=1, sticky='e', padx=1, pady=1)
        tk.Radiobutton(root, text="Check Ethnicity", variable=self.choice, value="Forebears",
                       command=self.selected_site, font=("Helvetica", 12)).\
            grid(row=2, column=1, sticky='w', padx=1, pady=1)

    def selected_site(self):
        self.site = self.choice.get()

    def search_button(self):
        search_this = self.search_field.get()

        if self.site == "Forebears":
            search_this = "https://forebears.io/surnames/" + self.format_surname(search_this)
            webbrowser.open(search_this, new=1)
        elif self.site == "PeopleSearchNumber":
            self.format_number(search_this)
            search_this = "https://www.fastpeoplesearch.com/" + self.format_number(search_this)
            webbrowser.open(search_this, new=1)
        # elif self.site == "PeopleSearchName":
        #     search_this = "https://www.fastpeoplesearch.com/name/" + self.format_name(search_this)
        #     webbrowser.open(search_this, new=1)

    def format_surname(self, search_this):
        if len(search_this.split()) > 1:
            formatted_surname = search_this.split(" ")[1]
            formatted_surname = formatted_surname.replace(',', ' ')

            return formatted_surname

        return search_this

    # def format_name(self, search_this):
    #     formatted_name = search_this.replace(", ", "_")
    #     formatted_name = formatted_name.replace(" ", "-")
    #
    #     return formatted_name

    def format_number(self, search_this):
        formatted_phone = re.sub("[^0-9]", "", search_this)

        if formatted_phone[0] == '1':
            formatted_phone = formatted_phone[1:]

        new_formatted_phone = formatted_phone[:3] + '-' + formatted_phone[3:6] + '-' + formatted_phone[6:10]

        return new_formatted_phone

    def clear_button(self):
        self.search_field.delete(0, "end")


def main():
    root = Tk()
    app = PhoneTool(root)
    root.mainloop()


if __name__ == "__main__":
    main()
