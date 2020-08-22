from django.core.exceptions import ValidationError
from django.test import SimpleTestCase
from .models import Vaccination, validate_rut


class RutTestCase(SimpleTestCase):
    def test_rut_validator(self):
        """RUTs are correctly validated"""
        error_invalid = 'The Chilean RUT is not valid.'

        ruts = {
            "0-0": None,
            "1-9": None,
            "253601639": None,
            "25.360.163-9": None,
            "76079824-K": None,
            "253601638": error_invalid,
            "25.360.16-9": error_invalid,
            "76079825-K": error_invalid,
            "76.079.825-K": error_invalid,
            "76079825-k": error_invalid,
            "76.079.825-k": error_invalid,
            "76.079825-k": error_invalid,
            "07679825-k": error_invalid,
            "07679825-k": error_invalid,
        }

        for rut in ruts:
            try:
                self.assertEqual(validate_rut(rut), ruts[rut])
            except ValidationError:
                # self.assertEqual(e.message, ruts[rut])
                self.assertIsNotNone(ruts[rut])
