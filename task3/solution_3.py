class LessonAttendance:
    def __init__(self, intervals: dict[str, list[int]]):
        self.lesson_start, self.lesson_end = intervals["lesson"]
        self.pupil_intervals = self.get_intervals(intervals["pupil"])
        self.tutor_intervals = self.get_intervals(intervals["tutor"])

    def get_intervals(self, data: list[int]) -> list[tuple[int, int]]:
        intervals = []
        for i in range(0, len(data), 2):
            start = data[i]
            end = data[i + 1]
            if end < self.lesson_start or start > self.lesson_end:
                continue
            intervals.append((max(start, self.lesson_start), min(end, self.lesson_end)))
        return intervals

    def merge_intervals(
        self, intervals: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        if not intervals:
            return []
        intervals.sort()
        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)
        return merged

    def calculate_total_time(self) -> int:
        pupil_intervals = self.merge_intervals(self.pupil_intervals)
        tutor_intervals = self.merge_intervals(self.tutor_intervals)

        total_time = 0
        for pupil_start, pupil_end in pupil_intervals:
            for tutor_start, tutor_end in tutor_intervals:
                start = max(pupil_start, tutor_start)
                end = min(pupil_end, tutor_end)
                if start < end:
                    total_time += end - start

        return total_time

    def __call__(self) -> int:
        return self.calculate_total_time()


def appearance(intervals: dict[str, list[int]]) -> int:
    attendance = LessonAttendance(intervals)
    return attendance()


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
