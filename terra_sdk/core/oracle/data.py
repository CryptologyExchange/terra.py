from __future__ import annotations

import attr

from terra_sdk.core import Coin, Dec

__all__ = [
    "ExchangeRatePrevote",
    "ExchangeRateVote",
    "AggregateExchangeRatePrevote",
    "AggregateExchangeRateVote",
]


@attr.s
class AggregateExchangeRateVote:

    exchange_rate_tuples: Coins = attr.ib(converter=Coins)
    voter: str = attr.ib()

    def to_data(self) -> dict:
        return {
            "exchange_rate_tuples": [
                {"denom": x.denom, "exchange_rate": str(x.amount)}
                for x in self.exchange_rate_tuples
            ],
            "voter": self.voter,
        }

    @classmethod
    def from_data(cls, data) -> AggregateExchangeRateVote:
        return cls(
            exchange_rate_tuples=Coins(
                [Coin(d.denom, d.exchange_rate) for d in data["exchange_rate_tuples"]],
                voter=data["voter"],
            )
        )


@attr.s
class AggregateExchangeRatePrevote:

    hash: str = attr.ib()
    voter: ValAddress = attr.ib()
    submit_block: int = attr.ib(converter=int)

    def to_data(self) -> dict:
        return {
            "hash": self.hash,
            "voter": self.voter,
            "submit_block": str(self.submit_block),
        }

    @classmethod
    def from_data(cls, data) -> AggregateExchangeRateVote:
        return cls(
            hash=data["hash"],
            voter=data["voter"],
            submit_block=int(data["submit_block"]),
        )


@attr.s
class ExchangeRateVote:

    exchange_rate: Coin = attr.ib(converter=Coin.parse)
    denom: str = attr.ib()
    voter: ValAddress = attr.ib()

    def to_data(self) -> dict:
        return {
            "exchange_rate": str(self.exchange_rate.amount),
            "denom": self.denom,
            "voter": self.voter,
        }

    @classmethod
    def from_data(cls, data) -> ExchangeRateVote:
        xr = Coin(data["denom"], data["exchange_rate"])
        return cls(exchange_rate=xr, denom=xr.denom, voter=data["voter"])


@attr.s
class ExchangeRateVote:

    exchange_rate: Coin = attr.ib(converter=Coin.parse)
    denom: str = attr.ib()
    voter: ValAddress = attr.ib()

    def to_data(self) -> dict:
        return {
            "exchange_rate": str(self.exchange_rate.amount),
            "denom": self.denom,
            "voter": self.voter,
        }

    @classmethod
    def from_data(cls, data) -> ExchangeRateVote:
        xr = Coin(data["denom"], data["exchange_rate"])
        return cls(exchange_rate=xr, denom=xr.denom, voter=data["voter"])


@attr.s
class ExchangeRatePrevote:

    hash: str = attr.ib()
    denom: str = attr.ib()
    voter: ValAddress = attr.ib()
    submit_block: int = attr.ib(converter=int)

    def to_data(self) -> Dict[str, str]:
        return {
            "hash": self.hash,
            "denom": self.denom,
            "voter": self.voter,
            "submit_block": str(self.submit_block),
        }

    @classmethod
    def from_data(cls, data: Dict[str, str]) -> ExchangeRatePrevote:
        return cls(
            hash=data["hash"],
            denom=data["denom"],
            voter=data["voter"],
            submit_block=int(data["submit_block"]),
        )
