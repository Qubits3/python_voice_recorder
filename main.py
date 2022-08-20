import customtkinter
import threading

import recorder

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


# pyinstaller --noconfirm --onedir --windowed --add-data "c:/users/metin/appdata/local/programs/python/python39/lib/site-packages/customtkinter;customtkinter/" main.py


def main():
    root = customtkinter.CTk()
    root.geometry("200x120")
    root.title("Sound Recorder")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=10, padx=10, fill="both", expand=False)

    button = customtkinter.CTkButton(master=frame,
                                     command=lambda: threading.Thread(target=recorder.record_audio).start(),
                                     text="Record")
    button.pack(pady=10, padx=10)

    button = customtkinter.CTkButton(master=frame,
                                     command=lambda: threading.Thread(target=recorder.stop_recording).start(),
                                     text="Stop")
    button.pack(pady=10, padx=10)

    root.mainloop()


if __name__ == '__main__':
    main()
