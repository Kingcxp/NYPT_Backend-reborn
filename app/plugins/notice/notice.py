import os
import aiofiles

from fastapi import status
from fastapi.responses import PlainTextResponse

from . import router


@router.get("/total")
async def notice_total() -> PlainTextResponse:
    """
    获取公告总数
    """
    tot: int = 0
    for i in range(1, 100):
        if not os.path.exists(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                f"notices/notice{i}.html"
            )
        ):
            break
        tot += 1
    return PlainTextResponse(str(tot), status_code=status.HTTP_200_OK)


@router.get("/{page}")
async def notice(page: int) -> PlainTextResponse:
    """
    获取指定编号的公告

    Args:
        page (int): 公告编号
    """
    page_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        f"notices/notice{page}.html"
    )
    if not os.path.exists(page_path):
        return PlainTextResponse(
            "",
            status_code=status.HTTP_404_NOT_FOUND
        )
    async with aiofiles.open(page_path, "r", encoding="utf-8") as f:
        content = await f.read()
    return PlainTextResponse(content, status_code=status.HTTP_200_OK)
