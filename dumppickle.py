import pickle
import time

entry = {'title': 'files 101', 'article_link': 'http://www.example.com/files', 'comments_link': None, 'internal_id': b'\xde\xd5\xb4\xf8', 'tags': ('files', 'pickle', 'serialize'), 'published': True, 'published_date': time.strptime('Fri Mar 16 04:20:00 1999')}

with open('entry2.pickle', 'wb') as f:
  pickle.dump(entry, f)

