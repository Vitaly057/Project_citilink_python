import os
import allure
from citilink_test_project.data.users import User
from citilink_test_project.pages.ui_pages.main_page import main_page
from selene import browser

@allure.epic('Authorized')
@allure.label("owner", "flowerfrog")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')

def test_authorization_registered_user():

    user = User(
        name=os.getenv('REGISTERED_USER_NAME'),
        password=os.getenv('REGISTERED_USER_PASSWORD')
    )
    browser.element('Войти').click()

    with allure.step("Open the main page"):
       main_page.open()

   with allure.step("Filling the authorization form"):
       main_page.filling_authorization_form(user)

   with allure.step("Checking that user has been authorized"):
        main_page.main_page.user_must_be_authorized(user)
