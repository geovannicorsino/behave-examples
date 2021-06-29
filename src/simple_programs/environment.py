from src.report.report_service import report


def before_all(context):
    context.scenarios = []


def after_scenario(context, scenario):
    context.scenarios.append(scenario)


def after_all(context):
    report(context.scenarios)
