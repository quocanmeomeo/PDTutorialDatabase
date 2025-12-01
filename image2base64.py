import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab
import io
import base64

class ImageToHtmlConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard Image to HTML Base64")
        self.root.geometry("400x250")
        
        self.generated_html = ""

        # UI Elements
        self.label_instruction = tk.Label(root, text="1. Copy an image (Ctrl+C or Snipping Tool)\n2. Click 'Convert' below", pady=10)
        self.label_instruction.pack()

        self.btn_convert = tk.Button(root, text="Convert Clipboard Image", command=self.process_clipboard, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.btn_convert.pack(pady=10)

        self.status_label = tk.Label(root, text="Waiting for image...", fg="gray")
        self.status_label.pack(pady=5)

        self.btn_copy = tk.Button(root, text="Copy HTML to Clipboard", command=self.copy_to_clipboard, state=tk.DISABLED, width=25)
        self.btn_copy.pack(pady=20)

    def process_clipboard(self):
        """Grabs image from clipboard, converts to Base64, and formats HTML."""
        try:
            # Grab image from clipboard
            img = ImageGrab.grabclipboard()

            if img is None:
                self.status_label.config(text="No image found in clipboard!", fg="red")
                return

            # Note: Sometimes clipboard contains a list of file paths instead of image data
            if isinstance(img, list):
                self.status_label.config(text="Error: Copied a file, not image data.\nOpen image and copy content.", fg="red")
                return

            # Convert image to bytes (PNG format)
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            img_bytes = buffered.getvalue()

            # Encode to Base64
            base64_str = base64.b64encode(img_bytes).decode("utf-8")

            # Create the formatted HTML tag requested
            self.generated_html = (
                f'<img src="data:image/png;base64,{base64_str}" '
                f'style="max-width: 100%; height: auto; border: 1px solid #ccc;">'
            )

            # Update UI
            self.status_label.config(text=f"Success! Image converted.\nSize: {len(base64_str)} chars", fg="blue")
            self.btn_copy.config(state=tk.NORMAL, bg="#008CBA", fg="white", font=("Arial", 10, "bold"))

        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg="red")

    def copy_to_clipboard(self):
        """Copies the generated HTML string to clipboard."""
        if self.generated_html:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.generated_html)
            self.root.update() # Required to finalize clipboard update
            messagebox.showinfo("Success", "HTML tag copied to clipboard!")
            self.status_label.config(text="Copied to clipboard!", fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToHtmlConverter(root)
    root.mainloop()