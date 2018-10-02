import unittest
from decompound import decompound

class TestDecompound(unittest.TestCase):

  def test_examples(self):
    dictionary = [
      'Haus', 
      'besichtigung', 
      'vereinbarung', 
      'papier', 
      'drucken', 
      'maschiene',
      'auto',
      'bahn'
    ]

    self.assertEqual(decompound('', []), [])
    self.assertEqual(decompound('', dictionary), [])
    self.assertEqual(decompound('Autobahn', dictionary), [['Auto', 'bahn']])
    self.assertEqual(decompound('Autobahnen', dictionary), [['Auto', 'bahnen']])
    self.assertEqual(decompound('Autohausbesichtigung', dictionary), [['Auto', 'haus', 'besichtigung']])
    self.assertEqual(decompound('Häuserbesichtigungsvereinbarungspapierdruckmaschienen', dictionary), [['Häuser', 'besichtigungs', 'vereinbarungs', 'papier', 'druck', 'maschienen']])

if __name__ == '__main__':
    unittest.main()
