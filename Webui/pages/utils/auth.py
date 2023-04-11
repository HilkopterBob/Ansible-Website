from fastapi import Request



users = [('nick', ''), ('jonas',''), ('sebastian','')]
admins = [('admin', '')]


async def is_authenticated(request: Request, session_info) -> bool:
    return session_info.get(request.session.get('id'), {}).get('authenticated', False)

async def is_admin(request: Request, session_info) -> bool:
    return session_info.get(request.session.get('id'), {}).get('admin', False)
