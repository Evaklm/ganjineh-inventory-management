import unittest

from inventory_example import InventoryPosition


class InventoryPositionTests(unittest.TestCase):
    def test_shortage_and_projection(self):
        position = InventoryPosition(physical=18, reserved=23, incoming=12)
        self.assertEqual(position.available, 0)
        self.assertEqual(position.shortage, 5)
        self.assertEqual(position.projected_available, 7)

    def test_negative_quantities_are_rejected(self):
        with self.assertRaises(ValueError):
            InventoryPosition(physical=-1, reserved=0)


if __name__ == "__main__":
    unittest.main()

