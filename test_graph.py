from lab3 import inheritance_or_aggregation
import unittest

class TestGraph(unittest.TestCase):

    def test_inheritance(self):
        self.assertEqual(inheritance_or_aggregation(["A --> B", "C --> B", "B --> D", "D o-> B"], "B", "-->"),
                         ["A", "C"])

    def test_aggregation(self):
        self.assertEqual(inheritance_or_aggregation(["A --> B", "C --> B", "B --> D", "D o-> B"], "B", "o->"),
                         ["D"])

'''
Тесты, которые необходимо написать:
узнать как оценивать тестовое покрытие.

'''
