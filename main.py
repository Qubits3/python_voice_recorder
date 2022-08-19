import customtkinter
import threading

import recorder

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

button_text = "Record"


def main():
    root = customtkinter.CTk()
    root.geometry("200x120")
    root.title("Sound Recorder")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=10, padx=10, fill="both", expand=False)

    button = customtkinter.CTkButton(master=frame,
                                     command=switch(),
                                     text=button_text)
    button.pack(pady=10, padx=10)

    button = customtkinter.CTkButton(master=frame,
                                     command=lambda: threading.Thread(target=recorder.stop_recording).start(),
                                     text="Stop")
    button.pack(pady=10, padx=10)

    root.mainloop()


def switch():
    threading.Thread(target=recorder.record_audio).start()
    global button_text
    button_text = "Recording..."


if __name__ == '__main__':
    main()
