# main/main.py
# from gui.main_window import MainWindow
# import tkinter as tk

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MainWindow(root)
#     root.mainloop()

import os

# Đường dẫn tương đối của file trong dự án
file_relative_path = 'gui/main_window.py'

# Đường dẫn tuyệt đối của dự án
project_directory = os.path.dirname(os.path.abspath(__file__))

# Kết hợp đường dẫn tương đối và tuyệt đối để có đường dẫn hoàn chỉnh của file
file_absolute_path = os.path.join(project_directory, file_relative_path)

# In ra đường dẫn của file
print(f"Đường dẫn tương đối của file: {file_relative_path}")
print(f"Đường dẫn tuyệt đối của dự án: {project_directory}")
print(f"Đường dẫn hoàn chỉnh của file: {file_absolute_path}")
