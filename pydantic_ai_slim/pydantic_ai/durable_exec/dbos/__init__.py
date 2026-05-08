from __future__ import annotations

from typing import TYPE_CHECKING

from ._agent import DBOSAgent, DBOSParallelExecutionMode
from ._model import DBOSModel
from ._utils import StepConfig

if TYPE_CHECKING:
    from ._mcp_toolset import DBOSMCPToolset

__all__ = ['DBOSAgent', 'DBOSModel', 'DBOSMCPToolset', 'DBOSParallelExecutionMode', 'StepConfig']


def __getattr__(name: str) -> object:
    if name == 'DBOSMCPToolset':
        from ._mcp_toolset import DBOSMCPToolset

        return DBOSMCPToolset
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
