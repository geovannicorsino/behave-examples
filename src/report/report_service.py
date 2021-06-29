def scenerios_count(scenarios):
    fp = 0
    # print(scenarios)
    fp = len(list(map(lambda x: + 1 if x.feature.status == 'passed' else + 0, scenarios)))
    stp = len(list(map(lambda x: + 1 if x.steps.status == 'passed' else + 0, scenarios)))
    return fp, stp


def report(scenarios):
    fp, stp = scenerios_count(scenarios)
    message = f"{fp} feature passed, {stp} steps passed"
    print(message)
