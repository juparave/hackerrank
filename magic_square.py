# magic square

# there's only one magic square

magic = [[8, 1, 6],
         [3, 5, 7],
         [4, 9, 2]]


def pp(square):
    """ pretty prints a square """
    s = '\n'.join([' '.join([str(cell) for cell in row]) for row in square])
    print(s)


def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1, -1, -1)]


def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def all_squares(square):
    """ returns all posible squares from square after rotating and transposing """
    all = []
    last = square
    for _ in range(2):
        all.append(last)
        for _ in range(3):
            # 3 rotations
            last = rotate_matrix(last)
            all.append(last)
        last = transpose_matrix(rotate_matrix(last))

    return all


all_magic_squares = all_squares(magic)


def square_distance(square_a, square_b):
    """ Calculate square distante """
    r = [[abs(a[i]-b[i]) for i in range(len(a))]
         for a, b in zip(square_a, square_b)]
    return sum(map(sum, r))


def form_magic(square):
    """ Looking for the minimum distance/cost to all magic squares """
    return min([s for s in [square_distance(square, all_magic_squares[i])
                            for i in range(len(all_magic_squares))]])


if __name__ == "__main__":
    sample = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

    print(form_magic(sample))
