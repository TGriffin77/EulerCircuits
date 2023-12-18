from screen import Screen

if __name__ == "__main__":
    try:
        display = Screen()
        display.loop()
    finally:
        pass # do something at end.

