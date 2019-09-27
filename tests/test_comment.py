import unittest
from app.models import Comment, User
from app import db

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username='Christine', password='potato', email='christine@ms.com')
        self.new_comment = Comment(comment_id=12345, text='This is awesome', user=self.user_James)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_id, 12345)
        self.assertEquals(self.new_comment.pitch_comment,'This is awesome')
        self.assertEquals(self.new_comment.user, self.user_James)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)
