from django.urls import reverse, resolve


class TestUrls:

    def test_signup_url(self):
        path = reverse('signup')
        assert resolve(path).view_name == 'signup'

    def test_home_url(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'

    def test_student_create_url(self):
        path = reverse('student-create')
        assert resolve(path).view_name == 'student-create'

    def test_student_list_url(self):
        path = reverse('student-list')
        assert resolve(path).view_name == 'student-list'

    # def test_student_rud_url(self):
    #     path = reverse('student-rud')
    #     assert resolve(path).view_name == 'student-rud'
