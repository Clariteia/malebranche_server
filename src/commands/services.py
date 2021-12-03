import logging
from asyncio import (
    StreamReader, )
from io import (
    BytesIO, )

from fastavro import (
    reader, )
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
        stream: StreamReader = request.raw_request.content
        content = BytesIO(await stream.read())

        for record in reader(content):
            logger.info(record)
            await Log.create(**record)
