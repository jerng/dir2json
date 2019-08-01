import datetime
import json
import subprocess
import sys
import uuid

output = subprocess.check_output(['pip','install', 'tika'])
print(output)

import tika
from tika import parser

gen = os.walk('/hostdata')

file_count=0
file_name_list = []
for dirpath, dirnames, filenames in gen:
    for filename in filenames:
        
        # DEV: START LIMIT: limit to five files only
            # Unbound Test (data, machine): 15191 files FINISHED in 6 min 48 sec.
            # EXAMINIE: Tika server returns a number of 415 and 422 errors.
        if file_count == 5:
            break
        
        # DEV: testing an image's EXIF data extraction
        # dirpath = '/hostdata/zo - photos, mostly from college'
        # filename = '2005-05-11 photo baxter IMG_0002.JPG'
        
        filestat = os.stat(dirpath + '/'  + filename)
        parsed = parser.from_file(dirpath + '/' + filename)
        
        file_name_list.append({ str(uuid.uuid4()) : {   'dir_path' : dirpath, 
                                                        'file_name': filename,
                                                        'byte_size': filestat.st_size,
                                                        'unix_ctime': str(datetime.datetime.utcfromtimestamp(filestat.st_ctime)),
                                                        'unix_mtime': str(datetime.datetime.utcfromtimestamp(filestat.st_mtime)),
                                                        'unix_atime': str(datetime.datetime.utcfromtimestamp(filestat.st_atime)),
                                                        'tika_metadata:' : (parsed['metadata'] if ('metadata' in parsed) else {}),
                                                        }})
        # BLOCK: print a counter.
        sys.stdout.write('\r')
        sys.stdout.write(str(file_count))
        sys.stdout.flush()
        
        # DEV: END LIMIT: limit to five files only
        file_count += 1

# BLOCK: Print dictionary as JSON.        
#json_data = json.dumps(file_name_list[0:5], indent=4)
#print(json_data)
