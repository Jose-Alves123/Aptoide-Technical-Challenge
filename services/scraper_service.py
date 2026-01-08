from utils import json_util, logger_util
import requests, logging

URL: str = "https://ws75.aptoide.com/api/7/app/getMeta"

def __dig(d, *keys, default=None):
    for k in keys:
        if not isinstance(d, dict):
            return default
        d = d.get(k)
    return d if d is not None else default


def scrape_metadata(package_name: str) -> dict:
    params : dict[str, str] = {"package_name": package_name}
    r = requests.get(URL, params=params, timeout=10)

    if r.status_code != 200:
        description : str = "An error occurred"

        try:
            description = r.json()['metadata']['errors'][0]['description']
        except:
            pass
        
        logger_util.log(description, package_name, r.status_code, False)
        return json_util.get_error(description)

    message: str = "Data retrieved with success"
    data : dict[str, str|int|bool|list] = r.json()["data"]

    owner = __dig(data, "file", "signature", "owner")
    parsed : dict[str, str] = (
        dict(
            part.strip().split("=", 1)
            for part in owner.split(",")
            if "=" in part
        ) if isinstance(owner, str) else {}
    )

    relevant_data = {
      "name": __dig(data, "name"),
      "size": __dig(data, "size"),
      "downloads": __dig(data, "stats", "downloads"),
      "version": __dig(data, "file", "vername"),
      "release_date": __dig(data, "modified"),
      "min_screen": __dig(data, "file", "hardware", "screen"),
      "supported_cpus": __dig(data, "file", "hardware", "cpus"),
      "package_id": __dig(data, "package"),
      "sha1_signature": __dig(data, "file", "signature", "sha1"),
      "developer_cn": parsed.get("CN", None),
      "organization": parsed.get("O", None),
      "local": parsed.get("L", None),
      "country": parsed.get("C", None),
      "state_city": parsed.get("ST", None)
    }
    
    logger_util.log(message, package_name, r.status_code, True)
    return json_util.get_success(message, relevant_data, "metadata")
