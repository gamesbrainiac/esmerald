from esmerald import patch, post, put
from esmerald.routing.apis.generics import CreateAPIView


class UserAPI(CreateAPIView):
    """
    CreateAPIView only allows the `post`, `put` and `patch`
    to be used by default.
    """

    @post()
    async def post(self) -> str:
        ...

    @put()
    async def put(self) -> str:
        ...

    @patch()
    async def patch(self) -> str:
        ...
