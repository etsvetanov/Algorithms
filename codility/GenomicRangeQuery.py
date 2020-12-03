def solution(S, P, Q):
    # write your code in Python 3.6
    N = len(S)

    nucl_pref = {
        'A': [-1] * N,
        'C': [-1] * N,
        'G': [-1] * N,
        'T': [-1] * N
    }

    nucl_pref[S[0]][0] = 0

    for i, c in enumerate(S[1:], 1):
        for nucl in ['A', 'C', 'G', 'T']:
            nucl_pref[nucl][i] = i if c == nucl else nucl_pref[nucl][i - 1]

    # print('nucl_pref:', nucl_pref)

    def getMinFactor(p, q):
        for factor, nucl in enumerate('ACGT', 1):
            if p <= nucl_pref[nucl][q] <= q:
                return factor

    return [getMinFactor(p, q) for p, q in zip(P, Q)]