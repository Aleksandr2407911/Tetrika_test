from task3.solution_3 import check_in, trim_edges, intersection_time


def test_check_in():
    assert check_in([22, 57], [(10, 11), (18, 26), (56, 60)]) == [(22, 26), (56, 57)]
    assert check_in([22, 57], [(33, 35), (38, 40)]) == [(33, 35), (38, 40)]


def test_trim_edges():
    assert trim_edges((11, 15, 18, 19, 22, 28), (15, 22)) == [
        (15, 15),
        (18, 19),
        (22, 22),
    ]
    assert trim_edges((11, 15, 18, 19, 22, 28), (15, 30)) == [
        (15, 15),
        (18, 19),
        (22, 28),
    ]


def test_intersection_time():
    assert intersection_time([(10, 20), (30, 40)], [(5, 15), (30, 35)]) == 10
    assert intersection_time([(10, 20), (30, 40)], [(10, 20), (30, 35)]) == 15
