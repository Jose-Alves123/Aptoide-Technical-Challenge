# 🐍 Python Developer Challenge – Aptoide Scraper API

Welcome to the coding challenge! 🚀
Your task is to build a Python-based API that scrapes package data from the Aptoide app store (https://en.aptoide.com/) and exposes it through a REST endpoint.

This project has one unique endpoint

```
GET /aptoide?package_name=<package_id>
```

This endpoint

- accepts a package name as a query, if none is provided accepts com.facebook.katana
- scrapes the Aptoide API to obtain all the valuable data
- returns this metadata in json format

## 🧾 Example

Request:

```
GET /aptoide?package_name=com.facebook.katana
```

Response (JSON):

```
{
  "name": "Facebook",
  "size": "152.5 MB",
  "downloads": "2B",
  "version": "532.0.0.55.71",
  "release_date": "2025-09-30 17:06:59",
  "min_screen": "SMALL",
  "supported_cpu": "arm64-v8a",
  "package_id": "com.facebook.katana",
  "sha1_signature": "8A:3C:4B:26:2D:72:1A:CD:49:A4:BF:97:D5:21:31:99:C8:6F:A2:B9",
  "developer_cn": "Facebook Corporation",
  "organization": "Facebook Mobile",
  "local": "Palo Alto",
  "country": "US",
  "state_city": "CA"
}
```

## Tech stack and Dependencies

- Python 3.13+
  - FastAPI (with pydantic)
  - uvicorn
- Docker (Dockerfile and compose)

## How to run

All dependencies are listed in the requirements.txt file. To run with docker, simply use the command:

```zsh
docker compose up
```

You can access the only API endpoint in the browser with the url provided below. Make sure you don't have anything else running in port 8000.

```
http://127.0.0.1:8000/aptoide/
```

## Tests

TODO

## 🎯 Evaluation Criteria

- The structure of the code follows a main.py file in root. The route is described in the routes/api/ folder. There is also /tests folder for testing, a /utils folder for util functions and a /services folder for helper functions.
- The only endpoint allows to fetch the Aptoide API to get all relevent metadata.
- If no parameter is provided, is None or empty, accepts com.facebook.katana as default parameter
- FastAPI was chosen because of the built-in swagger and also because it provides better run time than Django for instance.
- No API token authentication was design, i believed it wasn't necessary for this test.
- The testing is done by running docker compose. One of the images run the tests, whenever we run the command to start the webapp.
