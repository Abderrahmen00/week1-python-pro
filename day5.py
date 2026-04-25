import asyncio
from dataclasses import dataclass
from time import perf_counter

import httpx

URL = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"


@dataclass
class Position:
    city: str
    lat: float
    lon: float


cities = [
    Position("Tunis", 36.81, 10.18),
    Position("Sousse", 35.8254, 10.6370),
    Position("Sfax", 34.74, 10.76),
    Position("Monastir", 35.76, 10.81),
    Position("Kairouan", 35.67, 10.1),
]


async def get_weather_async(
    pos: Position, client: httpx.AsyncClient
) -> dict[str, object]:
    response = await client.get(URL.format(lat=pos.lat, lon=pos.lon))
    return dict(response.json())


def get_weather_sync(pos: Position, client: httpx.Client) -> dict[str, object]:
    response = client.get(URL.format(lat=pos.lat, lon=pos.lon))
    return dict(response.json())


def print_weather(city: str, w: dict[str, object]) -> None:
    cw = w["current_weather"]
    units = w["current_weather_units"]
    assert isinstance(cw, dict) and isinstance(units, dict)
    print(f"{city}: {cw['temperature']}{units['temperature']}")


async def run_async() -> float:
    start = perf_counter()
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(*[get_weather_async(c, client) for c in cities])
        for city, w in zip(cities, results):
            print_weather(city.city, w)
    elapsed = perf_counter() - start
    print(f"Async took: {elapsed:.2f}s\n")
    return elapsed


def run_sync() -> float:
    start = perf_counter()
    with httpx.Client() as client:
        results = [get_weather_sync(c, client) for c in cities]
        for city, w in zip(cities, results):
            print_weather(city.city, w)
    elapsed = perf_counter() - start
    print(f"Sync took: {elapsed:.2f}s\n")
    return elapsed


async def main() -> None:

    print("--- Async ---")
    async_time = await run_async()

    print("--- Sync ---")
    sync_time = run_sync()

    print(f"Speedup: {sync_time / async_time:.1f}x")


if __name__ == "__main__":
    asyncio.run(main())
