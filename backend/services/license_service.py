import string
from datetime import datetime

from backend.db import postgres_repo
import secrets

from backend.db.license_type import LicenseType


def list_all_licenses():
    """
    Returns a list of all valid licenses

    :return:
    list: List of all licenses
    """
    return postgres_repo.get_all_licenses()


def create_new_license(
        product: str,
        expiration: str,
        description: str,
        license_type: str
):
    # Move constant out
    fmt = "%Y-%m-%d %H:%M:%S %z"
    license_type = license_type.lower()

    try:
        if license_type not in (t.name for t in LicenseType):
            raise ValueError(f"Invalid value for license_type: {license_type}")
        license_type = LicenseType[license_type].name

        if license_type != LicenseType.perpetual.name and not expiration:
            error_msg = f"Expiration date required for {license_type} license"
            raise Exception(error_msg)

        if license_type != LicenseType.perpetual.name:
            expiration = datetime.strptime(expiration, fmt)
        else:
            expiration = None

        # Generate license
        new_license = _generate_license()

        postgres_repo.insert_license(
            new_license=new_license,
            product=product,
            expiry=expiration,
            description=description,
            license_type=license_type
        )
        return new_license
    except ValueError:
        # TODO implement custom exception to return 400.
        # For now, this simply returns HTTP 200 {"license": null}
        # ValueError will be raised in two cases:
        # 1) license_type is incorrect
        # 2) expiration is incorrect
        pass
    except Exception as e:
        # TODO improve error handling. This case is too broad
        print(e)


# TODO move out to a util module
def _generate_license():
    """
    Generates a new random license key according to the following format:
    ####-####-####-####.
    16 alphanumerics (A-Z 0-9). All alphabetical characters capitalized.
    :return:
    str: license key
    """
    character_set = string.ascii_uppercase + string.digits
    new_license = '-'.join(
        ''.join(secrets.choice(character_set) for _ in range(4))
        for _ in range(4)
    )

    return new_license
