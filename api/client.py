import inspect
import logging

import requests

logger = logging.getLogger("example." + __name__)


class RestfulBookerClient:

    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def verify_response(
            self, res: requests.Response, ok_status=200
    ) -> requests.Response:
        func = inspect.stack()[1][3]
        if isinstance(ok_status, int):
            ok_status = [ok_status]
        if res.status_code not in ok_status:
            raise ValueError(
                f"Verified response: function {func} failed: "
                f"server responded {res.status_code} "
                f"with data: {res.content}"
            )
        else:
            logger.info(
                f"Verified response: function {func} code {res.status_code}"
            )
        return res

    vr = verify_response

    def authorize(self, username, password):
        res = self.login(username, password)
        if res.status_code != 200:
            raise Exception("Unable to authorize using given credentials")
        session_token = res.json().get("token")
        cookie = requests.cookies.create_cookie("token", session_token)
        self._s.cookies.set_cookie(cookie)

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self._s.post(self.host + "/auth", json=data)

    def create_booking(self, data: dict):
        return self._s.post(self.host + "/booking", json=data)

    def update_booking(self, uid: int,  data: dict):
        return self._s.put(self.host + f"/booking/{uid}", json=data)

    def get_booking(self, uid: int):
        return self._s.get(self.host + f"/booking/{uid}")
