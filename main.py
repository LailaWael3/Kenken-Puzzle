import puzzle_generation as pg
import backtracking as bt


def performace_analysis_generate(size):
    cliques = []
    for i in range(100):
        cliques.append(pg.generate(size))

    return cliques

def performance_of_all_algorithms(size):
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

    print("Backtracking")
    print("avg time: ", avg_time, "avg checks: ", avg_checks, "avg assigns", avg_assigns)

    total_time = 0
    total_checks = 0
    total_assigns = 0
    for clique in cliques:
        ken = pg.Kenken(size, clique)
        time, check, assign = ken.performance_analysis(bt.forward_checking)  

        total_time += time
        total_checks += check
        total_assigns += assign

    avg_time = total_time / 100
    avg_checks = total_checks / 100
    avg_assigns = total_assigns / 100

    print("Backtracking with Forward Checking")
    print("avg time: ", avg_time, "avg checks: ", avg_checks, "avg assigns", avg_assigns)


    total_time = 0
    total_checks = 0
    total_assigns = 0
    for clique in cliques:
        ken = pg.Kenken(size, clique)
        time, check, assign = ken.performance_analysis(bt.AC3)  

        total_time += time
        total_checks += check
        total_assigns += assign

    avg_time = total_time / 100
    avg_checks = total_checks / 100
    avg_assigns = total_assigns / 100

    print("Backtracking with Arc consistency")
    print("avg time: ", avg_time, "avg checks: ", avg_checks, "avg assigns", avg_assigns)


if __name__ == "__main__":

    size = 5
    print(size)
    performance_of_all_algorithms(size)



 