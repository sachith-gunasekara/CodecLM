import sys
import unittest

from pyprojroot import here
sys.path.append(str(here()))

from codeclm.encoder import Encoder

class TestEncoder(unittest.TestCase):

    def test_generate_metadata(self):
        instruction = "Explain why the concept of chiaroscuro is significant in Baroque painting when contrasting it with the use of sfumato in the Renaissance period."
        encoder = Encoder(instruction)

        metadata = encoder.generate_metadata()

        print('\n', metadata)

        self.assertIsInstance(metadata, dict)
        self.assertIsInstance(metadata['use_case'], str)
        self.assertIsInstance(metadata['skills'], list)
        
        for skill in metadata['skills']:
            self.assertIsInstance(skill, str)

if __name__ == '__main__':
    unittest.main(verbosity=2)