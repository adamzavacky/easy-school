from django.utils import timezone
from mixer.backend.django import mixer

from students.models import FeeType
from teachers.models import Teacher
from course.models import Course

import pytest


def create_user(user_id=6, date_of_joining=timezone.now(),
                gender='M', date_of_birth='1997-05-27', cnic='adamkoo', phone_no='0944194324',
                address='Wonderland', is_teaching=True):
    return Teacher.objects.create(user_id=user_id, date_of_joining=date_of_joining, gender=gender,
                                  date_of_birth=date_of_birth, cnic=cnic, phone_no=phone_no, address=address,
                                  is_teaching=is_teaching)


@pytest.mark.django_db
class TestModels:

    def test_teacher_full_name(self):
        fullname = mixer.blend('teachers.Teacher')
        assert fullname == fullname

    def test_user_creation(self):
        t = create_user()
        assert isinstance(t, Teacher)

    def test_fee_type(self):
        fee_type = FeeType.objects.create(
            name='C',
            display_name='Cash',
            amount=50
        )
        assert fee_type.name == 'C'
        assert fee_type.display_name == 'Cash'
        assert fee_type.amount == 50

    def test_course(self):
        course = Course.objects.create(
            course_name='New course',
            course_description='new course'
        )
        assert course.course_name == 'New course'
        assert course.course_description == 'new course'