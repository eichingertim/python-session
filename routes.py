from flask import jsonify

from route_utils import *
from middleware import *


def init_routes(app):
    app.add_url_rule(INFO, 'info', info)
    app.add_url_rule(DB, 'db', db, methods=['GET'])
    app.add_url_rule(HELLO, 'hello', hello)
    app.add_url_rule(API, 'list_routes', list_routes, defaults={'app': app})
    app.add_url_rule(USER_PROFILE, 'user_profile', user_profile)
    app.add_url_rule(PERSON, 'person', person)
    app.add_url_rule(PERSON, 'person_add', person_add, methods=['POST'])
    app.add_url_rule(PERSON, 'person_update', person_update, methods=['PUT'])


def list_routes(app):
    routes = list()
    for route in app.url_map.iter_rules():
        routes.append({
            'Route': str(route),
            'Endpoint': route.endpoint,
            'Methods': list(route.methods)
        })

    return jsonify({'Routes': routes, 'Total': len(routes)})
