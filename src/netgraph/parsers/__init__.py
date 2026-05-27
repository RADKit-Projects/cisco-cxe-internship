"""Parser package."""

from netgraph.parsers.base import Parser
from netgraph.parsers.lldp import LldpParser

__all__ = ["Parser", "LldpParser"]
