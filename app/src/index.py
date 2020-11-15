from time import sleep as sleep
import tkinter as tk
from tkinter import filedialog
from document.document_functions import Documents as doc
import os.path
print("########################### \n"
      "# Welcome to the test app # \n"
      "###########################")

var = input("Press [S] for search or [U] for upload, any other key to quit: ").lower()
while var in ["s", "u"]:
    if var == "s":
        sleep(1)
        print("Okay -- so you want to search")
        sleep(1)
        search_term = input("Give me a search string: ")
        if(search_term):
            doc.search(search_term)
    if var == "u":
        sleep(1)
        print("Okay -- so you want to upload")
        sleep(1)
        root = tk.Tk()
        root.withdraw()
        from store.storage import Upload
        Upload.upload(filedialog.askopenfilename())
    var = input("Press [S] for search or [U] for upload, any other key to quit: ").lower()
