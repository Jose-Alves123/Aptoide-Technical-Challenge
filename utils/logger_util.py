import logging

logger = logging.getLogger("uvicorn.error")


def log(message: str, package_name: str, status_code: int, success: bool = True) -> None:

    data : dict[str, str | int]= {
        "message" : message,
        "package_name" : package_name,
        "status_code" : status_code
    }

    logger.info(data) if success else logger.error(data)
