from pynput import mouse

def on_click(x, y, button, pressed):
    print((x,y))
    if not pressed:
        return False

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
