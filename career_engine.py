def analyze_student(answers):

    scores = {
        "علوم الحاسب": 0,
        "الأمن السيبراني": 0,
        "الذكاء الاصطناعي": 0,
        "علوم البيانات": 0,
        "هندسة البرمجيات": 0
    }

    scores["علوم الحاسب"] += answers["logic"] * 2
    scores["الأمن السيبراني"] += answers["security"] * 2
    scores["الذكاء الاصطناعي"] += answers["ai"] * 2
    scores["علوم البيانات"] += answers["data"] * 2
    scores["هندسة البرمجيات"] += answers["software"] * 2

    total = sum(scores.values())

    results = []

    for field, score in scores.items():

        percentage = round(
            (score / total) * 100,
            2
        )

        results.append(
            (field, percentage)
        )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results