import customtkinter as ctk

# import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x220")
        self.title("Stopwatch")

        self.running = False
        self.time_elapsed = 0

        self.label = ctk.CTkLabel(self, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(padx=20, pady=(20, 10))

        self.btn_start = ctk.CTkButton(self, text="Start", width=180, height=40, font=("Helvetica", 18), command=self.start)
        self.btn_start.pack(padx=20, pady=10)

        self.btn_reset = ctk.CTkButton(self, text="Reset", width=180, height=40, font=("Helvetica", 18), command=self.reset)
        self.btn_reset.pack(padx=20, pady=10)

    def update(self):
        if self.running:
            self.label.configure(text=self.format_time(self.time_elapsed))
            self.after(1000, self.update)
            self.time_elapsed += 1

    def start(self):
        if self.btn_start.cget("text") == "Start":
            self.btn_start.configure(text="Stop")
            if not self.running:
                self.running = True
                self.update()
        else:
            self.btn_start.configure(text="Start")
            self.running = False

    def reset(self):
        self.btn_start.configure(text="Start")
        self.running = False
        self.time_elapsed = 0
        self.label.configure(text="00:00:00")

    def format_time(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"


if __name__ == "__main__":
    app = App()
    app.mainloop()
