def decrypt(message : [int])-> str:
    text = "".join([chr(num) for num in message])
    return text


if __name__ == '__main__':
    code = [84, 104, 105, 115, 32, 101, 120, 101, 114, 99, 105, 99, 101, 32, 105, 115, 32, 97, 119, 101, 115, 111, 109, 101, 32, 33]
    print(f"Votre code décrypté veut dire : {decrypt(code)}")