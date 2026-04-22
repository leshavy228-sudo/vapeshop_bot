from aiogram.client.session.aiohttp import AiohttpSession

def create_telegram_aiohttp_session(proxy_url: str = None) -> AiohttpSession:
    # TUN сделает всё сам, прокси в коде больше не нужен
    return AiohttpSession()