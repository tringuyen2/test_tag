def decode_escape_sequence(byte_str):
    i = 0
    result = b""

    print("test")
    while i < len(byte_str):
        if byte_str[i:i+2] == b"\\x":
            try:
                hex_value = byte_str[i+2:i+4]
                decoded_byte = bytes.fromhex(hex_value.decode())
                result += decoded_byte
                i += 4
            except ValueError:
                result += b"\\" + byte_str[i+1:i+4]
                i += 4
        else:
            result += byte_str[i:i+1]
    return result

escaped_bytes = b'\\x3\\x4\\x5'
decoded_bytes = decode_escape_sequence(escaped_bytes)
print(decoded_bytes)
