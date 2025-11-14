from services.models import Proxy


def load_proxies() -> list[str]:
    with open("proxies.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def parse_proxies(proxies: list[str]) -> list[Proxy]:
    parsed_proxies: list[Proxy] = []
    for proxy in proxies:
        host, port, user, pswd = proxy.split(":")
        parsed_proxies.append(
            Proxy(server=f"http://{host}:{port}", username=user, password=pswd)
        )
    return parsed_proxies
