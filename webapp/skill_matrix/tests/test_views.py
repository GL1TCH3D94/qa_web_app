from django.test import TestCase, Client
from django.urls import reverse
from skill_matrix import models
from datetime import datetime
from django.contrib.auth import authenticate, login, logout, get_user_model
import json

class TestViews(TestCase):

    def setUp(self):

        User = get_user_model()

        self.client = Client()

        self.super_username = 'super@gmail.com'
        self.super_password = 'Super@123'  
        super_user = User.objects.create_superuser(username=self.super_username)
        super_user.set_password(self.super_password)
        super_user.save()

        self.username = 'dummy@gmail.com'
        self.password = 'Dummy@123'
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        self.subject1 = models.Subject.objects.create(
            name = 'Science',
            description = 'Description',
            field = 'Physics'
        )

        self.skill1 = models.Skill.objects.create(
            subject = self.subject1,
            current_level = 5,
            required_level = 10,
            last_updated = datetime.now(),
            user = user
        )  
    
    def test_project_master_view_GET_unauthorised_redirects(self):
        response = self.client.get(reverse('master'))
        self.assertEquals(response.status_code, 302)

    def test_project_master_view_GET_standard_authorised_redirects(self):
        self.client_object = self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('master'))
        self.assertEquals(response.status_code, 302)

    def test_project_master_view_GET_super_authorised_redirects(self):
        self.client_object = self.client.login(username=self.super_username, password=self.super_password)

        response = self.client.get(reverse('master'))
        self.assertEquals(response.status_code, 200)

    def test_project_list_skills_view_GET_unauthorised_redirects(self):
        response = self.client.get(reverse('skill'))
        self.assertEquals(response.status_code, 302)

    def test_project_list_skills_view_GET_authorised_200(self):
        self.client_object = self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('skill'))
        self.assertEquals(response.status_code, 200)

    def test_project_list_subjects_view_GET_unauthorised_redirects(self):
        response = self.client.get(reverse('subject'))
        self.assertEquals(response.status_code, 302)

    def test_project_list_subjects_view_GET_authorised_200(self):
        self.client_object = self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('subject'))
        self.assertEquals(response.status_code, 200)

    def test_project_update_subject_view_GET_unauthorised_redirects(self):
        response = self.client.get(reverse('update_subject', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_project_update_subject_view_GET_authorised_200(self):
        self.client_object = self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('update_subject', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_project_delete_subject_view_GET_unauthorised_redirects(self):
        response = self.client.get(reverse('delete_subject', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_project_delete_subject_view_GET_authorised_200(self):
        self.client_object = self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('delete_subject', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_project_deleted_view_GET_unauthorised_redirects(self):
        response = self.client.get(reverse('deleted', args=[1]))
        self.assertEquals(response.status_code, 302)

    
    def test_project_deleted_view_GET_standard_authorised_redirects_to_admin(self):
        self.client_object = self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('deleted', args=[1]))
        self.assertRedirects(response, '/admin/login/?next=/skill_matrix/deleted/1', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    def test_project_deleted_view_GET_super_authorised_redirect_to_skill(self):
        self.client_object = self.client.login(username=self.super_username, password=self.super_password)

        response = self.client.get(reverse('deleted', args=[1]))
        self.assertRedirects(response, '/skill_matrix/skill', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    def test_project_s_deleted_view_GET_unauthorised_redirects_to_admin(self):
        response = self.client.get(reverse('s_deleted', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_project_s_deleted_view_GET_standard_authorised_redirects(self):
        self.client_object = self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('s_deleted', args=[1]))
        self.assertRedirects(response, '/admin/login/?next=/skill_matrix/s_deleted/1', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    def test_project_s_deleted_view_GET_super_authorised_redirects_to_subject(self):
        self.client_object = self.client.login(username=self.super_username, password=self.super_password)

        response = self.client.get(reverse('s_deleted', args=[1]))
        self.assertRedirects(response, '/skill_matrix/subject', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    def test_project_add_skill_view_GET_unauthorised_redirects(self):
        response = self.client.get(reverse('add_skill'))
        self.assertEquals(response.status_code, 302)

    def test_project_add_skill_view_GET_authorised_200(self):
        self.client_object = self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('add_skill'))
        self.assertEquals(response.status_code, 200)

    def test_project_add_subject_view_GET_unauthorised_redirects(self):
        response = self.client.get(reverse('add_subject'))
        self.assertEquals(response.status_code, 302)

    def test_project_add_subject_view_GET_authorised_200(self):
        self.client_object = self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse('add_subject'))
        self.assertEquals(response.status_code, 200)

    def test_project_invalid_user_view_GET_unauthorised(self):
        response = self.client.get(reverse('invalid_user'))
        self.assertEquals(response.status_code, 200)
