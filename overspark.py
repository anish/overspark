#!/usr/bin/python2
import string,subprocess
import time,os

host_array = ["white1", "white2", "white3", "white5", "white6", "white7",  "white8", "white9", "white10", "eval3", "eval4", "iscsi-sw7", "iscsi-sw8", "iscsi-sw5", "iscsi-sw6"]
host_array.sort()
ret_list=[]
ping = 'ping %s -c 1 -W 1'
dead="\033[0;31mdead\033[m"
alive="\033[0;32malive\033[m"
for machine in host_array:
	ret_list.append(subprocess.Popen((ping % (machine)).split(),stderr=subprocess.STDOUT, stdout=subprocess.PIPE,bufsize=-1,shell=False))
time.sleep (1)
for machine in ret_list:
	print "%10s is \t%s" % (host_array[ret_list.index(machine)],dead if machine.poll() != 0 else alive)

