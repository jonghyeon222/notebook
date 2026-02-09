from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title("Notebook")
window.geometry("400x400")
window.resizable(False, False)

menu = Menu(window)

menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="새파일")
menu_1.add_command(label="저장")
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이")
menu.add_cascade(label="만든이", menu=menu_2)

text_area = Text(window)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

text_area.grid(sticky = N+S+E+W)

window.config(menu=menu)
window.mainloop()
