from flask import Blueprint

licenses = Blueprint(name='licenses', import_name=__name__, url_prefix='/api')

@licenses.get('/licenses')
def list_licenses():
    return "Not implemented", 501

@licenses.get('/licenses/<license>')
def validate_license(license):
    return "Not implemented", 501


@licenses.post('/licenses')
def create_new_license():
    return "Not implemented", 501


@licenses.delete('/licenses/<license>')
def revoke_license(license):
    return "Not implemented", 501

