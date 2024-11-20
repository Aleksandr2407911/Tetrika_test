pupil = [
    2789,
    4500,
    2807,
    4542,
    4512,
    4513,
    4564,
    5150,
    4581,
    4582,
    4734,
    5009,
    5095,
    5096,
    5106,
    6480,
    5158,
    5773,
    5849,
    6480,
    6500,
    6875,
    6502,
    6503,
    6524,
    6524,
    6579,
    6641,
]  # Убрал первые 5 цифр они виезде одинаковые во втором интервале

sort_pupil = sorted(pupil)
print(sort_pupil == pupil)  # Список не корректный.


def zip_file(times: list[int]) -> list[tuple[int, int]]:
    count = 0
    time_in = []
    time_out = []
    for time in times:
        if count % 2 == 0:
            time_in.append(time)
        else:
            time_out.append(time)
        count += 1
    pair_time = list(zip(time_in, time_out))
    return pair_time


for time_in, time_out in zip_file(pupil):
    if time_in < time_out:
        print(f"{time_in} : {time_out}")
