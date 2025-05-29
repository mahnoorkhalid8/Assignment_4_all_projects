# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
# from PyQt6.QtGui import QPainter, QColor, QMouseEvent
# from PyQt6.QtCore import Qt, QRect
# import sys

# CANVAS_WIDTH = 400
# CANVAS_HEIGHT = 400
# CELL_SIZE = 40
# ERASER_SIZE = 20

# class EraserCanvas(QWidget):
#     def _init_(self):
#         super()._init_()
#         self.setFixedSize(CANVAS_WIDTH, CANVAS_HEIGHT)
#         self.cells = []
#         self.eraser_pos = None
        
#         # Create a grid of blue cells
#         for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
#             for col in range(0, CANVAS_WIDTH, CELL_SIZE):
#                 self.cells.append((col, row, QColor("blue")))

#     def paintEvent(self, event):
#         painter = QPainter(self)
        
#         # Draw the grid
#         for x, y, color in self.cells:
#             painter.setBrush(color)
#             painter.setPen(Qt.GlobalColor.black)
#             painter.drawRect(x, y, CELL_SIZE, CELL_SIZE)
        
#         # Draw the eraser
#         if self.eraser_pos:
#             painter.setBrush(QColor("pink"))
#             painter.drawRect(self.eraser_pos[0], self.eraser_pos[1], ERASER_SIZE, ERASER_SIZE)

#     def mouseMoveEvent(self, event: QMouseEvent):
#         self.eraser_pos = (event.position().x(), event.position().y())
        
#         # Erase cells that overlap with the eraser
#         new_cells = []
#         for x, y, color in self.cells:
#             if not (x < event.position().x() + ERASER_SIZE and x + CELL_SIZE > event.position().x() and
#                     y < event.position().y() + ERASER_SIZE and y + CELL_SIZE > event.position().y()):
#                 new_cells.append((x, y, color))
#             else:
#                 new_cells.append((x, y, QColor("white")))
        
#         self.cells = new_cells
#         self.update()

# class MainWindow(QMainWindow):
#     def _init_(self):
#         super()._init_()
#         self.setWindowTitle("Eraser Canvas - PyQt6")
#         self.setFixedSize(CANVAS_WIDTH, CANVAS_HEIGHT)
        
#         self.canvas = EraserCanvas()
#         self.setCentralWidget(self.canvas)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())




from graphics import Canvas
import time
    
CANVAS_WIDTH : int = 400
CANVAS_HEIGHT : int = 400

CELL_SIZE : int = 40
ERASER_SIZE : int = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    # Get mouse info to help us know which cells to delete
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    # Calculate where our eraser is
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find things that overlap with our eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # For everything that overlaps with our eraser (that isn't our eraser), change
    # its color to white
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')

# There is no need to edit code beyond this point

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE  # Figure out how many rows of cells we need
    num_cols = CANVAS_WIDTH // CELL_SIZE   # Figure out how many columns of cells we need
    
    # Make a grid of squares based on the number of rows and columns.
    # The rows and columns along with our cell size help determine where
    # each individual cell belongs in our grid!
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE   # The right coordinate of the cell is CELL_SIZE pixels away from the left
            bottom_y = top_y + CELL_SIZE   # The bottom coordinate of the cell is CELL_SIZE pixels away from the top
            
            # Create a single cell in the grid
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
            
            
    canvas.wait_for_click()  # Wait for the user to click before creating the eraser
    
    last_click_x, last_click_y = canvas.get_last_click()  # Get the starting location for the eraser
    
    # Create our eraser
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )
    
    # Move the eraser, and erase what it's touching
    while True:
        # Get where our mouse is and move the eraser to there
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        # Erase anything touching the eraser
        erase_objects(canvas, eraser) 
        
        time.sleep(0.05)


if __name__ == '__main__':
    main()