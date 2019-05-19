ascii_length = 8
static_input = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]


# Создание вхожного сообщения
def create_input_message(input_str):
    k = amount_of_zero(len(input_str) * ascii_length + 1)
    message = "".join([create_right_byte(ord(i.encode("ascii"))) for i in input_str]) + "1" + "".join(["0" for i in range(k)]) + create_right_add(input_str)
    message = [create_input(message[0 + i * 512: 512 + i * 512]) for i in range(int(len(message) / 512))]
    return message


# Создание входного блока
def create_input(input_str):
    result = []
    for i in range(int(len(input_str) / 32)): result.append(input_str[0 + i * 32 : 32 + i * 32])
    result = [int(i, 2) for i in result]
    return result


# Вычисление количества нулей
def amount_of_zero(input_int):
    k = 0
    while True:
        if (input_int + k) % 512 == 448: return k
        else: k += 1


# Организация правильного байта
def create_right_byte(input_int):
    return "".join(["0" for i in range(8 - len(bin(input_int)[2:]))]) + bin(input_int)[2:]


# Организация правильной добавки к входу
def create_right_add(input_str):
    return "".join(["0" for i in range(64 - len(bin(len(input_str) * ascii_length)[2:]))]) + bin(len(input_str) * ascii_length)[2:]