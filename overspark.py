#!/usr/bin/python2
import sys,string,subprocess
import time,os
import curses

host_array = ["white1", "white2", "white3", "white5", "white6", "white7",  "white8", "white9", "white10", "eval3", "eval4", "iscsi-sw7", "iscsi-sw8", "iscsi-sw5", "iscsi-sw6"]
host_array.sort()
ret_list=[]
ping_cmd = 'ping %s -c 1 -W 1'
issue = 'ssh root@%s \'cat /etc/issue\''

def init_screen():
	curses.start_color()
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

def ping():
	for machine in host_array:
		ret_list.append(subprocess.Popen((ping_cmd % (machine)).split(),stderr=subprocess.STDOUT, stdout=subprocess.PIPE,bufsize=-1,shell=False))
	time.sleep (1)

def dump_status(myscreen):
	i=2
	for machine in ret_list:
		myscreen.addstr(i,4, "%10s \tis" % (host_array[ret_list.index(machine)]), curses.color_pair(3))
		if machine.poll() != 0:
			myscreen.addstr(i ,20, "\t\tdead", curses.color_pair(1))
		else:
		        myscreen.addstr(i, 20, "\t\talive", curses.color_pair(2))
		i += 1
	myscreen.refresh()
	myscreen.getch()

def main(argv=None):
	host_array.sort()
	myscreen = curses.initscr()
	init_screen()
	ping()
	myscreen.border(0)
	dump_status(myscreen)
	curses.endwin()

if __name__ == "__main__":
    sys.exit(main())
