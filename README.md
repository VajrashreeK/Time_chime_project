# Time_chime_project
### Project Description: Clock with Alarm

**Project Overview:**

The Pendulum Clock with Alarm is a desktop application designed to provide a real-time clock display and customizable alarm functionality. Built using Python's `tkinter` for the graphical user interface (GUI) and `pygame` for audio playback, this project allows users to set specific time intervals for alarms, control the volume, and start or stop the clock as needed.

**Key Features:**

1. **Real-time Clock Display:**
   - Displays the current time in a large, easily readable format.
   - Automatically updates every second to show the current time.

2. **Customizable Alarm Intervals:**
   - Users can set specific time intervals (hours, minutes, and seconds) for the alarm.
   - The alarm will ring at the set intervals, providing auditory and visual notifications.

3. **Volume Control:**
   - Provides a volume slider to adjust the alarm sound volume.
   - Ensures that the alarm sound level can be customized to the user's preference.

4. **Start and Stop Functionality:**
   - Users can start or stop the clock with dedicated buttons.
   - The clock stops updating when the stop button is pressed, and resumes when the start button is pressed.

**Technical Details:**

1. **GUI Design:**
   - The application uses `tkinter` for the GUI, providing a clean and user-friendly interface.
   - Elements are organized into frames and labels for clear separation and styling.
   - The main frame uses a dark blue background for a visually appealing look.

2. **Audio Playback:**
   - The `pygame` library is used to initialize the mixer and play the alarm sound.
   - An external audio file (`alarm_sound.mp3`) is played when the alarm rings.

3. **Interval Setting:**
   - Users can input the desired hours, minutes, and seconds for the alarm interval.
   - The application validates the input to ensure only positive integers are accepted.

4. **Alarm Functionality:**
   - The application calculates the total interval time in seconds and checks if the interval has passed since the last alarm.
   - When the interval is reached, the alarm sound is played, and a visual notification is shown using a message box.

**Usage:**

1. **Setup:**
   - Ensure `pygame` and `tkinter` libraries are installed.
   - Place an alarm sound file (`alarm_sound.mp3`) in the same directory as the script.

2. **Running the Application:**
   - Execute the script to launch the application.
   - The main window will display the current time and provide options to set the alarm interval, control the volume, and start or stop the clock.

3. **Setting the Alarm:**
   - Enter the desired hours, minutes, and seconds in the respective fields.
   - Click the "Set Interval" button to set the alarm interval.
   - Start the clock by clicking the "Start Clock" button.

4. **Controlling the Volume:**
   - Use the volume slider to adjust the alarm sound volume.

5. **Stopping the Clock:**
   - Click the "Stop Clock" button to pause the clock updates.

**Benefits:**

- **Convenience:** Provides an easy-to-use interface for setting alarms and checking the current time.
- **Customization:** Allows users to set specific alarm intervals and adjust the volume to their preference.
- **Efficiency:** Automates the process of checking the time and ringing an alarm at set intervals.

The Pendulum Clock with Alarm is a versatile and user-friendly tool for anyone needing a reliable and customizable time-keeping solution. Whether for time management, productivity, or personal use, this application offers a convenient way to keep track of time and stay on schedule.
