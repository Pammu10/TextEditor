from tkinter import *
from tkinter.ttk import *

from tkinter.filedialog import askopenfilename, asksaveasfilename
i = 1


def save_file(window, notepad):
    filepath = asksaveasfilename( defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not filepath:
        return
    with open(filepath, 'w', encoding='utf-8') as output_file:
        text_content = notepad.get('1.0', END)

        output_file.writelines(text_content)

    window.title(f"Pammu editor -{filepath}")


def open_file(window, notepad):
    filepath = askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not filepath:
        return
    
    with open(filepath, 'r', encoding='utf-8') as input_file:
        input_text = input_file.read()
        notepad.insert(END, input_text)

    window.title(f"Pammu editor -{filepath}")

light = True

def change_theme(notepad):
    global light
    if light:
        notepad.config(bg='black')
        notepad.config(fg='white')
        light = False
    else:
        notepad.config(bg='white')
        notepad.config(fg='black')
        light = True





def main():
    
    window = Tk()
    window.title("Pammu Editor")
    window.geometry("1280x600")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=400)
    
    notepad = Text(window)
    notepad.grid(row=0, column=1, sticky='nsew')

    frame_btns = Frame(window, relief=RAISED, border=2)

    btn_save = Button(frame_btns, text="Save File", command=lambda: save_file(window, notepad))
    btn_open = Button(frame_btns, text="Open File", command=lambda: open_file(window, notepad))
    
    btn_theme = Button(frame_btns, text="Change theme", command=lambda: change_theme(notepad))
    btn_bold = Button(frame_btns, text="Bold")
    btn_italic = Button(frame_btns, text="Italics")

    btn_open.grid(row=0, column= 0, padx=5, pady=5, sticky='ew')
    btn_save.grid(row=1, column=0, padx=5, sticky='ew')
    btn_theme.grid(row=2, column=0, padx=5,  pady=5, sticky='ew')
    btn_bold.grid(row=3, column=0, padx=5, sticky='ew')
    btn_italic.grid(row=4, column=0, padx=5,  pady=5, sticky='ew')

    frame_btns.grid(row=0, column=0, sticky='ns')
    window.mainloop()

main()



