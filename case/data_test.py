# -*- coding:utf-8 -*-
__author__ = "longhao"
__date__ = "2021.3.23"

import ddt
import unittest


@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    @ddt.data(
        [2, 6],
        [20, 21],
        [3, 7]
    )
    @ddt.unpack
    def test_add(self, a, b):
        print("%d+%d=%d" % (a, b, a + b))


if __name__ == "__main__":
    unittest.main()
