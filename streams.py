# stream objects

import io

# string in memory as stream object
str = 'hello world'
so_str = io.StringIO(str)
print(so_str.read())

# byte array as stream object
io.BytesIO(byteArray)