import unittest
from read import parse_file

# class test_utils(unittest.TestCase):
#     def test_dollar_replacer(self):
#         self.assertEqual(dollar_replacer("|a2010|22020"), "2010 2020")
#         self.assertEqual(dollar_replacer("|aSpMaBN"),"SpMaBN")
#     def test_dict_mapper(self):
#         self.assertEqual(
#             dict_mapper('''.001. |aXX458594'''), {'001:': '|aXX458594'}
#         )
#         self.assertEqual(
#             dict_mapper('''.001. |aXX458594\n.001. 4 |a1234'''), {'001:': '|aXX458594', "001:1": "|a1234"}
#         )
if __name__ == '__main__':
    unittest.main()