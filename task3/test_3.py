from task3.solution_3 import LessonAttendance

test_data_first = {
    "lesson": [20, 40],
    "pupil": [18, 22, 25, 30, 38, 45],
    "tutor": [18, 25, 25, 50],
}

test_data_second = {
    "lesson": [20, 40],
    "pupil": [18, 22, 19, 20, 25, 30, 38, 45],
    "tutor": [18, 25, 25, 50],
}
appearance_first = LessonAttendance(test_data_first)


def test_appearance_without_nested():
    assert appearance_first.pupil_intervals == [
        (20, 22),
        (25, 30),
        (38, 40),
    ]
    assert appearance_first.tutor_intervals == [
        (20, 25),
        (25, 40),
    ]
    assert appearance_first.merge_intervals(appearance_first.pupil_intervals) == [
        (20, 22),
        (25, 30),
        (38, 40),
    ]
    assert appearance_first.merge_intervals(appearance_first.tutor_intervals) == [
        (20, 40)
    ]
    assert appearance_first.calculate_total_time() == 9


appearance_second = LessonAttendance(test_data_second)


def test_appearance_with_nested():
    assert appearance_second.pupil_intervals == [
        (20, 22),
        (20, 20),
        (25, 30),
        (38, 40),
    ]
    assert appearance_second.tutor_intervals == [
        (20, 25),
        (25, 40),
    ]
    assert appearance_second.merge_intervals(appearance_second.pupil_intervals) == [
        (20, 22),
        (25, 30),
        (38, 40),
    ]
    assert appearance_second.merge_intervals(appearance_second.tutor_intervals) == [
        (20, 40)
    ]
    assert appearance_second.calculate_total_time() == 9
