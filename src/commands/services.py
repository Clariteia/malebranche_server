import logging

from minos.cqrs import (
    CommandService,
)
from minos.networks import (
    Response,
    RestRequest,
    enroute,
)

from ..aggregates import (
    Log,
)

logger = logging.getLogger(__name__)


class LogCommandService(CommandService):
    @enroute.rest.command("/logs", "POST")
    async def create_log(self, request: RestRequest) -> Response:
        record = await request.content()
        await Log.create(**record)
