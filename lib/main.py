import PIL
import tkinter
from PIL import Image
from functools import partial
from tkinter import filedialog

win = tkinter.Tk()

global inPath
inPath = ""

chooseBtn = tkinter.Button(win, text="Choose input file")
def pathChoose(): # choose input picture
    inPath = filedialog.askopenfilename(filetypes=(("PNG Files", "*.png"),("All files", "*.*")))
    chooseBtn["text"] = inPath.split("/")[-1]
    chooseBtn["fg"] = "green"
    return inPath

chooseBtn["command"] = lambda: inPath
chooseBtn.pack()

pixelTxt = tkinter.Label(win, text="Picture dimensions in pixels (e.g. 16)")
pixelTxt.pack()

pixelInp = tkinter.Entry(win)
pixelInp.pack()

genBtn = tkinter.Button(win, text="Convert picture")

def generatePicture():
    print(inPath)
    validSizes = ["1", "2", "4", "8", "16", "32", "64", "128", "256"]
    if pixelInp.get() in validSizes:
        outSize = 16 
        img = Image.open(inPath)
        wpercent = (outSize / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((outSize, hsize), PIL.Image.NEAREST)
        img.save("out.png")

        genBtn["fg"] = "green"
    else:
        genBtn["fg"] = "red"
        print("Invalid size error.")

genBtn["command"] = generatePicture
genBtn.pack()


win.mainloop()