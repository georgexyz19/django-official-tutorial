from django.test import TestCase
import datetime

from django.utils import timezone
from .models import Question

from django.urls import reverse


class QuestionModelTests(TestCase):

    def test_recently_published_future(self):
        """
        was_published_recently() returns False for questions
        whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59,
                                                   seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(text, days):
    """ 
    days: positive future, negative in the past
    this is a help function for QuestionIndexViewTests
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=text, pub_date=time)


class QuestionIndexViewTests(TestCase):

    def test_no_question(self):
        """ database is blank by default during test """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest'], [])

    def test_past_question(self):
        create_question("Past question.", -30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['latest'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        create_question("Future question.", 30)
        response = self.client.get(reverse('index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(
            response.context['latest'],
            []
        )

    def test_future_and_past_question(self):
        create_question("Past question.", -30)
        create_question("Future question.", 30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['latest'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        create_question("Past question 1", -30)
        create_question("Past question 2", -5)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['latest'],
            ['<Question: Past question 2>', '<Question: Past question 1>']
        )


class QuestionDetailViewTests(TestCase):

    def test_past_question(self):
        q = create_question("Past question.", -5)
        response = self.client.get(reverse('detail', args=(q.id, )))
        self.assertContains(response, q.question_text)

    def test_future_question(self):
        q = create_question("Future question.", 5)
        response = self.client.get(reverse('detail', args=(q.id, )))
        self.assertEqual(response.status_code, 404)

