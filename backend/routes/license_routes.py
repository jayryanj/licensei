from flask import Blueprint
from backend.services import license_service

licenses = Blueprint(name='licenses', import_name=__name__, url_prefix='/api')

@licenses.get('/licenses')
def list_licenses():
    return {"licenses": license_service.list_all_licenses()}, 200

@licenses.get('/licenses/<license>')
def validate_license(license):
    return "Not implemented", 501


@licenses.post('/licenses')
def create_new_license():
    return "Not implemented", 501


@licenses.delete('/licenses/<license>')
def revoke_license(license):
    return "Not implemented", 501

