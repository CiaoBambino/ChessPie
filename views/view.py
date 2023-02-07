import curses

class View:
    
    def __init__(self) -> None:
        
        terminal = curses.initscr()

        curses.endwin()
