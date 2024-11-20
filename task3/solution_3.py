def check_in(
    bounders: list[int], for_check_intervals: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    clear_evens_odds = []

    for time_in, time_out in for_check_intervals:
        if time_out < bounders[0] or time_in > bounders[1]:
            continue
        clear_evens_odds.append((max(time_in, bounders[0]), min(time_out, bounders[1])))

    return clear_evens_odds


def trim_edges(intervals: list[int], lesson: list[int]) -> list[tuple[int, int]]:
    count = 0
    evens = []
    odds = []
    for i in intervals:
        if count % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
        count += 1
    evens_odds = list(zip(evens, odds))
    clear_evens_odds = check_in(lesson, evens_odds)
    return clear_evens_odds


def intersection_time(
    trim_presences_pupil: list[tuple[int, int]], trim_presences_tutor: list[tuple[int, int]]
) -> int:
    total = 0
    for pupil_time in trim_presences_pupil:
        for tutor_time in trim_presences_tutor:
            start = max(pupil_time[0], tutor_time[0])
            end = min(pupil_time[1], tutor_time[1])
            if start < end:
                total += end - start
    return total


def appearance(intervals: dict[str, list[int]]) -> int:
    presense_pupil = trim_edges(intervals["pupil"], intervals["lesson"])
    presense_tutor = trim_edges(intervals["tutor"], intervals["lesson"])
    return intersection_time(presense_pupil, presense_tutor)


tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
]


for test_dict in tests:
    print(appearance(test_dict["intervals"]))


if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
