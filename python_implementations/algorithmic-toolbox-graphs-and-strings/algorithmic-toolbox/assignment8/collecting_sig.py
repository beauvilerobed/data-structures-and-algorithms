from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments = sorted(segments, key=lambda x: x.end)
    points = []
    endpoint = -1
    for segment in segments:
        if endpoint < segment.start:
            endpoint = segment.end
            points.append(endpoint)

    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)