import curses
from curses import wrapper


def main(stdscr):
    try:
        while True:
            curses.noecho()
            curses.cbreak()
            stdscr.keypad(True)
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
            win.border(' ',' ','=',' ','=','=',' ',' ')
            
            win.addstr(1,2,"ti-id (1)",)
            win.addstr(1,16,"ti-db (2)",)
            win.addstr(1,30,"ti-ui (3)",)
            win.addstr(1,44,"ti-sm (4)",)
            win.addstr(1,58,"ti-netflow (5)",)
            win.addstr(1,77,"postgres (6)",)
            win.addstr(1,94,"gcx-sm (7)",)
            win.addstr(1,109,"quit (q)",)
            
            win.addstr(1,13,"|",)
            win.addstr(1,27,"|",)
            win.addstr(1,41,"|",)
            win.addstr(1,55,"|",)
            win.addstr(1,74,"|",)
            win.addstr(1,91,"|",)
            win.addstr(1,106,"|",)
            


            win.refresh()
            
            stdscr.refresh()
            curses.flushinp()
            option = stdscr.getch()
            if option == ord('q'):
                curses.nocbreak()
                stdscr.keypad(False)
                curses.echo()
                curses.endwin()
                break
            else:
                
                stdscr.addstr(10,10,chr(option),)
                stdscr.refresh()
                curses.napms(2000)


    except KeyboardInterrupt:
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()


wrapper(main)
