from unittest import TestCase

from utils.text_conversor import text_conversor


class TestConvertText(TestCase):
    def test_convert_text_to_minute_latters_and_strip_accets(self):

        """strip text and convert to minute letters"""

        convert_result = text_conversor("DESCRIÇÃO")

        self.assertEqual(convert_result, "descricao")
