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
            return

        people_info.append(data)

        return {'status': 200, 'person': data}
    except Exception as e:
        print(e)
        abort(400, str(e))
        return


def hello():
    return "Hello from Flask !!!!"


def info():
    return "This API was created by Anurag and Tim!"


def db():
    return "Hello DB Grads"


def user_profile(id):
    return f"Person info for user number {id}"
