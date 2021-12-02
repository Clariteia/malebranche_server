import logging
import urllib.parse

from fastavro import reader
from minos.cqrs import (
    CommandService,
)
from minos.networks import (
    RestRequest,
    Response,
    enroute,
)

logger = logging.getLogger(__name__)


class LogCommandService(CommandService):
    @enroute.rest.command("/logs", "POST")
    async def create_log(self, request: RestRequest) -> Response:
        c = await request.raw_request.content.read()
        for record in reader(c):
            logger.info(record)

        log = await c.json(loads=urllib.parse.parse_qs)

        logger.info(log)
