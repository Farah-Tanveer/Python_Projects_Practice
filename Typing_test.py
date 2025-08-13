from tkinter import *
import time
import random
import requests

# Globals
time_limit = 30
time_left = time_limit
timer_running = False
start_time = None
chosen_text = ""
typed_texts = []
original_texts = []
current_word_index = 0
words = []
flash_job = None

# Difficulty texts
texts = {
    "Easy": [
        "I love programming in Python.",
        "Coding every day improves skills.",
        "Practice makes a coder perfect.",
        "Debugging helps find and fix errors.",
        "Learning new things is always fun."
    ],
    "Medium": [
        "Python offers powerful libraries for data analysis.",
        "Building projects is the best way to master coding.",
        "Consistency and patience lead to success in programming.",
        "Errors and bugs help programmers learn new lessons.",
        "Typing speed can improve with regular practice."
    ],
    "Hard": [
        "Machine learning and artificial intelligence are transforming the world.",
        "Optimizing algorithms requires both theoretical knowledge and practice.",
        "Programming challenges test problem solving and logical reasoning skills.",
        "Collaboration in coding projects teaches teamwork and communication.",
        "Understanding computational complexity is crucial for efficient coding."
    ]
}


def show_frame(frame):
    frame.tkraise()

def fade_in_label(label, colors, delay=100, idx=0):
    """Cycle label fg colors for fade-in effect"""
    if idx < len(colors):
        label.config(fg=colors[idx])
        label.after(delay, fade_in_label, label, colors, delay, idx+1)

def start_test():
    global time_limit, time_left, timer_running, start_time, typed_texts, original_texts, current_word_index
    typed_texts.clear()
    original_texts.clear()
    current_word_index = 0

    time_limit = int(duration_var.get())
    time_left = time_limit
    timer_label.config(text=f"Time Left: {time_left} sec", fg="#00FF00")
    timeup_label.config(text="")
    load_new_text()

    entry.config(state="normal")
    entry.delete("1.0", END)
    entry.focus()

    start_time = time.time()
    timer_running = True
    update_timer()

    show_frame(test_frame)

def update_timer():
    global time_left, timer_running
    if time_left > 0 and timer_running:
        # Color fade
        if time_left > time_limit * 0.6:
            timer_label.config(fg="#00FF00")  # Green
        elif time_left > time_limit * 0.3:
            timer_label.config(fg="#FFD700")  # Yellow
        else:
            timer_label.config(fg="#FF4500")  # Red

        timer_label.config(text=f"Time Left: {time_left} sec")
        time_left -= 1
        win.after(1000, update_timer)
    else:
        end_test()

def load_new_text():
    global chosen_text, words, current_word_index
    chosen_text = random.choice(texts[diff_var.get()])
    words = chosen_text.split()
    current_word_index = 0
    show_highlighted_text()

def show_highlighted_text(correct=True):
    text_display.config(state="normal")
    text_display.delete("1.0", END)
    for i, word in enumerate(words):
        if i == current_word_index:
            if correct:
                text_display.insert(END, word + " ", "highlight_correct")
            else:
                text_display.insert(END, word + " ", "highlight_wrong")
        else:
            text_display.insert(END, word + " ")
    text_display.config(state="disabled")

def on_typing(event=None):
    if not timer_running:
        return
    typed = entry.get("1.0", END).strip().split()
    if typed:
        current_typed = typed[-1]
        target_word = words[current_word_index]
        if target_word.startswith(current_typed):
            show_highlighted_text(correct=True)
        else:
            show_highlighted_text(correct=False)

def on_space(event=None):
    global current_word_index
    typed = entry.get("1.0", END).strip().split()
    current_word_index = min(len(typed), len(words) - 1)
    show_highlighted_text()

def on_enter(event=None):
    if not timer_running:
        return "break"
    typed = entry.get("1.0", END).strip()
    typed_texts.append(typed)
    original_texts.append(chosen_text)
    entry.delete("1.0", END)
    load_new_text()
    return "break"

def flash_timeup():
    """Make TIME'S UP flash"""
    current_color = timeup_label.cget("fg")
    new_color = "#E63946" if current_color == "#FFFFFF" else "#FFFFFF"
    timeup_label.config(fg=new_color)
    global flash_job
    flash_job = win.after(400, flash_timeup)

def end_test():
    global timer_running
    timer_running = False
    entry.config(state="disabled")
    timeup_label.config(text="TIME'S UP!", font=("Arial", 28, "bold"))
    flash_timeup()
    show_results_button.config(state="normal")

def show_results():
    if flash_job:
        win.after_cancel(flash_job)
    total_chars = sum(len(t) for t in typed_texts)
    actual_time = time_limit - time_left if (time_limit - time_left) > 0 else 1
    wpm = (total_chars / 5) / (actual_time / 60)

    correct_words = 0
    total_words = 0
    for tw, ow in zip(typed_texts, original_texts):
        typed_words = tw.split()
        orig_words = ow.split()
        total_words += len(orig_words)
        for i, word in enumerate(orig_words):
            if i < len(typed_words) and typed_words[i] == word:
                correct_words += 1

    accuracy = (correct_words / total_words) * 100 if total_words > 0 else 0

    results_heading.config(text="Results")
    results_stats.config(
        text=f"WPM: {int(wpm)}\n\nAccuracy: {accuracy:.2f}%\n\nTotal Words Typed: {total_words}",
        fg="#F1C40F"
    )

    # Animate results text color pulse
    pulse_colors = ["#F1C40F", "#FFD700", "#FFA500", "#F1C40F"]
    fade_in_label(results_stats, pulse_colors, delay=300)

    show_frame(result_frame)

def restart():
    show_frame(welcome_frame)

# Main Window
win = Tk()
win.title("Typing Speed Test")
win.geometry("1000x700")
win.config(bg="#1A1714")

# Frames
welcome_frame = Frame(win, bg="#1A1714")
test_frame = Frame(win, bg="#1A1714")
result_frame = Frame(win, bg="#1A1714")
for frame in (welcome_frame, test_frame, result_frame):
    frame.place(relwidth=1, relheight=1)

# Welcome Frame
welcome_label = Label(welcome_frame, text="Typing Speed Test",
                      font=("Arial", 36, "bold"), fg="#F1C40F", bg="#2C2620")
welcome_label.pack(ipady=30, fill="x")

fade_in_label(welcome_label, ["#1A1714", "#4A3F35", "#B8860B", "#F1C40F"], delay=400)

sub_label = Label(welcome_frame, text="Select Your Test",
                  font=("Arial", 24, "bold"), bg="#1A1714", fg="#F5E6A1")
sub_label.pack(pady=40)

duration_var = StringVar(value="30")
diff_var = StringVar(value="Easy")

welcome_card = Frame(welcome_frame, bg="#2C2620", bd=3, relief="ridge")
welcome_card.pack(pady=20, ipadx=50, ipady=30)

duration_label = Label(welcome_card, text="Duration (sec):",
                       font=("Arial", 20), bg="#2C2620", fg="#F1C40F")
duration_label.grid(row=0, column=0, padx=30, pady=15, sticky="e")
duration_menu = OptionMenu(welcome_card, duration_var, "15", "30", "60", "90", "120")
duration_menu.config(font=("Arial", 16), bg="#4A3F35", fg="#F1C40F", width=8)
duration_menu.grid(row=0, column=1, padx=30, pady=15)

diff_label = Label(welcome_card, text="Difficulty:",
                   font=("Arial", 20), bg="#2C2620", fg="#F1C40F")
diff_label.grid(row=1, column=0, padx=30, pady=15, sticky="e")
diff_menu = OptionMenu(welcome_card, diff_var, "Easy", "Medium", "Hard")
diff_menu.config(font=("Arial", 16), bg="#4A3F35", fg="#F1C40F", width=8)
diff_menu.grid(row=1, column=1, padx=30, pady=15)

start_btn = Button(welcome_frame, text="Start Test", font=("Arial", 22, "bold"),
                   bg="#B8860B", fg="white", command=start_test)
start_btn.pack(pady=30)

# Test Frame
text_display = Text(test_frame, font=("Arial", 22), wrap="word", width=60, height=4,
                    bg="#2C2620", fg="#F5E6A1", bd=0, relief="flat")
text_display.pack(pady=(50, 20))
text_display.tag_configure("highlight_correct", background="#B8860B", foreground="white")
text_display.tag_configure("highlight_wrong", background="#E63946", foreground="white")
text_display.config(state="disabled")

entry = Text(test_frame, font=("Arial", 18), width=60, height=4,
             bg="#3E342C", fg="#F5E6A1", insertbackground="#F5E6A1",
             state="disabled", wrap="word")
entry.pack(pady=20)
entry.bind("<KeyRelease>", on_typing)
entry.bind("<space>", on_space)
entry.bind("<Return>", on_enter)

timer_label = Label(test_frame, text=f"Time Left: {time_limit} sec",
                    font=("Arial", 22, "bold"),
                    bg="#1A1714", fg="#E63946")
timer_label.pack(pady=(20, 10))

timeup_label = Label(test_frame, text="", bg="#1A1714")
timeup_label.pack(pady=(10, 20))

show_results_button = Button(test_frame, text="Show Results", font=("Arial", 20, "bold"),
                             bg="#B8860B", fg="white", command=show_results, state="disabled")
show_results_button.pack(pady=30)

# Result Frame
results_heading = Label(result_frame, text="", font=("Arial", 36, "bold"),
                        bg="#2C2620", fg="#F1C40F")
results_heading.pack(ipady=20, fill="x")

results_card = Frame(result_frame, bg="#3E342C", bd=3, relief="ridge")
results_card.pack(pady=(60, 20), ipadx=70, ipady=25)

results_stats = Label(results_card, text="", font=("Arial", 22, "bold"),
                      bg="#3E342C", fg="#F5E6A1", justify="center")
results_stats.pack(pady=15)

restart_button = Button(result_frame, text="Restart", font=("Arial", 20, "bold"),
                        bg="#B8860B", fg="white", command=restart)
restart_button.pack(pady=25)

# Start with Welcome Frame
show_frame(welcome_frame)

win.mainloop()
