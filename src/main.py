from tkinter import Tk
from ui.main_window import MainWindow
import logging

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Application started")
    
    root = Tk()
    
    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate window dimensions for 1/5 of the screen width
    window_width = screen_width // 5
    window_height = screen_height
    
    # Set window geometry to occupy the rightmost 1/5 of the screen
    root.geometry(f"{window_width}x{window_height}+{screen_width - window_width}+0")
    
    # Update the window to ensure the geometry is set correctly
    root.update_idletasks()
    
    root.title("桌面助手")
    
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()