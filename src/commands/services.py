import logging
import urllib.parse
from io import BytesIO

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
        c = request.raw_request.content
        s = BytesIO(await c.read())

        for record in reader(s):
            logger.info(record)

        log = await c.json(loads=urllib.parse.parse_qs)

        logger.info(log)
