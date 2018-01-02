import curses, os

screen = curses.initscr() #initializes a new window for capturing key presses
curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
curses.start_color() # Lets you use colors when highlighting selected menu option
screen.keypad(1) # Capture input from keypad

# Change this to use different colors when highlighting
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background

MENU = "menu"
COMMAND = "command"
EXITMENU = "exitmenu"

def run_menu(parent='.'):
	pos=0 #pos is the zero-based index of the hightlighted menu option. Every time runmenu is called, position returns to 0, when runmenu ends the position is returned and tells the program what opt$
	x = None #control for while loop, let's you scroll through options until return key is pressed then returns pos to program
	options = [i for i in os.listdir(parent)
					if not i.startswith('.') and not i == "menu.py"]
	while True:
		curses.curs_set(0) # Make cursor invisible
		screen.border(0)
		screen.addstr(1, 2, "Project Euler %s" %
					'' if parent == '.' else parent, curses.A_STANDOUT)
		i = 0
		for i, entry in enumerate(options):
			if pos == i: textstyle = curses.color_pair(1) # highlight
			else: textstyle = curses.A_NORMAL
			screen.addstr(4 + i, 4, "%d - %s" % (i + 1, entry), textstyle)
		#screen.addstr(4 + i, 4, "%d - Exit" % i + 1, textstyle)

		x = screen.getch() # get user input
		if x == ord('j') or x == 258:
			pos += 1
		elif x == ord('k') or x == 259:
			pos -= 1
		elif x == ord('q') or x == ord('h'):
			break
		elif x == ord('\n') or x == ord('l'):
			if parent == '.':
				screen.clear()
				run_menu(options[pos])
				screen.clear()
			else:
				curses.def_prog_mode()
				os.system('reset')
				os.system('cd %s && time python3 %s; cd ..' % (parent, options[pos]))
				os.system('read -n1')
				screen.clear()
				curses.reset_prog_mode()
				curses.curs_set(0) # Make cursor invisible again
		pos %= len(options)


# Main program
exit_menu = False
while not exit_menu:
	run_menu()
	exit_menu = True
curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
