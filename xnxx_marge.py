# -*- coding: utf-8 -*-
import os
disk = 'E:\\xoxx\\'
def main():
	for root,dirs,files in os.walk(disk):
		ts_list = [int(i[:-3]) for i in files]
	ts_list.sort()
	for i in ts_list:
		with open(disk+'like.ts','ab') as w:
			with open(disk+str(i)+'.ts','rb') as r:
				w.write(r.read())

if __name__ == '__main__':
	main()
