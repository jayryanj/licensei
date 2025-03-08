from flask import Blueprint, request

from backend.services import license_service

licenses = Blueprint(name='licenses', import_name=__name__, url_prefix='/api')


@licenses.get('/licenses')
def list_licenses():
    response = {
        "licenses": license_service.list_all_licenses()
    }
    return response, 200


@licenses.get('/licenses/<license>')
def validate_license(license):
    return "Not implemented", 501


@licenses.post('/licenses')
def create_new_license():
    request_body = request.get_json()
    product = request_body.get("product") or None
    expiration = request_body.get("expiration") or None
    description = request_body.get("description") or None
    # Need to validate missing field
    license_type = request_body.get("license_type")

    new_license = license_service.create_new_license(
        product=product,
        expiration=expiration,
        description=description,
        license_type=license_type
    )

    response = {
        "license": new_license
    }

    # 5xx should be handled by error handler
    # 4xx should be handled by validator
    return response, 200


@licenses.delete('/licenses/<license>')
def revoke_license(license):
    return "Not implemented", 501
