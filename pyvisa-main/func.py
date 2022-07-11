import time


def get_arrival_index(volts, rate):  # get_cutting_wave用の関数
    volt_basis = max(volts)*rate
    for i, volt in enumerate(volts):
        if volt > volt_basis:
            break
    return i


def get_cutting_wave(time, volts, rate):
    start_i = get_arrival_index(volts, rate)
    end_i = len(volts) - get_arrival_index(volts[::-1], rate)

    out_time = time[start_i:end_i]
    out_volts = volts[start_i:end_i]
    return out_time, out_volts


def serch(plus_interval, stage, scope):
    position = []
    position.append(stage.status())
    while True:
        center = scope.get_pk2pk()

        stage.move_to_rel(0, plus_interval, 0, 0)
        right = scope.get_pk2pk()

        stage.move_to_rel(0, -2*plus_interval, 0, 0)
        left = scope.get_pk2pk()

        stage.move_to_rel(0, plus_interval, plus_interval, 0)
        up = scope.get_pk2pk()

        stage.move_to_rel(0, plus_interval, -2*plus_interval, 0)
        down = scope.get_pk2pk()

        stage.to_zero()

        if right > left and right > center:
            stage.move_one(2, plus_interval)

        if left > right and left > center:
            stage.move_one(2, -1*plus_interval)
        time.sleep(1)

        if up > down and up > center:
            stage.move_one(3, plus_interval)

        if down > up and down > center:
            stage.move_one(3, -1*plus_interval)

        latest_position = stage.status()

        if latest_position in position:
            break

        position.append(latest_position)


def serch2(plus_interval, stage, scope):
    position = []
    position.append(stage.status())
    while True:
        center = scope.get_max()

        stage.move_to_rel(0, plus_interval, 0, 0)
        right = scope.get_max()

        stage.move_to_rel(0, -2*plus_interval, 0, 0)
        left = scope.get_max()

        stage.move_to_rel(0, plus_interval, plus_interval, 0)
        up = scope.get_max()

        stage.move_to_rel(0, plus_interval, -2*plus_interval, 0)
        down = scope.get_max()

        stage.to_zero()

        if right > left and right > center:
            stage.move_one(2, plus_interval)

        if left > right and left > center:
            stage.move_one(2, -1*plus_interval)
        time.sleep(1)

        if up > down and up > center:
            stage.move_one(3, plus_interval)

        if down > up and down > center:
            stage.move_one(3, -1*plus_interval)

        latest_position = stage.status()

        if latest_position in position:
            break

        position.append(latest_position)
