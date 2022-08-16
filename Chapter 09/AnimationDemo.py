from tkinter import *  # Import all definitoons from tkinter

class AnimationDemo:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Animation Demo")  # Set a title

        width = 250  # Width of the canvas
        canvas = Canvas(window, bg = "white",
                    width = 250, height = 50)
        canvas.pack()

        x = 0  # Strating x positon
        canvas.create_text(x, 30,
            text = "Message moving?", tags = "text")

        dx = 3
        while True:
            canvas.move("text", dx, 0)  # Move text dx unit
            canvas.after(100)  # Sleep for 100 milliseconds
            canvas.update()  # Update canvas
            if x < width:
                x += dx  # Get the current positon for string
            else:
                x = 0  # Reset string positon to the begining
                canvas.delete("text")
                # Redraw text at the begining
                canvas.create_text(x, 30, text = "Message moving?",
                    tags = "text")

        window.mainloop()  # Create an eventloop

AnimationDemo()  # Create GUI