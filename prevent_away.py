import pyautogui
import time
import math

def move_mouse_in_circle(radius, center_x, center_y, duration=0.1):
    try:
        while True:
          
            for angle in range(0, 360, 5):  
                x = center_x + radius * math.cos(math.radians(angle))
                y = center_y + radius * math.sin(math.radians(angle))
                pyautogui.moveTo(x, y, duration=duration)
            time.sleep(1)  
    except KeyboardInterrupt:
        print("Mouse movement stopped.")

if __name__ == "__main__":
    
    current_mouse_x, current_mouse_y = pyautogui.position()
    radius = 100  # Adjust the radius of the circle
    
   
    move_mouse_in_circle(radius, current_mouse_x, current_mouse_y)
