import tkinter as tk
from controller import enter_car, exit_car, list_cars
from utils import format_car_list
import data_access

# ساخت جدول جدید در دیتابیس
data_access.init_db()

def update_car_list():
    cars = list_cars()
    label_count.config(text=f"تعداد ماشین‌ها: {len(cars)}")
    label_list.config(text=format_car_list(cars))

def on_enter_car():
    success, msg = enter_car(entry_name.get(), entry_model.get(), entry_color.get(), entry_plate.get())
    label_status.config(text=msg)
    if success:
        entry_name.delete(0, tk.END)
        entry_model.delete(0, tk.END)
        entry_color.delete(0, tk.END)
        entry_plate.delete(0, tk.END)
        update_car_list()

def on_exit_car():
    success, msg = exit_car(entry_plate.get())
    label_status.config(text=msg)
    entry_plate.delete(0, tk.END)
    update_car_list()

window = tk.Tk()
window.title("سیستم پارکینگ استاد")
window.geometry("650x500")

tk.Label(window, text="نام ماشین:").pack()
entry_name = tk.Entry(window, width=30)
entry_name.pack(pady=5)

tk.Label(window, text="مدل ماشین:").pack()
entry_model = tk.Entry(window, width=30)
entry_model.pack(pady=5)

tk.Label(window, text="رنگ:").pack()
entry_color = tk.Entry(window, width=30)
entry_color.pack(pady=5)

tk.Label(window, text="شماره پلاک:").pack()
entry_plate = tk.Entry(window, width=30)
entry_plate.pack(pady=5)

tk.Button(window, text="ورود ماشین", command=on_enter_car, width=20).pack(pady=5)
tk.Button(window, text="خروج ماشین (با شماره پلاک)", command=on_exit_car, width=30).pack(pady=5)

label_count = tk.Label(window, text="تعداد ماشین‌ها: 0", font=("Arial", 14))
label_count.pack(pady=10)

label_list = tk.Label(window, text="", justify="left", anchor="w")
label_list.pack(pady=10)

label_status = tk.Label(window, text="", fg="red")
label_status.pack()

update_car_list()
window.mainloop()
