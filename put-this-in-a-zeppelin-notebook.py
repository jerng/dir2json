import subprocess

output = subprocess.check_output(['pip','install', 'tika'])
print(output)

import tika
from tika import parser

import datetime
import json
import uuid

gen = os.walk('/hostdata')

file_count=0
file_name_list = []
for dirpath, dirnames, filenames in gen:
    for filename in filenames:
        
        # DEV: START: limit to five files only
        if file_count == 5:
            break
        
        # DEV: testing an image's EXIF data extraction
        # dirpath = '/hostdata/zo - photos, mostly from college'
        # filename = '2005-05-11 photo baxter IMG_0002.JPG'
        
        filestat = os.stat(dirpath + '/'  + filename)
        file_name_list.append({ str(uuid.uuid4()) : {   'dir_path' : dirpath, 
                                                        'file_name': filename,
                                                        'byte_size': filestat.st_size,
                                                        'unix_ctime': str(datetime.datetime.utcfromtimestamp(filestat.st_ctime)),
                                                        'unix_mtime': str(datetime.datetime.utcfromtimestamp(filestat.st_mtime)),
                                                        'unix_atime': str(datetime.datetime.utcfromtimestamp(filestat.st_atime)),
                                                        'tika_metadata:' : parser.from_file(dirpath + '/' + filename)['metadata'],
                                                        }})
        
        # DEV: END: limit to five files only
        file_count += 1
        
json_data = json.dumps(file_name_list[0:5], indent=4)
print(json_data)
