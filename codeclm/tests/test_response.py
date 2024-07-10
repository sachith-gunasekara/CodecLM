import sys
import unittest

from pyprojroot import here
sys.path.append(str(here('codeclm')))

from helpers.response import extract_encoded_metadata_from_response

class TestResponse(unittest.TestCase):
    def test_extract_encoded_metadata_from_response(self):
        response = "Use case: general knowledge question answering\nSkills: art history, comparison"
        target = {
            'use_case': 'general knowledge question answering',
            'skills': ['art history', 'comparison']
        }

        source = extract_encoded_metadata_from_response(response)

        self.assertEqual(source, target)

if __name__ == '__main__':
    unittest.main(verbosity=2)