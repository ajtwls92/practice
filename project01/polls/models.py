from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 객체를 설명하는 문자열을 정의하는 메서드
    def __str__(self):
        return f'{self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 객체를 설명하는 문자열을 정의하는 메서드
    def __str__(self):
        return f'{self.choice_text}'

