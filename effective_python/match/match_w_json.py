from dataclasses import dataclass
import json

@dataclass
class PersonCustmomer:
    first_name: str
    last_name: str

@dataclass
class BusinessCustomer:
    company_name: str

record1= """{"customer": {"last": "Ross", "first": "Bob"}}"""
record2="""{"customer": {"entity": "Nestor's pizzeria"}}"""


def deserialize(data):
    record = json.loads(data)
    match record:
        case {"customer": {"last": last_name,
                           "first": first_name}}:
            return PersonCustmomer(first_name,last_name)
        case {"customer": {"entity": company_name}}:
            return BusinessCustomer(company_name)
        case _:
            raise ValueError("Unknown record type")

print("Record1:", deserialize(record1))
print("Record2:", deserialize(record2))