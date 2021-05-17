# BEHAVE_DEBUG_ON_ERROR = True

def before_all(context):
    context.scenarios = []
    context.name_qa = "Geovanni Corsino"


def after_scenario(context, scenario):
    context.scenarios.append(scenario)


def after_all(context):
    print(f"--------{context.name_qa}------------")
    [print(scenario) for scenario in context.scenarios if scenario.status != "failed"]