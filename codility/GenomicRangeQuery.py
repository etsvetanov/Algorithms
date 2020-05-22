def solution(S, P, Q):
    result = []
    DNA_len = len(S)
    mapping = {"A": 1, "C": 2, "G": 3, "T": 4}
    # next_nucl is used to store the position information
    # next_nucl[0] is about the "A" nucleotides, [1] about "C"
    #    [2] about "G", and [3] about "T"
    # next_nucl[i][j] = k means: for the corresponding nucleotides i,
    #    at position j, the next corresponding nucleotides appears
    #    at position k (including j)
    # k == -1 means: the next corresponding nucleotides does not exist
    next_nucl = [[-1] * DNA_len, [-1] * DNA_len, [-1] * DNA_len, [-1] * DNA_len]
    # Scan the whole DNA sequence, and retrieve the position information
    next_nucl[mapping[S[-1]] - 1][-1] = DNA_len - 1
    for index in range(DNA_len - 2, -1, -1):
        next_nucl[0][index] = next_nucl[0][index + 1]
        next_nucl[1][index] = next_nucl[1][index + 1]
        next_nucl[2][index] = next_nucl[2][index + 1]
        next_nucl[3][index] = next_nucl[3][index + 1]
        next_nucl[mapping[S[index]] - 1][index] = index
    for index in range(0, len(P)):
        if next_nucl[0][P[index]] != -1 and next_nucl[0][P[index]] <= Q[index]:
            result.append(1)
        elif next_nucl[1][P[index]] != -1 and next_nucl[1][P[index]] <= Q[index]:
            result.append(2)
        elif next_nucl[2][P[index]] != -1 and next_nucl[2][P[index]] <= Q[index]:
            result.append(3)
        else:
            result.append(4)
    return result

mapping = {"A": 1, "C": 2, "G": 3, "T": 4}

def solution(S, P, Q):
    result = []
    size = len(S)

    # noinspection PyDictCreation
    next_nucl = {
        'A': [-1] * size,
        'C': [-1] * size,
        'G': [-1] * size,
        'T': [-1] * size,
    }

    next_nucl[S[-1]] = size - 1

    for i in reversed(range(size - 1)):
        next_nucl['A'][i] = next_nucl['A'][i + 1]
        next_nucl['C'][i] = next_nucl['C'][i + 1]
        next_nucl['G'][i] = next_nucl['G'][i + 1]
        next_nucl['T'][i] = next_nucl['T'][i + 1]
        next_nucl[S[i]][i] = i

    for p,q in zip(P, Q):
        for nucl, factor in enumerate('ACGT'):
            if next_nucl[nucl][p] != -1 and next_nucl[nucl][q] <= q:
                result.append(factor)



solution(S='CAGCCTA', P=[2, 5, 0], Q=[4, 5, 6])

