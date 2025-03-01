from backend.db import postgres_repo

def list_all_licenses():
    return postgres_repo.get_all_licenses()
