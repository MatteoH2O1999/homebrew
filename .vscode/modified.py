import time
import pathlib
import sys
import json

timestamp = int(time.time())
path = pathlib.Path(sys.argv[1])

text = path.read_text()
json_data = json.loads(text)
json_data['_meta']['dateLastModified'] = timestamp
path.write_text(json.dumps(json_data, indent='\t'))