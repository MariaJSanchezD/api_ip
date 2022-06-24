import unittest
import db

class testdb(unittest.TestCase):
    def test_selectAS(self):
        test_param = 13335
        result = db.database.selectAsNumber(db.database(), test_param)
        self.assertTrue(result)

    def test_selectIP(self):
        test_param = "1.0.0.0"
        result = db.database.selectIPadd(db.database(), test_param)
        self.assertTrue(result)


unittest.main()