from __future__ import (
    annotations,
)

from minos.common import MinosConfig
from minos.common import MinosSetup
from sqlalchemy import (
    create_engine,
)
from sqlalchemy.orm import (
    sessionmaker,
)

from .models import (
    META,
)


class LogQueryRepository(MinosSetup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = create_engine(
            "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
                **kwargs
            )
        )
        self.session = sessionmaker(bind=self.engine)()

    async def _setup(self) -> None:
        META.create_all(self.engine)

    @classmethod
    def _from_config(cls, *args, config: MinosConfig, **kwargs) -> LogQueryRepository:
        return cls(
            *args,
            **(config.repository._asdict() | {"database": "log_query_db"}) | kwargs
        )
