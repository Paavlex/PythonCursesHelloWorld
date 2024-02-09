import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_RED)
    stdscr.clear()
    stdscr.addstr(10, 20, "Hello World!", curses.A_UNDERLINE)
    stdscr.addstr(20, 40, "Hello World!", curses.color_pair(1))
    stdscr.addstr(30, 60, "Hello World!", curses.A_BLINK)
    stdscr.addstr(40, 80, "Hello World!", curses.A_DIM)


    stdscr.refresh()
    stdscr.getch()
    
wrapper(main)
