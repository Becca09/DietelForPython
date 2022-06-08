import unittest


class playgroundTest(unittest.TestCase):

    def setUp(self) -> None:
        print("i run before")

    def tearDown(self) -> None:
        print("i run after")


if __name__ == '__main__':
    unittest.main()
