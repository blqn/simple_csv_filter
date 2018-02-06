#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `simple_csv_filter` package."""

import unittest
import os
import csv

from simple_csv_filter.simple_csv_filter import apply_filter


HERE = os.path.dirname(os.path.realpath(__file__))


class SimpleCSVFilter(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(HERE, 'data', 'test.csv')) as test_csv:
            reader = csv.reader(test_csv)
            self.header = next(reader)
            self.data = [{self.header[0]: id_, self.header[1]: email}
                         for id_, email in reader]

    def test_apply_filter_1(self):
        filter_ = {"email": ".*@free.fr$", "id": "^42$"}
        matched = [r for r in self.data if apply_filter(filter_, 'or', r)]
        self.assertListEqual(
            [{'email': 'jblessed15@vistaprint.com', 'id': '42'},
             {'email': 'amadsen2i@free.fr', 'id': '91'}],
            matched
        )

    def test_apply_filter_2(self):
        filter_ = {"email": ".*@free.fr$", "id": "^42$"}
        matched = [r for r in self.data if apply_filter(filter_, 'and', r)]
        self.assertEqual(len(matched), 0)

    def test_apply_filter_3(self):
        filter_ = {"email": ".*@free.fr$", "id": "^42$"}
        matched = [r for r in self.data if apply_filter(filter_, 'none', r)]
        self.assertEqual(len(matched), len(self.data) - 2)
