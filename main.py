import os
from datetime import datetime, timedelta
import random

from tkinter import *
import customtkinter as ctk
from PIL import Image
from playsound import playsound

class PomodoroApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme("dark-blue")

        self.current_theme = "dark"

        self.title("Pomodoro")
        self.geometry("1000x800")

        self.current_theme = "dark"
        self.current_focus_time = "25"
        self.current_break_time = "5"
        self.pomodoro_session_counter = 0 
        self.pomodoro_session = 0
        self.pomodoro_cycle = 4 # Default
        self.pomodoro_interval_time = "30" # Default
        self.current_label = "Work"

        self.previous_settings()

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.tomato_icon_path = os.path.join(BASE_DIR, "icons/tomato_icon.png")
        self.homepage_icon_path = os.path.join(BASE_DIR, "icons/homepage_icon.png")
        self.analysis_icon_path = os.path.join(BASE_DIR, "icons/analysis_icon.png")
        self.settings_icon_path = os.path.join(BASE_DIR, "icons/settings_icon.png")
        self.theme_icon_path = os.path.join(BASE_DIR, "icons/theme_icon.png")
        
        self.widgets()
        self.homepage_page()

    def previous_settings(self):
        with open("data/settings.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(": ")
                
                if key == "Focus Time":
                    self.current_focus_time = value
                elif key == "Break Time":
                    self.current_break_time = value
                elif key == "Pomodoro Cycle":
                    self.pomodoro_cycle = value
                elif key == "Time Between Pomodoros":
                    self.pomodoro_interval_time = value

    def widgets(self):
        self.homepage_header_label = ctk.CTkLabel(
            self,
            text="Pomodoro",
            font=("Helvetica", 40)
        )
        self.homepage_header_label.grid(row=0, column=1, padx=10, pady=20)

        self.label_combobox_label = ctk.CTkLabel(
            self,
            text="Label",
            font=("Helvetica", 14)
        )
        self.label_combobox_label.place(x=120, y=70)

        self.label_combobox = ctk.CTkComboBox(
            self,
            values=["Work", "Study", "Read"],
            width=100
        )
        self.label_combobox.set("Work")
        self.label_combobox.place(x=100, y=100)

        self.quote_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 25),
            wraplength=200,
        )
        self.quote_label.place(x=100, y=350)

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
            text=self.current_focus_time+":00",
            font=("Helvetica", 30)
        )
        self.timer.grid(row=2, column=1, padx=10, pady=20)

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

        self.start_timer_button = ctk.CTkButton(
            self.button_frame,
            text="Start Timer",
            command=self.start_timer,
            height=60
        )
        self.start_timer_button.grid(row=0, column=0, padx=10, pady=20)

        self.restart_timer_button = ctk.CTkButton(
            self.button_frame,
            text="Restart Timer",
            command=self.restart_timer,
            height=60
        )
        self.restart_timer_button.grid(row=0, column=1, padx=10, pady=20)
        
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
            command=self.analysis_page,
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
                widget.place_forget()

        self.homepage_header_label.grid(row=0, column=1, padx=10, pady=20)
        
        # if self.homepage_header_label.cget("text") != "Focus!": 
        #     self.label_combobox_label.place(x=120, y=70)
        #     self.label_combobox.place(x=100, y=100)

        # else:
        #     self.label_combobox_label.place(x=120, y=70)

        self.label_combobox_label.place(x=120, y=70)
        self.label_combobox.place(x=100, y=100)

        # self.quote_label.configure(text=self.random_quote())
        # self.quote_label.after(10000, lambda: self.quote_label.configure(text=""))
        self.quote_label.place(x=50, y=350)

        self.tomato_label.grid(row=1, column=1, padx=10, pady=20)

        self.timer.grid(row=2, column=1, padx=10, pady=20)
        self.timer.configure(text=self.current_focus_time+":00")

        self.button_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=20)
        self.bottom_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

    def analysis_page(self):
        for widget in self.winfo_children():
            if widget != self.bottom_frame:
                widget.grid_forget()
                widget.place_forget()

        self.homepage_header_label.grid(row=0, column=1, padx=10, pady=20)

        self.todays_session_count = ctk.CTkLabel(
            self,
            text=str(self.pomodoro_session_counter)+" Pomodoros in this session!",
            font=("Helvetica", 20)
        )
        self.todays_session_count.grid(row=1, column=1, padx=10, pady=20)

        self.session_history_button = ctk.CTkButton(
            self,
            text="See History",
            command=self.session_history_page,
            fg_color="#B8860B",
            # hover_color="#B8860B",
            height=60,
        )
        self.session_history_button.grid(row=2, column=1, padx=10, pady=20)

        self.weekly_report_button = ctk.CTkButton(
            self,
            text="Weekly Report",
            command=lambda: self.previous_reports_page("Weekly"),
            fg_color="#B8860B",
            height=60
        )
        self.weekly_report_button.grid(row=3, column=1, padx=10, pady=20)

        self.monthly_report_button = ctk.CTkButton(
            self,
            text="Monthly Report",
            command=lambda: self.previous_reports_page("Monthly"),
            fg_color="#B8860B",
            height=60
        )
        self.monthly_report_button.grid(row=4, column=1, padx=10, pady=20)

        self.bottom_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

    def session_history_page(self):
        for widget in self.winfo_children():
            if widget != self.bottom_frame:
                widget.grid_forget()
                widget.place_forget()

        self.homepage_header_label.grid(row=0, column=1, padx=10, pady=20)

        self.session_history_result_label = ctk.CTkLabel(
            self,
            text="No Tasks Available...",
            font=("Helvetica", 20),
            text_color="red"
        )

        with open("data/history.txt", "r") as file:
            lines = file.readlines()

            if lines:
                self.records = []

                self.records_frame = ctk.CTkScrollableFrame(self, width=700, height=400)
                self.records_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

                for i in range(5):
                    self.records_frame.grid_columnconfigure(i, weight=1)

                record_date_header = ctk.CTkLabel(self.records_frame, text="Date")
                record_date_header.grid(row=0, column=0, padx=10, pady=5)

                record_start_header = ctk.CTkLabel(self.records_frame, text="Start Time")
                record_start_header.grid(row=0, column=1, padx=10, pady=5)

                record_end_header = ctk.CTkLabel(self.records_frame, text="End Time")
                record_end_header.grid(row=0, column=2, padx=10, pady=5)

                record_focus_header = ctk.CTkLabel(self.records_frame, text="Focus Time")
                record_focus_header.grid(row=0, column=3, padx=10, pady=5)

                record_label_header = ctk.CTkLabel(self.records_frame, text="Label")
                record_label_header.grid(row=0, column=4, padx=10, pady=5)

                for i, record in enumerate(lines, start=1):
                    parts = record.split(", ")

                    data = {}
                    for part in parts:
                        key, value = part.split(": ")
                        data[key.strip()] = value.strip()

                    date_label = ctk.CTkLabel(
                        self.records_frame,
                        text=data['Date']
                    )
                    date_label.grid(row=i, column=0, padx=10, pady=5)

                    start_time_label = ctk.CTkLabel(
                        self.records_frame,
                        text=data['Start Time']
                    )
                    start_time_label.grid(row=i, column=1, padx=10, pady=5)

                    end_time_label = ctk.CTkLabel(
                        self.records_frame,
                        text=data['End Time']
                    )
                    end_time_label.grid(row=i, column=2, padx=10, pady=5)

                    focus_time_label = ctk.CTkLabel(
                        self.records_frame,
                        text=data['Focus Time (in minutes)']
                    )
                    focus_time_label.grid(row=i, column=3, padx=10, pady=5)

                    label_label = ctk.CTkLabel(
                        self.records_frame,
                        text=data['Label']
                    )
                    label_label.grid(row=i, column=4, padx=10, pady=5)

                    self.records.append(date_label)
                    self.records.append(start_time_label)
                    self.records.append(end_time_label)
                    self.records.append(focus_time_label)
                    self.records.append(label_label)
            
            else:
                self.records = []
                self.session_history_result_label.grid(row=1, column=1, padx=10, pady=5)

        self.session_history_go_back_button = ctk.CTkButton(
            self,
            text="Go Back",
            command=self.analysis_page,
            fg_color="red",
            height=60,
        )
        self.session_history_go_back_button.grid(row=len(self.records) // 5 + 2, column=1, padx=10, pady=20)

        self.bottom_frame.grid(row=len(self.records) // 5 + 3, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

    def previous_reports_page(self, report_type):
        for widget in self.winfo_children():
            if widget != self.bottom_frame:
                widget.grid_forget()
                widget.place_forget()

        self.homepage_header_label.grid(row=0, column=1, padx=10, pady=20)

        self.session_history_go_back_button = ctk.CTkButton(
            self,
            text="Go Back",
            command=self.analysis_page,
            fg_color="red",
            # hover_color="#B8860B",
            height=60,
        )
        self.session_history_go_back_button.grid(row=1, column=1, padx=10, pady=20)

    def settings_page(self):
        for widget in self.winfo_children():
            if widget != self.bottom_frame:
                widget.grid_forget()
                widget.place_forget()

        self.homepage_header_label.grid(row=0, column=1, padx=10, pady=20)

        theme_icon = PhotoImage(file=self.theme_icon_path)
        theme_icon = theme_icon.subsample(10, 10)

        self.switch_theme_button = ctk.CTkButton(
            self,
            text="",
            image=theme_icon,
            command=self.switch_theme,
            height=60,
            width=60
        )
        self.switch_theme_button.place(x=100, y=100)

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
        
        self.pomodoro_cycle_label = ctk.CTkLabel(
            self,
            text="Pomodoro Cycle",
            font=("Helvetica", 20)
        )
        self.pomodoro_cycle_label.grid(row=5, column=1, padx=10, pady=(20, 0))

        self.pomodoro_cycle_entry = ctk.CTkEntry(
            self,
            placeholder_text="1 - 8 Sessions",
            width=200,
            height=30,
            border_width=1,
            corner_radius=10
        )
        self.pomodoro_cycle_entry.grid(row=6, column=1, padx=10, pady=(20, 0))

        self.pomodoro_interval_time_label = ctk.CTkLabel(
            self,
            text="Break Between Pomodoros",
            font=("Helvetica", 20)
        )
        self.pomodoro_interval_time_label.grid(row=7, column=1, padx=10, pady=(40, 0))

        self.pomodoro_interval_time_entry = ctk.CTkEntry(
            self,
            placeholder_text="5 - 60 Minutes",
            width=200,
            height=30,
            border_width=1,
            corner_radius=10
        )
        self.pomodoro_interval_time_entry.grid(row=8, column=1, padx=10, pady=(20, 1))

        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 20)
        )
        self.result_label.grid(row=9, column=1, padx=10, pady=22.5)

        self.apply_changes_button = ctk.CTkButton(
            self,
            text="Apply Changes",
            command=self.apply_changes,
            fg_color="green",
            hover_color="#006400",
            height=60,
        )
        self.apply_changes_button.grid(row=10, column=1, padx=10, pady=9.4)

        self.bottom_frame.grid(row=11, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

    def switch_theme(self):
        if self.current_theme == "dark":
            ctk.set_appearance_mode("light")
            self.current_theme = "light"
        else:
            ctk.set_appearance_mode("dark")
            self.current_theme = "dark"

    def apply_changes(self):
        try:
            focus_time = int(self.focus_time_entry.get())
            break_time = int(self.break_time_entry.get())
            cycle = int(self.pomodoro_cycle_entry.get())
            time_betw_pomodoros = int(self.pomodoro_interval_time_entry.get())

            self.pomodoro_session = cycle

            if focus_time >= 1 and focus_time <= 120 and break_time >= 1 and break_time <= 30 and cycle >= 1 and cycle <=8 and time_betw_pomodoros >= 1 and time_betw_pomodoros <= 60: # Change later
                self.current_focus_time = str(focus_time)
                self.current_break_time = str(break_time)
                self.pomodoro_interval_time = str(time_betw_pomodoros)

                with open("data/settings.txt", "w") as file:
                    file.write(f"Focus Time: {self.current_focus_time}\nBreak Time: {self.current_break_time}\nPomodoro Cycle: {cycle}\nTime Between Pomodoros: {self.pomodoro_interval_time}")

                self.result_label.configure(text="Changes Saved!", text_color="green")

            else:
                self.result_label.configure(text="Please Enter Valid Numbers!", text_color="red")
        
        except:
            self.result_label.configure(text="Please Enter Valid Numbers!", text_color="red")

        self.result_label.after(3000, self.result_label_clear_message)

        self.homepage_header_label.focus()

        self.focus_time_entry.delete(0, END)
        self.break_time_entry.delete(0, END)
        self.pomodoro_cycle_entry.delete(0, END)
        self.pomodoro_interval_time_entry.delete(0, END)
        
        self.timer.configure(text=self.current_focus_time+":00")

    def start_timer(self):
        if self.start_timer_button.cget("text") == "Stop Timer":
            self.label_combobox_label.configure(text="Label")
            self.label_combobox.place(x=100, y=100)

            self.after_cancel(self.timer_id)
            self.start_timer_button.configure(text="Continue Timer")
            self.paused_time = self.current_focus_time_seconds
        
        elif self.start_timer_button.cget("text") == "Continue Timer":
            self.current_label = self.label_combobox.get()
            self.label_combobox_label.configure(text=self.current_label)
            self.label_combobox.place_forget()

            self.start_countdown(self.paused_time, "Focus")
            self.start_timer_button.configure(text="Stop Timer")
        
        else:
            self.quote_label.configure(text=self.random_quote())
            self.quote_label.after(10000, lambda: self.quote_label.configure(text=""))

            self.current_label = self.label_combobox.get()
            self.label_combobox_label.configure(text=self.current_label)
            self.label_combobox.place_forget()

            self.homepage_header_label.configure(text="Focus!")
            self.current_focus_time_seconds = int(self.current_focus_time) * 60
            self.start_countdown(self.current_focus_time_seconds, "Focus")
            self.start_timer_button.configure(text="Stop Timer")

    def start_countdown(self, countdown_time, mode):
        def countdown():
            nonlocal countdown_time
            minutes, seconds = divmod(countdown_time, 60)

            temp_break_time = self.current_break_time

            time_format = f"{minutes:02}:{seconds:02}"
            self.timer.configure(text=time_format)

            if countdown_time > 0:
                countdown_time -= 1
                self.current_focus_time_seconds = countdown_time
                self.timer_id = self.after(1000, countdown)
            else:
                playsound("sounds/alarm.wav")
                if mode == "Focus":
                    self.pomodoro_session_counter += 1

                    now = datetime.now()

                    with open("data/history.txt", "a+") as file:
                        date = now.strftime("%d-%m-%Y")

                        day = now.strftime("%A")
                        
                        start_time = now.strftime("%H:%M:%S")
                        end_time = (now + timedelta(minutes=int(self.current_focus_time))).strftime("%H:%M:%S")
                        
                        file.write(f"Date: {date}, Day: {day}, Start Time: {start_time}, End Time: {end_time}, Focus Time (in minutes): {self.current_focus_time}, Break Time (in minutes): {self.current_break_time}, Label: {self.current_label}\n")

                    if self.pomodoro_session_counter % int(self.pomodoro_interval_time) == 0:
                        self.homepage_header_label.configure(text="Pomodoro Completed!")
                        self.current_break_time = self.pomodoro_interval_time
                        self.pomodoro_cycle += 1

                    else:
                        self.current_break_time = temp_break_time
                        self.homepage_header_label.configure(text="Take a Break!")

                    self.timer.configure(text="Break Time!")
                    self.timer_id = self.after(1000, lambda: self.start_countdown(int(self.current_break_time) * 60, "Break"))
                    
                elif mode == "Break":
                    self.homepage_header_label.configure(text="Focus!")
                    self.timer.configure(text="Focus Time!")
                    self.timer_id = self.after(1000, lambda: self.start_countdown(int(self.current_focus_time) * 60, "Focus"))

                    self.quote_label.configure(text=self.random_quote())
                    self.quote_label.after(10000, lambda: self.quote_label.configure(text=""))
        
        countdown()

    def restart_timer(self):
        if self.start_timer_button.cget("text") == "Continue Timer":
            self.timer.configure(text=self.current_focus_time+":00")
            self.start_timer_button.configure(text="Start Timer")
            self.homepage_header_label.configure(text="Pomodoro")

            #self.label_combobox.place(x=100, y=100)
        else:
            self.restart_timer_button.configure(text="Stop the timer first!")
            self.restart_timer_button.after(1000, lambda: self.restart_timer_button.configure(text="Restart Timer"))

    def result_label_clear_message(self):
        self.result_label.configure(text="")

    def random_quote(self):
        with open("quotes/quotes.txt", "r") as file:
            lines = file.readlines()

        random_quote = random.choice(lines).strip()

        return random_quote

if __name__ ==  "__main__":
    app = PomodoroApp()
    app.mainloop()
