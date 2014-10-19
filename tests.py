import unittest
import path

p = path.Path(r'C:\Documents and Settings\Mahan')

class PathTest(unittest.TestCase):
    def test_comp(self):
        self.assertEqual(p.full, r'C:\Documents and Settings\Mahan')
        self.assertEqual(p.path, r'C:\Documents and Settings\Mahan')
        self.assertEqual(p.drive, r'C:')
        self.assertEqual(p.dir, r'C:\Documents and Settings')
        self.assertEqual(p.filedir, r'Documents and Settings')
        self.assertEqual(p.file, r'Mahan')
        self.assertEqual(p.name, r'Mahan')
        self.assertEqual(p.ext, r'')

if __name__ == '__main__':
    unittest.main(verbosity=3)
