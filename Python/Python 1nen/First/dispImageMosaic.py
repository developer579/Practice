import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispImage(path):
	newImage = PIL.Image.open(path).convert("L").resize((32,32)).resize((300,300))
	imageData = PIL.ImageTk.PhotoImage(newImage)
	imageLabel.configure(image = imageData)
	imageLabel.image = imageData

def openfile():
	fpath = fd.askopenfilename()
	
	if fpath:
		dispImage(fpath)
		
root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く",command = openfile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
