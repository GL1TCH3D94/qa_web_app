from django.test import SimpleTestCase
from django.urls import reverse, resolve
from skill_matrix import views

class TestUrls(SimpleTestCase):
    
    def test_master_url_is_resolved(self):
        url = reverse('master')
        self.assertEquals(resolve(url).func, views.master_view)

    def test_skill_url_is_resolved(self):
        url = reverse('skill')
        self.assertEquals(resolve(url).func, views.list_skills_view)

    def test_subject_url_is_resolved(self):
        url = reverse('subject')
        self.assertEquals(resolve(url).func, views.list_subjects_view)

    def test_update_subject_url_is_resolved(self):
        url = reverse('update_subject', args=[1])
        self.assertEquals(resolve(url).func, views.subject_update_view)

    def test_delete_subject_url_is_resolved(self):
        url = reverse('delete_subject', args=[1])
        self.assertEquals(resolve(url).func, views.subject_delete_view)

    def test_update_skill_url_is_resolved(self):
        url = reverse('update_skill', args=[1])
        self.assertEquals(resolve(url).func, views.skill_update_view)

    def test_delete_skill_url_is_resolved(self):
        url = reverse('delete_skill', args=[1])
        self.assertEquals(resolve(url).func, views.skill_delete_view)

    def test_deleted_url_is_resolved(self):
        url = reverse('deleted', args=[1])
        self.assertEquals(resolve(url).func, views.delete_view)

    def test_s_deleted_url_is_resolved(self):
        url = reverse('s_deleted', args=[1])
        self.assertEquals(resolve(url).func, views.s_delete_view)

    def test_add_skill_url_is_resolved(self):
        url = reverse('add_skill')
        self.assertEquals(resolve(url).func, views.skill_create_view)

    def test_add_subject_url_is_resolved(self):
        url = reverse('add_subject')
        self.assertEquals(resolve(url).func, views.subject_create_view)

    def test_invalid_user_url_is_resolved(self):
        url = reverse('invalid_user')
        self.assertEquals(resolve(url).func, views.invalid_user_view)