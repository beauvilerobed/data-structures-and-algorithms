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

def main():
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(n)
    print(*output_points)


if __name__ == '__main__':
    main()