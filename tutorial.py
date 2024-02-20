import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_RED)
    BLUE_AND_RED = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_YELLOW)
    GREEN_AND_YELLOW = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    YELLOW_AND_BLACK = curses.color_pair(3)

    stdscr.clear()

    stdscr.refresh()
    #stdscr.getch()
    begin_x = 0 #curses.LINES - 5) 
    begin_y = (curses.LINES - 3) 
    height = 3
    #width = (curses.COLS-1) 
    width = (curses.COLS)
    win = curses.newwin(height, width, begin_y, begin_x)
    win.addstr(0,0,"Hello There!", curses.A_REVERSE)
    win.border(' ',' ','=',' ','=','=',' ',' ')
    
    win.addstr(1,5,"Hello",)
    win.addstr(1,20,"There",)
    win.addstr(1,30,"!",)

    win.refresh()
    
    stdscr.refresh()
    win.getch()

wrapper(main)
