from fastapi import Request



users = [('nick', ''), ('jonas','')]
admins = [("admin", r"!t6S%cB2nyTY8nmd0w4t!v0fxLvKMPYFKR3LJf9kFMMC34h*Ch")]


async def is_authenticated(request: Request, session_info) -> bool:
    return session_info.get(request.session.get('id'), {}).get('authenticated', False)


