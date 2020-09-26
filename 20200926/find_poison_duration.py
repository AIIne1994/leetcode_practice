def findPoisonedDuration(timeSeries, duration):
    max_damage = duration * len(timeSeries)
    total_loss_damage = 0
    for time in timeSeries:
        if time == timeSeries[0]:
            pre_time = time
            continue
        loss_damage = duration - time + pre_time
        if loss_damage > 0:
            total_loss_damage += loss_damage
        pre_time = time
    return max_damage - total_loss_damage


if __name__ == "__main__":
    pass