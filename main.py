import tkinter as tk
import threading

import recorder


def main():
    root = tk.Tk()
    root.title("Sound Recorder")

    canvas = tk.Canvas(root, width=200, height=100)
    canvas.grid()

    button = tk.Button(root, command=lambda: threading.Thread(target=recorder.record_audio).start(), text="Record")
    button.grid()

    button = tk.Button(root, command=lambda: threading.Thread(target=recorder.stop_recording()).start(), text="Stop")
    button.grid()

    root.mainloop()


if __name__ == '__main__':
    main()
