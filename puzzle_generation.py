from functools import reduce
from random import  random, shuffle, randint, choice
from itertools import product, permutations
import backtracking
import time

def operation(operator):
    if operator == '+':
        return lambda a, b: a + b
    elif operator == '-':
        return lambda a, b: abs(a - b)
    elif operator == 'x':
        return lambda a, b: a * b
    elif operator == '÷':
        return lambda a, b: a / b
    else:
        return None

def adjacent(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2

    dx, dy = x1 - x2, y1 - y2

    return (dx == 0 and abs(dy) == 1) or (dy == 0 and abs(dx) == 1)

def generate(size):

    board = [[((i + j) % size) + 1 for i in range(size)] for j in range(size)]

    for _ in range(size):
        shuffle(board)

    for c1 in range(size):
        for c2 in range(size):
            if random() > 0.5:
                for r in range(size):
                    board[r][c1], board[r][c2] = board[r][c2], board[r][c1]

    board = {(j + 1, i + 1): board[i][j] for i in range(size) for j in range(size)}

    uncaged = sorted(board.keys(), key=lambda var: var[1])

    cliques = []
    while uncaged:

        cliques.append([])

        csize = randint(1, 4)

        cell = uncaged[0]

        uncaged.remove(cell)

        cliques[-1].append(cell)

        for _ in range(csize - 1):

            adjs = [other for other in uncaged if adjacent(cell, other)]

            cell = choice(adjs) if adjs else None

            if not cell:
                break

            uncaged.remove(cell)
            
            cliques[-1].append(cell)
            
        csize = len(cliques[-1])
        if csize == 1:
            cell = cliques[-1][0]
            cliques[-1] = ((cell, ), '.', board[cell])
            continue
        elif csize == 2:
            fst, snd = cliques[-1][0], cliques[-1][1]
            if board[fst] / board[snd] > 0 and not board[fst] % board[snd]:
                operator = choice("+x÷-")
            else:
                operator = choice("+-x")       
        else:
            operator = choice("+x")

        target = reduce(operation(operator), [board[cell] for cell in cliques[-1]])

        cliques[-1] = (tuple(cliques[-1]), operator, int(target))

    return cliques



def RowXorCol(xy1, xy2):
    return (xy1[0] == xy2[0]) != (xy1[1] == xy2[1])



def conflicting(A, a, B, b):
    for i in range(len(A)):
        for j in range(len(B)):
            
            if RowXorCol(A[i], B[j]) and a[i] == b[j]:
                return True

    return False



def satisfies(values, operation, target):
    for p in permutations(values): 
        if reduce(operation, p) == target:
            return True

    return False

def gdomains(size, cliques):
    domains = {}
    for clique in cliques:
        members, operator, target = clique

        domains[members] = list( product(  range(1, size + 1)  , repeat=len(members))) 

        qualifies = lambda values: not conflicting(members, values, members, values) and satisfies(values, operation(operator), target)

        domains[members] = list(filter(qualifies, domains[members]))

    return domains


def gneighbors(cliques):
    neighbors = {}
    for members, _, _ in cliques:
        neighbors[members] = []

    for A, _, _ in cliques:
        for B, _, _ in cliques:
            if A != B and B not in neighbors[A]:
                if conflicting(A, [-1] * len(A), B, [-1] * len(B)):
                    neighbors[A].append(B)
                    neighbors[B].append(A)

    return neighbors


class Kenken(backtracking.CSP):

    def __init__(self, size, cliques):
        
        variables = [members for members, _, _ in cliques]
        
        domains = gdomains(size, cliques)

        neighbors = gneighbors(cliques)

        backtracking.CSP.__init__(self, variables, domains, neighbors, self.constraint)

        self.checks = 0

    def constraint(self, A, a, B, b):
        self.checks += 1

        return A == B or not conflicting(A, a, B, b)



    def performance_analysis(self, inference=backtracking.no_inference):
        self.checks = 0
        self.nassigns = 0
        start = time.perf_counter()
        assignment = backtracking.backtracking_search(self, inference)
        end = time.perf_counter()
        checks = self.checks
        assign = self.nassigns
        time_taken = end - start
        return  time_taken, checks, assign
