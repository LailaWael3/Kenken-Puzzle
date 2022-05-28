import puzzle_generation as pg
# import kenken_gui as kg
import backtracking as bt
import time

# def perfomance_analysis(size, inference=bt.no_inference):
#     for i in range(100):
#         cliques = pg.generate(size)
#         ken = pg.Kenken(size, cliques)
#         assignment = bt.backtracking_search(ken, inference)
#         if (i == 99):
#             ken.display(assignment)

def performace_analysis_generate(size):
    cliques = []
    for i in range(100):
        cliques.append(pg.generate(size))

    return cliques

# def performance_analysis_modified(size, cliques, inference=bt.no_inference):
#     for i, clique in enumerate(cliques):
#         ken = pg.Kenken(size, clique)
#         assignment = bt.backtracking_search(ken, inference)
#         if (i == 99):
#             ken.display(assignment)

if __name__ == "__main__":
    size = 4

    # start = time.perf_counter()
    # perfomance_analysis(size)
    # end = time.perf_counter()

    # cliques = performace_analysis_generate(size)
    # # print(len(cliques))

    # start = time.perf_counter()
    # performance_analysis_modified(size, cliques)
    # end = time.perf_counter()

    # print("time taken by bt: ", end-start)

    # start = time.perf_counter()
    # performance_analysis_modified(size, cliques, bt.forward_checking)
    # end = time.perf_counter()

    # print("time taken by bt with fc: ", end-start)

    # start = time.perf_counter()
    # performance_analysis_modified(size, cliques, bt.AC3)
    # end = time.perf_counter()

    # print("time taken by bt with mac: ", end-start)

    # cliques = pg.generate(size) 

    # ken = pg.Kenken(size, cliques)

    # # print(cliques)

    # assignment = bt.backtracking_search(ken, inference=bt.forward_checking)

    # print (assignment)

    # ken.display(assignment) 



    cliques = performace_analysis_generate(size)
    total_time = 0
    total_checks = 0
    total_assigns = 0
    for clique in cliques:
        ken = pg.Kenken(size, clique)
        time, check, assign = ken.performance_analysis()  

        total_time += time
        total_checks += check
        total_assigns += assign

    avg_time = total_time / 100
    avg_checks = total_checks / 100
    avg_assigns = total_assigns / 100


    print("avg time: ", avg_time, "avg checks: ", avg_checks, "avg assigns", avg_assigns)