import base64

message = input("Enter your messgae to encode or decode: ")

encode = message.encode('ascii')
base64_bytes = base64.b64encode(encode)
print(base64_bytes)

message_byte = base64.b64decode(base64_bytes)
message = message_byte.decode('ascii')
print(message)

