import unittest
from boggle2 import boggle_checker, board_generate, guess_generate, get_adj_positions


class PrimesTestCase(unittest.TestCase):
    """Tests for `boggle2.py."""

    def test_is_A_in_board_of_A(self):
        """Is A successfully found in a board of only A's?"""
        self.assertTrue(boggle_checker([["A", "A", "A"],["A", "A", "A"],["A", "A", "A"]], "AAA"))

    def test_is_B_in_board_of_A(self):
        """"Is B found to not be in a board of only A's?"""
        self.assertFalse(boggle_checker([["A", "A", "A"],["A", "A", "A"],["A", "A", "A"]], "B"))

    def test_is_a_letter_used_twice(self):
        """"Is it possible that a letter will be reused?"""
        self.assertFalse(boggle_checker([["A", "A", "A"],["A", "B", "A"],["A", "A", "A"]], "BAB"))

    def test_will_negative_coordinates_be_returned(self):
        """given an illegal (negative) position will the function return illegal positions"""
        self.assertTrue(get_adj_positions(-3, -3, 3) == [])

    def test_will_coordinates_be_returned_off_the_board(self):
        """given an illegal (positive) position will the function return illegal positions?"""
        self.assertTrue(get_adj_positions(5, 5, 3) == [])

    def test_will_edge_coordinates_be_returned(self):
        """given an edge position will the function return any positions?"""
        self.assertTrue(get_adj_positions(2, 2, 3) != [])

    def test_will_corner_coordinates_return_three_positions(self):
        """given a corner position will the function return 3 positions?"""
        self.assertTrue((len(get_adj_positions(0, 2, 3))) == 3)

    def test_will_center_coordinates_return_eight_positions(self):
        """given a centre position will the function return 8 positions?"""
        self.assertTrue((len(get_adj_positions(1, 1, 3))) == 8)


if __name__ == '__main__':
    unittest.main()