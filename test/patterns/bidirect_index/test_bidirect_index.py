# The MIT License (MIT)
#
# Copyright (c) 2020 Aibolit
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os.path
from pathlib import Path
from unittest import TestCase
import unittest
from aibolit.patterns.bidirect_index.bidirect_index import BidirectIndex


@unittest.skip("Not implemented")
class BidirectIndexTestCase(TestCase):
    dir_path = Path(os.path.realpath(__file__)).parent

    def test_bidirect_index_increase_decrease(self):
        self.assertEqual(
            BidirectIndex().value(Path(self.dir_path, "BidirectIndexIncreaseDecrease.java")),
            [3],
            "Could not find bidirect index when index increased and then decreased",
        )

    def test_bidirect_index_decrease_increase(self):
        self.assertEqual(
            BidirectIndex().value(Path(self.dir_path, "BidirectIndexDecreaseIncrease.java")),
            [3],
            "Could not find bidirect index when index decreased and then increased",
        )

    def test_bidirect_index_increase_decrease_assignment(self):
        self.assertEqual(
            BidirectIndex().value(Path(self.dir_path, "BidirectIndexIncreaseDecreaseAssignment.java")),
            [3],
            "Could not find bidirect index when index increased and then decreased with assignment",
        )

    def test_bidirect_index_increase_assignment_decrease(self):
        self.assertEqual(
            BidirectIndex().value(Path(self.dir_path, "BidirectIndexIncreaseAssignmentDecrease.java")),
            [3],
            "Could not find bidirect index when index increased with assignment and then decreased",
        )

    def test_bidirect_index_increase_assignment_decrease_assignment(self):
        self.assertEqual(
            BidirectIndex().value(
                Path(self.dir_path, "BidirectIndexIncreaseAssignmentDecreaseAssignment.java")
            ),
            [3],
            "Could not find bidirect index when index increased with assignment and then decreased with assignment",
        )

    def test_bidirect_index_hidden_scope_true(self):
        self.assertEqual(
            BidirectIndex().value(Path(self.dir_path, "BidirectIndexHiddenScope.java")),
            [0],
            "Could not find bidirec index when scope is hidden",
        )

    def test_bidirect_index_outsider(self):
        self.assertEqual(
            BidirectIndex().value(Path(self.dir_path, "BidirectIndexOutsider.java")),
            [10],
            "Could not find bidirec index when index is ot of loop",
        )
