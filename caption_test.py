from tkinter import *
from tkinter import ttk
import unittest
from caption import Caption


class TestCaption(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(Tk())
        self.caption = Caption(self.canvas)
        # self.caption.overrideId(1)

    def tearDown(self):
        self.canvas = None

    def test_can_override_caption_id(self):
        self.caption.overrideId(1)
        self.assertEqual(self.caption.getId(), 1, msg='Guaranteed 1st Caption ID equals 1.')

    def test_caption_id_increments_on_new(self):
        self.caption.overrideId(1)
        self.assertEqual(self.caption.getId(), 1, msg='1st Caption ID equals 1.')
        self.caption = Caption(self.canvas)
        self.assertEqual(self.caption.getId(), 2, msg='2st Caption ID equals 2.')
        self.caption = Caption(self.canvas)
        self.assertEqual(self.caption.getId(), 3, msg='3nd Caption ID equals 3.')

    # def test_each_new_caption_gets_unique_id(self):
    #     for i in range(10):
    #         caption = Caption(self.canvas)
    #         caption.createCaption("Something_" + str(caption.getId()))

    def test_can_set_caption_text(self):
        caption = Caption(self.canvas)
        self.assertNotEqual(caption.getText(), 'Aha!')
        caption.setText('Aha!')
        self.assertEqual(caption.getText(), 'Aha!')

    def test_create_caption_func(self):
        self.caption = Caption(self.canvas)
        self.caption.createCaption('Aha!')
        self.assertEqual(self.caption.getId(), 1)
        self.assertEqual(self.caption.getText(), 'Aha!')


if __name__ == '__main__':
    unittest.main()
