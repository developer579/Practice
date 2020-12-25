import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import sklearn.datasets
import sklearn.svm
import numpy

def dispImage(filename):
	newImage = PIL.Image.open(filename).convert("L")
	ImageData = PIL.ImageTk.PhotoImage(newImage.resize((300,300)))
	ImageLabel.configure(image=ImageData)
	ImageLabel.image = ImageData
	newImage = newImage.resize((8,8),PIL.Image.ANTIALIAS)
	numImage = numpy.asarray(newImage,dtype=float)
	numImage = numpy.floor(16-16*(numImage/256))
	numImage = numImage.flatten()
	return numImage

def predictDisits(data):
	digits = sklearn.datasets.load_digits()
	clf = sklearn.svm.SVC(gamma = 0.001)
	clf.fit(digits.data,digits.target)
	n = clf.predict([data])
	tl2.configure(text="この画像は"+str(n)+"です！")

def openfile():
        typ = [("テキストファイル","*png")]
        di = "LavandulanoiMac/Users/lavandula/Documents/'Python 1nen'/First/NumberImage"
        fpath=fd.askopenfilename(filetypes=typ,initialdir=di)
        if fpath:
                data = dispImage(fpath)
                predictDisits(data)

root = tk.Tk()
root.title("人口知能アプリ『チノ』")
root.geometry("400x400")

tl1 = tk.Label(text="手書きの数字を認識します！")
ImageLabel = tk.Label()
btn = tk.Button(root,text="ファイルを開く",command = openfile)
tl2 = tk.Label()

tl1.pack()
ImageLabel.pack()
btn.pack()
tl2.pack()

tk.mainloop()
