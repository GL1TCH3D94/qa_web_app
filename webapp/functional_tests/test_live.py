from selenium import webdriver
from skill_matrix import models
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from django.urls import reverse
import time
from django.contrib.auth import authenticate, login, logout, get_user_model

class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')

        User = get_user_model()

        self.username = 'standardUser'
        self.password = 'Correct@123'  
        self.email = 'user@user.net'
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        self.super_username = 'superUser'
        self.super_password = 'Super@123'  
        super_user = User.objects.create_superuser(username=self.super_username)
        super_user.set_password(self.super_password)
        super_user.save()

    def tearDown(self):
        self.browser.close()

    def test_sql_injection_from_valid_user(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(by=By.LINK_TEXT, value='Skills').click()
        self.browser.find_element(by=By.LINK_TEXT, value='Login').click()
        self.browser.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.browser.find_element(by=By.NAME, value='password').send_keys(self.password)
        self.browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/form/div/div/div/div[4]/div[3]/div[2]/div/div/button').click()
        self.browser.find_element(by=By.LINK_TEXT, value='Add Subject').click()
        self.browser.find_element(by=By.NAME, value='name').send_keys('Maths')
        self.browser.find_element(by=By.NAME, value='description').send_keys('Hard')
        self.browser.find_element(by=By.NAME, value='field').send_keys("Sql statement'); DROP TABLE admin; --")
        self.browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/form/div/div/div/div[3]/div[3]/div[3]/div[2]/div/div/button').click()
        self.browser.find_element(by=By.LINK_TEXT, value='Subjects').click()
        time.sleep(2)
        self.browser.find_element(by=By.LINK_TEXT, value='Skills').click()
        self.browser.find_element(by=By.LINK_TEXT, value='Login').click()
        time.sleep(2)
        self.browser.find_element(by=By.NAME, value='username').send_keys(self.super_username)
        self.browser.find_element(by=By.NAME, value='password').send_keys(self.super_password)
        self.browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/form/div/div/div/div[4]/div[3]/div[2]/div/div/button').click()
        time.sleep(2)
        self.assertEquals(self.browser.find_element(by=By.CLASS_NAME, value="header").text, "SUPERUSER")
        
        
    def test_password_requirements_enforced_invalid_password(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(by=By.LINK_TEXT, value='Register').click()
        self.browser.find_element(by=By.NAME, value='username').send_keys('invalidUser')
        self.browser.find_element(by=By.NAME, value='email').send_keys('invalid@invalid.net')
        self.browser.find_element(by=By.NAME, value='password1').send_keys('User123')
        self.browser.find_element(by=By.NAME, value='password2').send_keys('User123')
        time.sleep(2)
        self.browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/form/div/div/div/div[3]/div[3]/div[4]/div[4]/div[2]/div/div/button').click()
        time.sleep(2)
        self.assertEquals(self.browser.current_url, self.live_server_url + "/accounts/register")

    def test_password_requirements_enforced_valid_password(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(by=By.LINK_TEXT, value='Register').click()
        self.browser.find_element(by=By.NAME, value='username').send_keys('validUser')
        self.browser.find_element(by=By.NAME, value='email').send_keys('valid@valid.net')
        self.browser.find_element(by=By.NAME, value='password1').send_keys(self.password)
        self.browser.find_element(by=By.NAME, value='password2').send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/form/div/div/div/div[3]/div[3]/div[4]/div[4]/div[2]/div/div/button').click()
        time.sleep(2)
        self.assertEquals(self.browser.current_url, self.live_server_url + "/")
        