from dependency_injector.wiring import (
    Provide, )
from minos.cqrs import (
    QueryService, )

from .repositories import (
    LogQueryRepository, )


class LogQueryService(QueryService):
    repository: LogQueryRepository = Provide["log_repository"]
