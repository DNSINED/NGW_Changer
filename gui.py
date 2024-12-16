from tkinter import Tk, StringVar
from tkinter import ttk
from nightbot_api import send_winner_message
from popup import inject_popup

def start_gui():
    def on_submit():
        winner_name = winner_name_var.get()
        if winner_name:
            asyncio.run(inject_popup(winner_name))
            send_winner_message(winner_name)

    root = Tk()
    root.title("Restricted Access")
    root.geometry("400x250")
    root.configure(bg="#000000")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", background="#000000", foreground="#00FF00", font=("Courier", 12))
    style.configure("TEntry", fieldbackground="#121212", foreground="#00FF00", insertcolor="#00FF00", font=("Courier", 12))
    style.configure("TButton", background="#121212", foreground="#00FF00", font=("Courier", 12, "bold"), padding=10)
    style.map("TButton", background=[("active", "#333333")])

    ttk.Label(root, text="!!! RESTRICTED ACCESS !!!", font=("Courier", 14, "bold")).pack(pady=10)

    winner_name_var = StringVar()
    entry = ttk.Entry(root, textvariable=winner_name_var, width=40)
    entry.insert(0, "Choose your winner...")
    entry.pack(pady=10, ipady=10)

    def clear_placeholder(event):
        if entry.get() == "Choose your winner...":
            entry.delete(0, "end")
    entry.bind("<FocusIn>", clear_placeholder)

    ttk.Button(root, text="Execute", command=on_submit).pack(pady=10)
    ttk.Label(root, text=r"⚠️ WARNING: Activity is being monitored ⚠️", font=("Courier", 10, "bold")).pack(side="bottom", pady=10)
    
    root.mainloop()
