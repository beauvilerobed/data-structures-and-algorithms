import unittest
from car_fueling import compute_min_num_of_refills


class CarFueling(unittest.TestCase):
    def test(self):
        for (d, m, stops, answer) in [             
            (950, 400, [200, 375, 550, 750], 2),
            (10, 3, [1, 2, 5, 9], -1),
            (200, 250, [100, 150], 0),
            (100, 50, [19, 30, 45, 65, 95], 2)
        ]:
            self.assertEqual(compute_min_num_of_refills(d, m, stops), answer)


if __name__ == '__main__':
    unittest.main()