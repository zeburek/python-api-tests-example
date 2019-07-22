from faker import Faker

faker = Faker()


def random_booking():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.pyint(),
        "depositpaid": True,
        "bookingdates": {
            "checkin": faker.iso8601()[:10],
            "checkout": faker.iso8601()[:10]
        },
        "additionalneeds": faker.word(),
    }
