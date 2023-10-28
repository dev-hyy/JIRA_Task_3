from behave import given


@given('Open Reely page')
def open_reely(context):
    context.app.main_page.open_main()


@given('User enters login credentials')
def user_login(context):
    context.app.main_page.sign_in('somesurd@gmail.com', '9a$vF4V.)Qv,)>v')