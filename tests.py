#!/usr/bin/env/python

import unittest
import corex as ce
import numpy as np


class CorexTest(unittest.TestCase):

    def setUp(self):
        X = np.array([[0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 1],
                      [1, 1, 1, 0, 0],
                      [1, 1, 1, 1, 1]], dtype=int)
        self.layer1 = ce.Corex(n_hidden=2, marginal_description='discrete', smooth_marginals=False)
        self.layer1.fit(X)

    def test_clusters(self):
        clusters = np.array([0, 0, 0, 1, 1], dtype=int)
        self.assertTrue(np.all(self.layer1.clusters == clusters))

    def test_labels(self):
        labels = np.array([[1, 1],
                           [1, 0],
                           [0, 1],
                           [0, 0]], dtype=int)
        self.assertTrue(np.all(self.layer1.labels == labels))


if __name__ == '__main__':
    unittest.main()
