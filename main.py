from tkinter import *
import customtkinter as ctk
import os
from PIL import Image

class PomodoroApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme("dark-blue")

        self.title("Pomodoro")
        self.geometry("1000x800")

        self.current_theme = "dark"
        self.current_focus_time = "25"
        self.current_break_time = "5"

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.tomato_icon_path = os.path.join(BASE_DIR, "icons/tomato_icon.png")
        self.homepage_icon_path = os.path.join(BASE_DIR, "icons/homepage_icon.png")
        self.analysis_icon_path = os.path.join(BASE_DIR, "icons/analysis_icon.png")
        self.settings_icon_path = os.path.join(BASE_DIR, "icons/settings_icon.png")
        
        self.widgets()
        self.homepage_page()

    def widgets(self):
        self.homepage_header_label = ctk.CTkLabel(
            self,
            text="Pomodoro",
            font=("Helvetica", 40)
        )
        self.homepage_header_label.grid(row=0, column=1, padx=10, pady=20)

        tomato_image = ctk.CTkImage(
            light_image=Image.open(self.tomato_icon_path),
            size=(350, 350)
        )
        self.tomato_label = ctk.CTkLabel(
            self,
            text="",
            image=tomato_image
        )
        self.tomato_label.grid(row=1, column=1, padx=10, pady=20)
        
        self.timer = ctk.CTkLabel(
            self,
            text=self.current_focus_time+":00",  # Timer
            font=("Helvetica", 30)
        )
        self.timer.grid(row=2, column=1, padx=10, pady=20)

        self.start_timer_button = ctk.CTkButton(
            self,
            text="Start Timer",
            command=self.start_timer,
            height=60
        )
        self.start_timer_button.grid(row=3, column=1, padx=10, pady=20)

        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

        homepage_icon = PhotoImage(file=self.homepage_icon_path)
        homepage_icon = homepage_icon.subsample(10, 10)

        self.homepage_button = ctk.CTkButton(
            self.bottom_frame,
            image=homepage_icon,
            text="",
            command=self.homepage_page,
            fg_color="red",
            hover_color="#8B0000",
            width=60,
            height=60,
        )
        self.homepage_button.grid(row=0, column=0, padx=5, pady=10)

        analysis_icon = PhotoImage(file=self.analysis_icon_path)
        analysis_icon = analysis_icon.subsample(10, 10)

        self.analysis_button = ctk.CTkButton(
            self.bottom_frame,
            image=analysis_icon,
            text="",
            # command,
            fg_color="lightblue",
            hover_color="#4682B4",
            width=60,
            height=60
        )
        self.analysis_button.grid(row=0, column=1, padx=5, pady=10)

        settings_icon = PhotoImage(file=self.settings_icon_path)
        settings_icon = settings_icon.subsample(10, 10)

        self.settings_button = ctk.CTkButton(
            self.bottom_frame,
            image=settings_icon,
            text="",
            command=self.settings_page,
            fg_color="yellow",
            hover_color="#B8860B",
            width=60,
            height=60
        )
        self.settings_button.grid(row=0, column=2, padx=5, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_columnconfigure(2, weight=1)

    def homepage_page(self):
        for widget in self.winfo_children():
            if widget != self.bottom_frame:
                widget.grid_forget()

        self.homepage_header_label.grid(row=0, column=1, padx=10, pady=20)
        self.tomato_label.grid(row=1, column=1, padx=10, pady=20)
        
        self.timer.grid(row=2, column=1, padx=10, pady=20)
        self.timer.configure(text=self.current_focus_time+":00")

        self.start_timer_button.grid(row=3, column=1, padx=10, pady=20)
        self.bottom_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

    def settings_page(self):
        for widget in self.winfo_children():
            if widget != self.bottom_frame:
                widget.grid_forget()

        self.homepage_header_label.grid(row=0, column=1, padx=10, pady=20)

        self.focus_time_label = ctk.CTkLabel(
            self,
            text="Focus Duration",
            font=("Helvetica", 20)
        )
        self.focus_time_label.grid(row=1, column=1, padx=10, pady=(20, 0))

        self.focus_time_entry = ctk.CTkEntry(
            self,
            placeholder_text="5 - 120 Minutes",
            width=200,
            height=30,
            border_width=1,
            corner_radius=10
        )
        self.focus_time_entry.grid(row=2, column=1, padx=10, pady=20)

        self.break_time_label = ctk.CTkLabel(
            self,
            text="Break Duration",
            font=("Helvetica", 20)
        )
        self.break_time_label.grid(row=3, column=1, padx=10, pady=(20, 0))

        self.break_time_entry = ctk.CTkEntry(
            self,
            placeholder_text="5 - 30 Minutes",
            width=200,
            height=30,
            border_width=1,
            corner_radius=10
        )
        self.break_time_entry.grid(row=4, column=1, padx=10, pady=20)
        
        self.invisible_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 20)
        )
        self.invisible_label.grid(row=5, column=1, padx=10, pady=20)

        self.invisible_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 20)
        )
        self.invisible_label.grid(row=6, column=1, padx=10, pady=20)

        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 20)
        )
        self.result_label.grid(row=7, column=1, padx=10, pady=33)

        self.apply_changes_button = ctk.CTkButton(
            self,
            text="Apply Changes",
            command=self.apply_changes,
            fg_color="green",
            hover_color="#006400",
            height=60,
        )
        self.apply_changes_button.grid(row=8, column=1, padx=10, pady=20)

        self.bottom_frame.grid(row=9, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

    def apply_changes(self):
        try:
            focus_time = int(self.focus_time_entry.get())
            break_time = int(self.break_time_entry.get())

            if focus_time >= 1 and focus_time <= 120 and break_time >= 1 and break_time <= 30:
                self.current_focus_time = str(focus_time)
                self.current_break_time = str(break_time)

                self.result_label.configure(text="Changes Saved!", text_color="green")

            else:
                self.result_label.configure(text="Please Enter Valid Numbers!", text_color="red")
        
        except:
            self.result_label.configure(text="Please Enter Valid Numbers!", text_color="red")

        self.result_label.after(3000, self.result_label_clear_message)

        self.homepage_header_label.focus()

        self.focus_time_entry.delete(0, END)
        self.break_time_entry.delete(0, END)
        
        self.timer.configure(text=self.current_focus_time+":00")

    def start_timer(self):
        self.current_focus_time_seconds = int(self.current_focus_time) * 60  # Odak zamanı saniyeye çevir
        self.start_countdown(self.current_focus_time_seconds, "Focus")  # Geri sayımı başlat

    def start_countdown(self, countdown_time, mode):
        def countdown():
            nonlocal countdown_time  # countdown_time'ı dışarıdan kullanabilmek için nonlocal olarak işaretle
            minutes, seconds = divmod(countdown_time, 60)

            time_format = f"{minutes:02}:{seconds:02}"
            self.timer.configure(text=time_format)

            if countdown_time > 0:
                countdown_time -= 1
                self.after(1000, countdown)  # 1 saniye sonra geri sayımı güncelle
            else:
                if mode == "Focus":
                    # Odak zamanı bittiğinde ara zamanına geç
                    self.timer.configure(text="Break Time!")
                    self.after(1000, lambda: self.start_countdown(int(self.current_break_time) * 60, "Break"))  # Ara zamanı başlat
                elif mode == "Break":
                    # Ara zamanı bittiğinde odak zamanına geç
                    self.timer.configure(text="Focus Time!")
                    self.after(1000, lambda: self.start_countdown(int(self.current_focus_time) * 60, "Focus"))  # Odak zamanı başlat

        countdown()





    def result_label_clear_message(self):
        self.result_label.configure(text="")

if __name__ ==  "__main__":
    app = PomodoroApp()
    app.mainloop()