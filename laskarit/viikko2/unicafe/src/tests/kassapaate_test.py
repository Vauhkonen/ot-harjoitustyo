import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
        self.rahaton = Maksukortti(10)

    def assert_kassapaate(self, rahaa, e, m):
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
        self.assertEqual(self.kassapaate.edulliset, e)
        self.assertEqual(self.kassapaate.maukkaat, m)

    def test_paate_luotu_oikein(self):
        self.assert_kassapaate(100000, 0, 0)

    def test_edullisen_kateisosto(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(vaihtoraha, 760)
        self.assert_kassapaate(100240, 1, 0)

    def test_maukkaan_kateisosto(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(vaihtoraha, 600)
        self.assert_kassapaate(100400, 0, 1)

    def test_edullisen_kateisosto_vajaalla_rahalla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
        self.assert_kassapaate(100000, 0, 0)

    def test_maukkaan_kateisosto_vajaalla_rahalla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assert_kassapaate(100000, 0, 0)

    def test_edullisen_korttiosto(self):
        onnistuiko =  self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(onnistuiko, True)
        self.assert_kassapaate(100000, 1, 0)
        self.assertEqual(str(self.kortti), "saldo: 7.6")

    def test_maukkaan_korttiosto(self):
        onnistuiko = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(onnistuiko, True)
        self.assert_kassapaate(100000, 0, 1)
        self.assertEqual(str(self.kortti), "saldo: 6.0")

    def test_edullisen_korttiosoto_ilman_rahaa(self):
        onnistuiko = self.kassapaate.syo_edullisesti_kortilla(self.rahaton)
        self.assertEqual(onnistuiko, False)
        self.assert_kassapaate(100000, 0, 0)

    def test_maukkaan_korttiosto_ilman_rahaa(self):
        onnistuiko = self.kassapaate.syo_maukkaasti_kortilla(self.rahaton)
        self.assertEqual(onnistuiko, False)
        self.assert_kassapaate(100000, 0, 0)

    def test_rahan_lataus_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assert_kassapaate(101000, 0, 0)

    def test_negatiivisen_rahan_lataus_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)
        self.assert_kassapaate(100000, 0, 0)
