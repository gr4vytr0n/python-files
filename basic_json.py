import json
import time

basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'python and json'
basic_entry['tags'] = ('python', 'json', 'serialize')
basic_entry['published'] = True
basic_entry['comments_link'] = None
basic_entry['bytes'] = b'\xDE\xD5\xB4\xF8'
basic_entry['time'] = time.strptime('Fri Mar 16 04:20:00 1999')

def to_json(python_object):
  if isinstance(python_object, bytes):
    return {'__class__': 'bytes',
            '__value__': list(python_object)}
  raise TypeError(repr(python_object) + ' is not JSON serializable')

def from_json(json_object):
  if '__class__' in json_object:
    if json_object['__class__'] == 'bytes':
      return bytes(json_object['__value__'])
  return json_object

with open('basic.json', mode='w', encoding='utf-8') as f:
  json.dump(basic_entry, f, indent=2, default=to_json)


with open('basic.json', mode='r', encoding='utf-8') as fr:
  fj = json.load(fr, object_hook=from_json)

print(time.asctime(time.struct_time(fj['time'])))

