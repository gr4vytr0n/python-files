import pickletools

def protocol_version(file_object):
  maxproto = -1
  for opcode, arg, pos in pickletools.genops(file_object):
    maxproto = max(maxproto, opcode.proto)
  return maxproto

with open('entry2.pickle', 'rb') as entry2:
  v = protocol_version(entry2)

print(v)
