def add_parity_bits(data):
    # Add 8 bit horizontal parity bits
    horizontal_parity = 0
    for i in range(8):
        for j in range(8):
            horizontal_parity ^= data[i * 8 + j]
        data[i * 8 + 8] = horizontal_parity
        horizontal_parity = 0

    # Add 8 bit vertical parity bits
    vertical_parity = 0
    for i in range(9):
        for j in range(8):
            vertical_parity ^= data[j * 8 + i]
        data[64 + i] = vertical_parity
        vertical_parity = 0

    return data


def write_to_file(data, file_name):
    with open(file_name, "w") as file:
        file.write(data)


def transmit_packet(data, file_name):
    data = add_parity_bits(data)
    write_to_file(data, file_name)


# Example usage
data = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
file_name = "parity_bits.txt"
transmit_packet(data, file_name)
