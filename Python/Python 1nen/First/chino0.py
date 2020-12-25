import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispImage(filename):
	newImage = PIL.Image.open(filename).convert("L")
	newImage = newImage.resize((8,8),PIL.Image.ANTIALIAS)
	ImageData = PIL.ImageTk.PhotoImage(newImage.resize((300,300)))
	ImageLabel.configure(image=ImageData)
	ImageLabel.image = ImageData

def openfile():
	fpath = fd.askopenfilename()
	if fpath:
		dispImage(fpath)

root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root,text="ファイルを開く",command = openfile)
ImageLabel = tk.Label()

btn.pack()
ImageLabel.pack()

tk.mainloop()
