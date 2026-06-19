import asyncio

from app.config.bot import bot, dp

from app.handlers.user.start import router as start_router
from app.handlers.user.profile import router as profile_router
from app.handlers.user.university import router as university_router
from app.handlers.user.university_info import (
    router as university_info_router
)
from app.handlers.user.umrah import (
    router as umrah_router
)
from app.handlers.user.visa import (
    router as visa_router
)
from app.handlers.user.ticket import (
    router as ticket_router
)
from app.handlers.user.hotel import (
    router as hotel_router
)
from app.handlers.user.operator import (
    router as operator_router
)
from app.handlers.user.transport import (
    router as transport_router
)
from app.handlers.user.subscription import (
    router as subscription_router
)

from app.handlers.admin.stats import (
    router as stats_router
)


async def main():
    dp.include_router(start_router)

    dp.include_router(subscription_router)

    dp.include_router(profile_router)

    dp.include_router(university_router)
    dp.include_router(university_info_router)

    dp.include_router(umrah_router)
    dp.include_router(visa_router)
    dp.include_router(ticket_router)
    dp.include_router(hotel_router)
    dp.include_router(transport_router)

    dp.include_router(operator_router)

    dp.include_router(stats_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())