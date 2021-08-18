def triangles(A):
    n = len(A)
    result = 0

    for x in range(n):
        z = x + 2

        for y in range(x+1, n):
            print(f'checkiung x=({x}, {A[x]}) y=({y}, {A[y]}) z=({z}, {A[z]})')
            if y == z: break
            while z < n and A[x] + A[y] > A[z]:
                z += 1

            result += z - y - 1

    return result



triangles([3, 5, 6, 7, 100, 1000, 2000, 3000])