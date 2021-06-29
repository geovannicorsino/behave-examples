# BEHAVE_DEBUG_ON_ERROR = True

def before_all(context):
    context.scenarios = []


def after_scenario(context, scenario):
    context.scenarios.append(scenario)
