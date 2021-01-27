from PIL import ImageDraw, Image
import hashlib
import numpy as np

def text_to_bits(text, encoding = 'utf-8'):
    bits = bin(int.from_bytes(text.encode(encoding), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def bits_to_int(bin):
    return int(bin, base = 2)

def int_to_bits(num):
    return bin(num)[2::]

def generate_bin_combination(_bin, avatar_size, block_size):
    combination = _bin

    while len(combination) < (avatar_size // block_size * (avatar_size // block_size)):
        new_num = int_to_bits(bits_to_int(combination) ** 2)
        combination += new_num
    return combination[:(avatar_size // block_size * (avatar_size // block_size))//2]

def generate(string:str, blocks:int, block_size:int, paddings:int, f:str):
    print("appen")
    background_color = '#f1f1f1'
    main_color = (tuple(channel // 2 + 128 for channel in hashlib.md5(string.encode('utf-8')).digest()[:3]))
    avatar_size = block_size * blocks
    block_size = avatar_size // blocks # размер квадрата
    img_size = (avatar_size, avatar_size)

    img = Image.new('RGB', img_size, background_color)
    draw = ImageDraw.Draw(img)

    bits = generate_bin_combination(text_to_bits(string), avatar_size, block_size)
    need_color = np.array([bit == '1' for bit in str(bits)]).reshape(avatar_size // block_size // 2,avatar_size // block_size)
    need_color = np.concatenate((need_color, need_color[::-1]))

    for x in range(avatar_size):
        for y in range(avatar_size):
            try:
                need_to_paint = need_color[x // block_size, y // block_size]
            except:
                pass

            if need_to_paint and x > block_size * paddings and y > block_size * paddings and y < avatar_size - block_size * paddings and x < avatar_size - block_size * paddings:
                draw.point((x, y), main_color)
    if f is not None:
        img.save(f)