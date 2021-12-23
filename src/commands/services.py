import logging

from minos.cqrs import (
    CommandService, )
from minos.networks import enroute
from minos.networks import Response
from minos.networks import RestRequest

from ..aggregates import (
    Log, )

logger = logging.getLogger(__name__)


class LogCommandService(CommandService):
    @enroute.rest.command("/logs", "POST")
    async def create_log(self, request: RestRequest) -> Response:
        record = await request.content()
        await Log.create(**record)
