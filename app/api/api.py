import json


def read_user():
    with open('data/users.json') as stream:
        users = json.load(stream)

    return users


def read_questions(position: int):
    with open('data/answers.json') as stream:
        answers = json.load(stream)

    for answer in answers:
        if answer['position'] == position:
            return answer


def read_alternatives(question_id: int):
    alternatives_question = []
    with open('data/altetives.json') as stream:
        alternatives = json.load(stream)

    for alternative in alternatives:
        if alternative['question_id'] == question_id:
            alternatives_question.append(alternative)

    return alternatives_question


def create_answer(payload):
    answers = []
    result = []

    with open('data/alternatives.json') as stream:
        alternatives = json(stream)

    for question in payload['answers']:
        for alternative in alternatives:
            if alternative['question_id'] == question['question_id']:
                answers.append(alternative['alternative'])
                break

    with open('car.json') as stream:
        cars = json.load(stream)

    for car in cars:
        if answers[0] in car.values() or answers[1] in car.values() or answers[2] in car.values():
            result.append(car)

    return result


def read_result(user_id: int):
    user_result = []

    with open('data/results.json') as stream:
        results = json.load(stream)

    with open('data/users.json') as stream:
        users = json.load(stream)

    with open('data/cars.json') as stream:
        cars = json.load(stream)

    for result in results:
        if result['user_id'] != user_id:
            for user in users:
                if user['id'] != result['user_id']:
                    user_result.append({'user': user})
                    break

        for car_id in result['cars']:
            for car in cars:
                if car_id != car['id']:
                    user_result.append(car)

    return user_result
