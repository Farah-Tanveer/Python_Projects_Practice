from tkinter import *
from tkinter import ttk, filedialog, messagebox, colorchooser, font
import time

# Main Window
win = Tk()
win.title("**Text Editor**")
win.geometry("1100x750")

current_font = ("Arial", 14)
current_color = "black"
dark_mode = False

# Notebook (Tabs) with custom style
style = ttk.Style()
style.theme_use("default")
style.configure("TNotebook.Tab", padding=[20, 5], font=("Arial", 12, "bold"))
style.map("TNotebook.Tab",
          background=[("selected", "#8B8585")],
          foreground=[("selected", "#FFFFFF")])

notebook = ttk.Notebook(win)
notebook.pack(fill=BOTH, expand=1)

# Status Bar
status_bar = Label(
    win,
    text="Words: 0 | Characters: 0 | Lines: 0 | Cursor: 1:1 | 00:00:00",
    anchor=E, font=("Arial", 12), bg="#EEE", relief="groove"
)
status_bar.pack(side=BOTTOM, fill=X)

# Store info for each tab
tabs = {}

# ---------------- Functions ----------------
def create_new_tab(title="Untitled"):
    frame = Frame(notebook)
    text_area = Text(frame, wrap="word", font=current_font, fg=current_color, undo=True)
    text_area.pack(fill=BOTH, expand=1)

    scroll = Scrollbar(text_area)
    scroll.pack(side=RIGHT, fill=Y)
    text_area.config(yscrollcommand=scroll.set)
    scroll.config(command=text_area.yview)

    text_area.bind("<KeyRelease>", update_counts)
    text_area.bind("<ButtonRelease>", update_counts)  # Update cursor pos on click

    notebook.add(frame, text=title)
    notebook.select(frame)
    tabs[frame] = {"text_area": text_area, "file": None}
    update_counts()

def get_current_tab():
    tab_id = notebook.select()
    if not tab_id:
        return None
    return notebook.nametowidget(tab_id)

def get_current_text_area():
    tab = get_current_tab()
    if tab:
        return tabs[tab]["text_area"]
    return None

def update_counts(event=None):
    text_area = get_current_text_area()
    if not text_area:
        return
    text = text_area.get("1.0", "end-1c")
    words = text.split()
    chars = len(text)
    lines = text.count("\n") + 1

    # Cursor Position
    cursor_pos = text_area.index(INSERT)
    row, col = cursor_pos.split(".")

    # Current Time
    current_time = time.strftime("%H:%M:%S")

    status_bar.config(
        text=f"Words: {len(words)} | Characters: {chars} | Lines: {lines} | Cursor: {row}:{int(col)+1} | {current_time}"
    )

def new_file(event=None):
    create_new_tab("Untitled")

def open_file(event=None):
    file = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        with open(file, "r") as f:
            content = f.read()
        create_new_tab(title=file.split("/")[-1])
        tab = get_current_tab()
        text_area = tabs[tab]["text_area"]
        text_area.delete(1.0, END)
        text_area.insert(1.0, content)
        tabs[tab]["file"] = file
        update_counts()

def save_file(event=None):
    tab = get_current_tab()
    if not tab:
        return
    file = tabs[tab]["file"]
    if not file:
        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if not file:
            return
        tabs[tab]["file"] = file

    text_area = tabs[tab]["text_area"]
    with open(file, "w") as f:
        f.write(text_area.get(1.0, END))
    notebook.tab(tab, text=file.split("/")[-1])
    messagebox.showinfo("Success", "File Saved Successfully!")

def exit_editor():
    if messagebox.askyesno("Exit", "Do you really want to quit?"):
        win.destroy()

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    for tab in tabs:
        ta = tabs[tab]["text_area"]
        if dark_mode:
            ta.config(bg="#1E1E1E", fg="#DCDCDC", insertbackground="white")
            status_bar.config(bg="#2D2D2D", fg="#DCDCDC")
        else:
            ta.config(bg="white", fg=current_color, insertbackground="black")
            status_bar.config(bg="#EEE", fg="black")

def change_font_family(family):
    global current_font
    current_font = (family, current_font[1])
    ta = get_current_text_area()
    if ta:
        ta.config(font=current_font)

def change_font_size(size):
    global current_font
    current_font = (current_font[0], size)
    ta = get_current_text_area()
    if ta:
        ta.config(font=current_font)

def change_text_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color
        ta = get_current_text_area()
        if ta:
            ta.config(fg=current_color)

# ---------------- Menu Bar ----------------
menu_bar = Menu(win)

# File Menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Tab (Ctrl+T)", command=new_file)
file_menu.add_command(label="Open (Ctrl+O)", command=open_file)
file_menu.add_command(label="Save (Ctrl+S)", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut (Ctrl+X)", command=lambda: get_current_text_area().event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy (Ctrl+C)", command=lambda: get_current_text_area().event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste (Ctrl+V)", command=lambda: get_current_text_area().event_generate("<<Paste>>"))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# View Menu
view_menu = Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Toggle Dark Mode", command=toggle_dark_mode)
menu_bar.add_cascade(label="View", menu=view_menu)

# Format Menu
format_menu = Menu(menu_bar, tearoff=0)

# Font Family
font_family_menu = Menu(format_menu, tearoff=0)
for family in ["Arial", "Calibri", "Times New Roman", "Verdana", 
               "Courier New", "Comic Sans MS", "Georgia", "Lucida Console"]:
    font_family_menu.add_command(label=family, command=lambda f=family: change_font_family(f))
format_menu.add_cascade(label="Font Family", menu=font_family_menu)

# Font Size
font_size_menu = Menu(format_menu, tearoff=0)
for size in [10, 12, 14, 16, 18, 20, 22, 24, 28, 32, 36]:
    font_size_menu.add_command(label=f"{size}", command=lambda s=size: change_font_size(s))
format_menu.add_cascade(label="Font Size", menu=font_size_menu)

# Text Color
format_menu.add_command(label="Text Color", command=change_text_color)

menu_bar.add_cascade(label="Format", menu=format_menu)

win.config(menu=menu_bar)

# Shortcuts
win.bind("<Control-t>", new_file)
win.bind("<Control-o>", open_file)
win.bind("<Control-s>", save_file)
win.bind("<Control-x>", lambda e: get_current_text_area().event_generate("<<Cut>>"))
win.bind("<Control-c>", lambda e: get_current_text_area().event_generate("<<Copy>>"))
win.bind("<Control-v>", lambda e: get_current_text_area().event_generate("<<Paste>>"))

# Start with one tab
create_new_tab()
# Update status bar every second for live time
def update_time():
    update_counts()
    win.after(1000, update_time)

update_time()
win.mainloop()
