'''
Author : LuciMadMax
Versino: final

This My Personal Method to Useing Tqdm ..
if You like This method You Can use it ....
'''

import os
import tqdm

filename = "test.PNG"  # filename
filesize = os.path.getsize(filename)        # Get File Size form FIle
with open(filename,'rb') as f:              # open file I/O mod
	reading_data = f.read(1024)             # Read file into a Variable 
	print("\n")
	process = tqdm.tqdm(reading_data,       # Here Put Thre FIle Buffer Size With Reading Data
	f"Sending..", unit='B',unit_scale=True, # Here Put Thre Msg and Unit 
	unit_divisor=1024, smoothing=0.5,       # Here Put Thre unit Divisor 1024 then put bar smooting scale 0.3/0.5
	miniters=0.01, ncols=100,total=filesize # Here Put Thre miniters mens scale update point 0.01/ 0.1 and also Put  bar width 70/100++
)
	while reading_data:                     # Start While Loop and Put Reading_data Variable . 
		process.update(len(reading_data))   # Update Process bar Vaiable Values with reading data length
		reading_data = f.read(1024)         # Here Again Reading_data from file
process.close()                             # Here Close Process Bar 