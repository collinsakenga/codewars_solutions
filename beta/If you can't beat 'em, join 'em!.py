def cant_beat_so_join(numbers):
    return sum(sorted(numbers, key=lambda x: -sum(x)), [])