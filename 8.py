import argparse
import json
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[str]
    state: str
    street: Optional[str]

    def __str__(self) -> str:
        address = ", ".join(
            part
            for part in [self.address_1, self.city, self.state_province, self.postal_code, self.country]
            if part
        )
        return f"{self.name} ({self.brewery_type}) - {address}"


def pobierz_browary(city: Optional[str] = None, liczba: int = 20) -> list[Brewery]:
    params = {"page": 1, "per_page": liczba}
    if city:
        params["by_city"] = city

    url = f"https://api.openbrewerydb.org/v1/breweries?{urlencode(params)}"
    request = Request(url, headers={"User-Agent": "python-brewery-client/1.0"})

    with urlopen(request, timeout=10) as response:
        dane = json.load(response)

    return [Brewery(**browar) for browar in dane[:liczba]]


def main() -> None:
    parser = argparse.ArgumentParser(description="Pobiera browary z Open Brewery DB.")
    parser.add_argument("--city")
    args = parser.parse_args()

    browary = pobierz_browary(city=args.city)
    for browar in browary:
        print(browar)


if __name__ == "__main__":
    main()
