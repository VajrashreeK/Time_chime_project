import tkinter as tk
from tkinter import ttk, messagebox
import time
import pygame

class PendulumClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pendulum Clock")

        # Initialize pygame mixer
        pygame.mixer.init()
        self.alarm_sound = pygame.mixer.Sound('alarm_sound.mp3')  # Replace with your sound file

        # Create a style for the frame with a darker shade of blue background
        style = ttk.Style()
        style.configure('DarkBlue.TFrame', background='#B0C4DE')

        # Create main frame
        main_frame = ttk.Frame(root, padding="10", style='DarkBlue.TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Time display (centered)
        self.time_label = ttk.Label(main_frame, font=('calibri', 40, 'bold'), anchor='center')
        self.time_label.grid(row=0, column=0, columnspan=3, pady=10, sticky='nsew')

        # Set Time Interval block
        set_interval_block = ttk.LabelFrame(main_frame, text="Set Time Interval", padding=(10, 5))
        set_interval_block.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        # Interval entry: Hours, Minutes, Seconds (centered)
        self.hours_label = ttk.Label(set_interval_block, text="Hours:")
        self.hours_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.hours_entry = ttk.Entry(set_interval_block, width=5)
        self.hours_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.minutes_label = ttk.Label(set_interval_block, text="Minutes:")
        self.minutes_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.minutes_entry = ttk.Entry(set_interval_block, width=5)
        self.minutes_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.seconds_label = ttk.Label(set_interval_block, text="Seconds:")
        self.seconds_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.seconds_entry = ttk.Entry(set_interval_block, width=5)
        self.seconds_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # Set Interval button (centered)
        self.set_button = ttk.Button(set_interval_block, text="Set Interval", command=self.set_interval)
        self.set_button.grid(row=3, column=0, columnspan=2, pady=5, sticky='nsew')

        # Start and Stop buttons (centered)
        self.start_button = ttk.Button(main_frame, text="Start Clock", command=self.start_clock)
        self.start_button.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

        self.stop_button = ttk.Button(main_frame, text="Stop Clock", command=self.stop_clock)
        self.stop_button.grid(row=2, column=1, padx=5, pady=5, sticky='nswe')

        # Volume control (centered)
        self.volume_label = ttk.Label(main_frame, text="Volume:")
        self.volume_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        
        self.volume_scale = ttk.Scale(main_frame, from_=0, to_=1, orient='horizontal', command=self.set_volume)
        self.volume_scale.set(1.0)  # Set initial volume to maximum
        self.volume_scale.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        # Initialize state
        self.interval_hours = 0
        self.interval_minutes = 0
        self.interval_seconds = 0
        self.last_ring_time = time.time()
        self.running = False

        # Configure root grid
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Configure main frame grid
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)

        # Ensure set_interval_block expands to fill its space
        set_interval_block.columnconfigure(0, weight=1)
        set_interval_block.columnconfigure(1, weight=1)

    def update_clock(self):
        if self.running:
            current_time = time.strftime('%H:%M:%S')
            self.time_label.config(text=current_time)
            self.check_alarm()
            self.root.after(1000, self.update_clock)

    def set_interval(self):
        try:
            hours = int(self.hours_entry.get())
            minutes = int(self.minutes_entry.get())
            seconds = int(self.seconds_entry.get())
            
            if hours < 0 or minutes < 0 or seconds < 0:
                raise ValueError
            
            self.interval_hours = hours
            self.interval_minutes = minutes
            self.interval_seconds = seconds
            
            self.last_ring_time = time.time()
            messagebox.showinfo("Info", f"Interval set to {hours} hours, {minutes} minutes, {seconds} seconds")
        
        except ValueError:
            messagebox.showerror("Error", "Please enter valid positive integers")

    def start_clock(self):
        if not self.running:
            self.running = True
            self.update_clock()

    def stop_clock(self):
        self.running = False

    def check_alarm(self):
        if self.interval_hours or self.interval_minutes or self.interval_seconds:
            current_time = time.time()
            interval_seconds = self.interval_hours * 3600 + self.interval_minutes * 60 + self.interval_seconds
            
            if current_time - self.last_ring_time >= interval_seconds:
                self.ring_alarm()
                self.last_ring_time = current_time

    def ring_alarm(self):
        self.alarm_sound.play()
        messagebox.showinfo("Alarm", "Time to ring!")

    def set_volume(self, volume):
        self.alarm_sound.set_volume(float(volume))

if __name__ == "__main__":
    root = tk.Tk()
    app = PendulumClockApp(root)
    root.mainloop()
