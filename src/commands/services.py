import logging

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
        content = await request.raw_request.text()
        logger.info(content)
        pass
