```Python3

import os
import tqdm

filename = "test.PNG"
filesize = os.path.getsize(filename) 

with open(filename,'rb') as f:       
	
    reading_data = f.read(1024)      
    
	process = tqdm.tqdm(reading_data,   
	f"Sending..", unit='B',unit_scale=True,
	unit_divisor=1024, smoothing=0.5,    
	miniters=0.01, ncols=100,total=filesize
)
	while reading_data:                  
		process.update(len(reading_data))  
		reading_data = f.read(1024)      
process.close()                      

```
