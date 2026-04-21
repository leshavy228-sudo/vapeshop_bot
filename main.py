import aiohttp
from aiohttp_socks import ProxyConnector
from aiogram.client.session.aiohttp import AiohttpSession
from typing import Optional

def create_telegram_aiohttp_session(proxy_url: Optional[str]) -> AiohttpSession:
    raw = (proxy_url or "").strip()
    aio_session = AiohttpSession()
    
    if not raw:
        return aio_session

    if raw.lower().startswith("socks5://"):
        connector = ProxyConnector.from_url(raw)
        client_session = aiohttp.ClientSession(connector=connector)
        aio_session._session = client_session 
        return aio_session

    aio_session.proxy = raw
    return aio_session