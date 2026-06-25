import re
from model.db.persondb import *


def valid_name(text):
    return bool(re.match(r'^[a-zA-Z\s]{2,20}$', text))


def valid_national_id(text):
    return bool(re.match(r'^\d{10}$', text))


def save(name, family, national_id):
    try:
        if valid_name(name) and valid_name(family) and valid_national_id(national_id):
            save_person(name, family, national_id)
            return True, "saved"
        else:
            return False, "invalid data"

    except Exception as e:
        return False, str(e)


def edit(id, name, family, national_id):
    try:
        if id > 0 and valid_name(name) and valid_name(family) and valid_national_id(national_id):
            edit_person(id, name, family, national_id)
            return True, "edited"
        else:
            return False, "invalid data"

    except Exception as e:
        return False, str(e)


def remove(id):
    try:
        if id > 0:
            remove_person(id)
            return True, "Removed"
        else:
            return False, "Invalid ID"

    except Exception as e:
        return False, str(e)


def find_all():
    try:
        return find_all_person()
    except Exception as e:
       return False,str(e)

def find_by_family(family):
    try:
        return find_by_family_person(family)
    except Exception as e:
        return False, str(e)
