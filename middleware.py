from flask import jsonify, request, abort

people_info = [{'name': 'Lisa Simpson', 'age': 43, 'job': 'Saxophone player'},
               {'name': 'Bart Simpson', 'age': 47, 'job': 'Skateboarder'}]


def person():
    return jsonify(people_info)


def person_add():
    try:
        data = request.get_json(force=True)
        keys = data.keys()

        if 'name' not in keys or 'age' not in keys or 'job' not in keys:
            abort(400, 'Not all attributes are available')

        people_info.append(data)

        return {'status': 200, 'person': data}
    except Exception as e:
        print(e)
        abort(400, str(e))


def person_update():
    try:
        data = request.get_json(force=True)
        keys = data.keys()

        if 'name' not in keys:
            abort(400, 'Name and one other required attribute not specified')

        if 'age' not in keys and 'job' not in keys:
            abort(400, 'Name and one other required attribute not specified')

        found = False

        for i, person in enumerate(people_info):
            if person['name'] == data['name']:

                try:
                    people_info[i]['age'] = data['age']
                except:
                    print('age should not be changed')

                try:
                    people_info[i]['job'] = data['job']
                except:
                    print('job should not be changed')
                found = True

        print('Found')

        if found:
            return {'status': 200, 'person': data}
        else:
            abort(400, 'Person cannot be updated. Person not available')
    except Exception as e:
        print(e)
        abort(400, str(e))


def hello():
    return "Hello from Flask !!!!"


def info():
    return "This API was created by Anurag and Tim!"


def db():
    return "Hello DB Grads"


def user_profile(id):
    return f"Person info for user number {id}"
