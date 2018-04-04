from struct import*

#store as bytes data

packed_data = pack('iiif', 6, 19, 4, 73.4)

print(packed_data)

#to get bytes back to normal

original_data = unpack('iiif',packed_data)

print(original_data)

print(unpack('iiif', b'\x06\x00\x00\x00\x13\x00\x00\x00\x04\x00\x00\x00\xcd\xcc\x92B'))
