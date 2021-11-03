from dependency_injector.wiring import (
    Provide,
)
from minos.common import (
    UUID_REGEX,
    AggregateDiff,
)
from minos.cqrs import (
    QueryService,
)
from minos.networks import (
    Request,
    Response,
    ResponseException,
    enroute,
)

from .repositories import (
    LogQueryRepository,
)


class LogQueryService(QueryService):
    repository: LogQueryRepository = Provide["log_repository"]
