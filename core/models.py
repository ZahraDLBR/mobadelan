from django.contrib.auth.models import AbstractUser
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    class Meta(object):
        unique_together = ('email',)

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bank_account = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=11)
    credit = models.PositiveIntegerField(default=200000)





class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    bank_account = models.CharField(max_length=16, default="111111111111111")
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    # tran = models.ManyToManyField(Quiz, through='TakenQuiz')
    # interests = models.ManyToManyField(Subject, related_name='interested_students')
    salary = models.PositiveIntegerField(default=1000000)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    credit = models.PositiveIntegerField(default=1000000)


class Transaction(models.Model):
    creator = models.ForeignKey(Customer, on_delete=models.CASCADE)
    corroborator = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)

    EXAM_GRE = 'GRE'
    EXAM_TOEFL = 'TFL'
    EXAM_IELTS = 'ILS'
    UNIVERSITY_EPFL = 'EPF'
    UNIVERSITY_MIT = 'MIT'
    UNIVERSITY_ETH = 'ETH'
    UNIVERSITY_OXFORD = 'OXF'
    INNER_TRANSFER = 'IN'
    OUTER_TRANSFER = 'OUT'
    RECHARGE_WALLET = 'RCH'

    TRANSACTIONS_TYPE_CHOICES = (
        (RECHARGE_WALLET, 'recharge wallet'),
        (OUTER_TRANSFER, 'outer transfer'),
        (INNER_TRANSFER, 'inner transfer'),
        (UNIVERSITY_EPFL, 'university of EPFL'),
        (UNIVERSITY_ETH, 'university of ETH'),
        (UNIVERSITY_OXFORD, 'university of Oxford'),
        (UNIVERSITY_MIT, 'university of MIT'),
        (EXAM_GRE, 'GRE exam'),
        (EXAM_IELTS, 'IELTS exam'),
        (EXAM_TOEFL, 'TOEFL exam'),

    )
    transactions_type = models.CharField(
        max_length=3,
        choices=TRANSACTIONS_TYPE_CHOICES,
        default=None,
    )

    WAIT = 'W'
    DONE = 'D'
    FAIL = 'F'

    STATE_CHOICES = (
        (WAIT, 'wait'),
        (DONE,'done'),
        (FAIL, 'fail')
    )
    state = models.CharField(
        max_length=1,
        choices=STATE_CHOICES,
        default='w'
    )

    create_time = models.DateTimeField(auto_now_add=True)

    value = models.PositiveIntegerField(default=0)
    is_invalid = models.BooleanField(default=False)



class Contact_msg(models.Model):
    email = models.EmailField()
    text = models.CharField('message', max_length=255)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=11)
    seen = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)


class Message(models.Model):

    sender = models.ForeignKey(User,related_name='send', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name='receive', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    text = models.CharField('message', max_length=100000)
    subject = models.CharField(max_length=255)
    seen = models.BooleanField(default=False)
