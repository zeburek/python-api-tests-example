from random import randint

from api import random


class TestExample:

    def test_create_new_booking(self, client):
        data = random.random_booking()
        res = client.vr(client.create_booking(data), [200, 201])
        created = res.json()
        assert created.get("bookingid")
        assert created.get("booking") == data

    def test_new_booking_exists(self, client):
        data = random.random_booking()
        res = client.vr(client.create_booking(data), [200, 201])
        created = res.json()
        bookingid = created.get("bookingid")
        res = client.vr(client.get_booking(bookingid))
        exists = res.json()
        assert exists == data

    def test_update_booking(self, client):
        data = random.random_booking()
        res = client.vr(client.create_booking(data), [200, 201])
        created = res.json()
        bookingid = created.get("bookingid")
        data2 = random.random_booking()
        res = client.vr(client.update_booking(bookingid, data2))
        updated = res.json()
        assert updated == data2

    def test_not_existing_booking(self, client):
        res = client.get_booking(randint(10000, 99999))
        assert res.status_code == 404
