"""Some useful base classes to inherit from."""
from abc import abstractmethod
from typing import Any, Callable, Dict, List, TYPE_CHECKING, Tuple, Type
from betterproto.lib.google.protobuf import Any as Any_pb
from betterproto import Message

from .json import JSONSerializable, dict_to_data

if TYPE_CHECKING:
    from ..core.msg import Msg


class BaseTerraData(JSONSerializable, Message):

    type: str
    type_url: str

    def to_data(self) -> dict:
        return {"type": self.type_url, "value": dict_to_data(self.__dict__)}

    @abstractmethod
    def to_proto(self):
        pass


def create_demux(inputs: List) -> Callable[[Dict[str, Any]], Any]:
    table = {i.type_url: i.from_data for i in inputs}

    def from_data(data: dict):
        return table[data["@type"]](data)

    return from_data


def create_demux_proto(protos: List[Tuple[str, Type[Message]]], msg_types: List[Type['Msg']]) -> Callable[[Any_pb], 'Msg']:
    proto_table = {i[0]: i[1] for i in protos}
    msg_handlers = {t.__name__: t.from_proto for t in msg_types}

    def from_proto(data: Any_pb) -> 'Msg':
        pb = proto_table[data.type_url]().parse(data.value)
        return msg_handlers[type(pb).__name__](pb)

    return from_proto


def create_demux_amino(inputs: List) -> Callable[[Dict[str, Any]], Any]:
    table = {i.type_amino: i.from_amino for i in inputs}

    def from_amino(data: dict):
        return table[data["type"]](data)

    return from_amino
