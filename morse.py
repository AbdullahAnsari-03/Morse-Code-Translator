import tkinter as tk
from tkinter import ttk

# Morse Code Dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '|'}

class MorseCodeTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Translator")
        self.root.geometry("400x300")  # Set the initial size of the window

        self.text_var = tk.StringVar()
        self.morse_var = tk.StringVar()

        # GUI Components with updated styles
        self.label_input = ttk.Label(root, text="Input Text:", font=("Helvetica", 12), foreground="#333")
        self.label_output = ttk.Label(root, text="Morse Code:", font=("Helvetica", 12), foreground="#333")
        self.entry_input = ttk.Entry(root, textvariable=self.text_var, font=("Helvetica", 12))
        self.label_morse_output = ttk.Label(root, textvariable=self.morse_var, font=("Helvetica", 20), foreground="blue")
        self.button_translate = ttk.Button(root, text="Translate", command=self.translate_text,
                                           style="TButton.Large.TButton", cursor="hand2")

        # Define a custom style for the button
        style = ttk.Style()
        style.configure("TButton.Large.TButton", font=("Helvetica", 12), background="#FFE873", foreground="black")

        # Layout with increased padding
        self.label_input.grid(row=0, column=0, padx=20, pady=10, sticky="E")
        self.label_output.grid(row=1, column=0, padx=20, pady=10, sticky="E")
        self.entry_input.grid(row=0, column=1, padx=20, pady=10, sticky="W")
        self.label_morse_output.grid(row=1, column=1, padx=20, pady=10, sticky="W")
        self.button_translate.grid(row=2, column=1, pady=20)

    def translate_text(self):
        input_text = self.text_var.get().upper()
        morse_code = self.text_to_morse(input_text)
        self.morse_var.set(morse_code)

    def text_to_morse(self, text):
        return ' '.join(MORSE_CODE_DICT[char] for char in text if char in MORSE_CODE_DICT)


if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeTranslator(root)
    root.mainloop()
