# gui/main_window.py
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from transformations import transformations

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Transformer")

        self.original_image_label = tk.Label(root)
        self.transformed_image_label = tk.Label(root)

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.transform_dropdown = tk.OptionMenu(root, tk.StringVar(), *transformations.keys())
        self.transform_button = tk.Button(root, text="Transform", command=self.transform_image)
        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)

        self.load_button.grid(row=0, column=0, pady=10)
        self.transform_dropdown.grid(row=0, column=1, pady=10)
        self.transform_button.grid(row=0, column=2, pady=10)
        self.save_button.grid(row=0, column=3, pady=10)
        self.original_image_label.grid(row=1, column=0, columnspan=2, pady=10)
        self.transformed_image_label.grid(row=1, column=2, columnspan=2, pady=10)

        self.original_image = None
        self.transformed_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.display_image(self.original_image, self.original_image_label)

    def transform_image(self):
        if self.original_image is not None:
            transform_name = self.transform_dropdown.get()
            if transform_name in transformations:
                transform_function = transformations[transform_name]
                self.transformed_image = transform_function(self.original_image)
                self.display_image(self.transformed_image, self.transformed_image_label)

    def save_image(self):
        if self.transformed_image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                self.transformed_image.save(file_path)

    def display_image(self, image, label):
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
