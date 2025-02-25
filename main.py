import numpy as np


def construct_hamming_code(k: int):
    n = 2**k - 1
    m = n - k

    H = []
    for col in range(1, n + 1):
        bin_rep = list(bin(col)[2:].zfill(k))
        bin_rep = [int(b) for b in bin_rep]
        H.append(bin_rep[::-1])

    H = np.array(H).T

    parity_positions = set([2**i for i in range(k)])
    data_cols = []
    parity_cols = []
    for col in range(1, n + 1):
        if col in parity_positions:
            parity_cols.append(col)
        else:
            data_cols.append(col)
    reorder = parity_cols + data_cols
    H_reordered = []
    for col in reorder:
        bin_rep = list(bin(col)[2:].zfill(k))
        bin_rep = [int(b) for b in bin_rep]
        H_reordered.append(bin_rep[::-1])
    H = np.array(H_reordered).T

    P = H[:, k:]
    I_m = np.eye(m, dtype=int)
    G = np.concatenate((I_m, P.T), axis=1)

    return G, H


def encode_message(message_bits, G):
    m = np.array(message_bits) % 2
    codeword = m.dot(G) % 2
    return codeword


if __name__ == "__main__":
    k = 4  # Для (15,11), k=4 => n=15, m=11
    G_15_11, H_15_11 = construct_hamming_code(k)

    message_example = [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]  # 11 бітів
    codeword = encode_message(message_example, G_15_11)

    print("Message bits:", message_example)
    print("Codeword (15 bits):", codeword.tolist())
