from behave import given, when, then


@given('there is a hello world app')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given there is a hello world app')


@when('run the app')
def step_impl(context):
    raise NotImplementedError(u'STEP: When run the app')


@then('there is an output of {text}')
def step_impl(context, text):
    raise NotImplementedError(u'STEP: Then there is an output of hello world')
