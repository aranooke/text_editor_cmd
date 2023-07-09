'''@author:aranooke;
Text editor GUI to open,read,write,save file; 
Minimalism style;
Experiments with GUI :)
'''


import tkinter as tk
from tkinter import filedialog,messagebox,simpledialog
from tkinter import ttk,font
import filesystem as fs;
class App():
    def __init__(self) -> None:
        self.root = tk.Tk();
        self.file = fs.File("");
        self.root.title("Text editor");
        self.text = tk.Text(self.root);
        
        self.text.grid(row = 0,column = 0);
        self.text.pack();
        self.add_menu();
        self.binds();
        
        self.root.mainloop();
    
    
    def binds(self):
        self.root.bind("<Control-s>", lambda event: self.save_dialog())
        self.root.bind("<Control-o>", lambda event: self.open_dialog())
        self.root.bind("<Control-n>", lambda event: self.new_file())
        self.root.bind("<Alt-e>", lambda event: self.root.quit())

    def add_menu(self):
        # Main menu with several cascades tasks to open,save,exit file 
        mainmenu = tk.Menu(self.root);
        self.root.config(menu = mainmenu);

        filemenu = tk.Menu(mainmenu,tearoff = 0);

        filemenu.add_command(label = "New",command = self.new_file);
        filemenu.add_command(label = "Open",command = self.open_dialog);
        filemenu.add_command(label="Save as",command=self.save_dialog);
        filemenu.add_command(label="Exit",command=self.root.quit);
        filemenu.add_separator();

        mainmenu.add_cascade(label = "File",menu = filemenu);
    
        convertmenu = tk.Menu(mainmenu,tearoff=0);
    
        convertmenu.add_command(label = "From pdf to txt");

        mainmenu.add_cascade(label = "Convert",menu = convertmenu);
        
        settings_menu = tk.Menu(mainmenu,tearoff=0);
        settings_menu.add_command(label = "Font info",command=settings_menu);
        mainmenu.add_cascade(label= "Settings",menu = settings_menu);

    def settings_menu(self):
        # chane font size of text
        font_size = simpledialog.askinteger("Font Size", "Enter the font size:")
        # if font_size:
        #     # Change the font size of the text widget
        #     font_style = font.Font(size=font_size)
        #     self.text.configure(font=font_style)

    def open_dialog(self):
        #open and read txt file
        self.filename = filedialog.askopenfilename();
        if self.filename.endswith(".txt") or self.filename.endswith(".html"):
            self.file = fs.File(self.filename);
            result = self.file.read_file();
            self.text.insert("1.0",result); # Fix it 
        else:
            messagebox.showwarning("File information warning","You could open only txt file,try again, \
                                   ");
    def new_file(self):
        self.text.delete("1.0","end");
    def save_dialog(self):
        # save txt file easy
        self.filename = filedialog.asksaveasfilename();
        result = self.text.get("1.0","end");
        self.file = fs.File(self.filename);
        self.file.write_file(result);

    def notebook(self):
        # create several widgets,now isn`t working
        note_book = ttk.Notebook();
        note_book.pack(expand=True,fill="both");

        # note_book.add(self.text,"First widget");

app = App();