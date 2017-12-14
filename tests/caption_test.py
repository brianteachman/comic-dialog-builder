from tkinter import *
from tkinter import ttk
import unittest
from caption import Caption


class TestCaption(unittest.TestCase):

    def setUp(self):
        # self.canvas = Canvas(Tk()) # doesn't work when passing canvas around
        self.canvas = Canvas(Toplevel())
        self.caption = Caption(self.canvas)
        # self.caption.override_id(1)

    def tearDown(self):
        self.canvas = None

    # def test_each_new_caption_gets_unique_id(self):
    #     for i in range(10):
    #         caption = Caption(self.canvas)
    #         caption.create_caption("Something_" + str(caption.get_id()))

    def test_can_override_caption_id(self):
        self.caption.override_id(1)
        self.assertEqual(self.caption.get_id(), 1, msg='Guaranteed 1st Caption ID equals 1.')

    def test_caption_id_increments_on_new(self):
        self.caption.override_id(1)
        self.assertEqual(self.caption.get_id(), 1, msg='1st Caption ID equals 1.')
        self.caption = Caption(self.canvas)
        self.assertEqual(self.caption.get_id(), 2, msg='2st Caption ID equals 2.')
        self.caption = Caption(self.canvas)
        self.assertEqual(self.caption.get_id(), 3, msg='3nd Caption ID equals 3.')

    def test_can_set_caption_text(self):
        caption = Caption(self.canvas)
        self.assertNotEqual(caption.get_text(), 'Aha!')
        caption.set_text('Aha!')
        self.assertEqual(caption.get_text(), 'Aha!')

    def test_create_caption_func(self):
        self.caption = Caption(self.canvas)
        self.caption.create_caption('Aha!')
        # self.caption.override_id(1)
        self.assertEqual(self.caption.get_id(), 5) # 4 prior Caption's created
        self.assertEqual(self.caption.get_text(), 'Aha!')


if __name__ == '__main__':
    unittest.main()
