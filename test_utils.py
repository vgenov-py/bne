import unittest
from utils import dict_mapper, dollar_replacer

s_t_1 = '''.000. |az n 0cza
.001. |aXX460733
.003. |aSpMaBN
.005. |a20191028142628.2
.008. |a031022 n anznnbabn          |a ana
.010.   |aXX460733
.016.   |aBNE20032766540
.024. 7 |ahttp://viaf.org/viaf/316734806|2viaf
.034.   |dW0055846|eW0055846|fN0425318|gN0425318|2ngn
.040.   |aSpMaBN|bspa|cSpMaBN|erdc|fembne
.042.   |a200310291444PCMPBC  BNEP 00
.080.   |a(460.181 Abelgas de Luna)|2mrf12
.151.   |aAbelgas de Luna
.451.   |aAbelgas de Luna (Entidad local menor)
.551.   |wg|aSena de Luna
.670.   |aELE|b(Abelgas de Luna)
.670.   |aNGN|b(Abelgas de Luna)
.781.   |zEspaña|zCastilla y León|zLeón (Provincia)|zSena de Luna|zAbelgas
de Luna
.856.   |uhttps://maps.google.es/maps?q=W005+58'46''N042+53'18'''''

class test_utils(unittest.TestCase):
    def test_dollar_replacer(self):
        self.assertEqual(dollar_replacer("|a2010|22020"), "2010 2020")
if __name__ == '__main__':
    unittest.main()