# 🐍 Python Developer Challenge – Aptoide Scraper API

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

```json
{
  "name": "Facebook",
  "size": 73126576,
  "downloads": 2000000000,
  "version": "543.0.0.56.73",
  "release_date": "2025-12-27 18:47:38",
  "min_screen": "SMALL",
  "supported_cpus": ["arm64-v8a"],
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

- Python 3.13 (with docker)
  - FastAPI (with pydantic)
  - uvicorn
  - pytest
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

## List of some packages

- com.facebook.katana
- com.whatsapp
- com.google.android.youtube
- com.duolingo
- net.daum.android.map
- codematics.universal.tv.remote.control
- com.azure.authenticator
- com.google.android.apps.wallpaper

## Logging

We log the result of the API fetched, as a error or info, deppending of the API status code. This is only appears in the terminal, is not appended to file or saved into a DB.

## Tests

The method scrape_metadata was tested 5 times with the strs:

- com.facebook.katana
- com.duolingo
- codematics.universal.tv.remote.control
- com.google.android.youtube
- gugugaga

This is tested with pytest. Each method (expect for method that tests package name guguga) tests both the metadata result and the message result with what is expected to return.

To run the tests we simply restart the docker compose. The tests run when we (re)start it.

## Swagger and Code Documentation

Swagger is supoorted by default by FastAPI.

```
http://localhost:8000/docs
```

Three schemas were implemented for this

- SuccessResponse
- ErrorResponse
- AppMetadatada

AppMetadatada is all the values that are important from the package data obtained. This is passed inside the SuccessResponse.

Each function also has docstrings to describe the parameters and expected results from the computation.

Variables are written with type hinting, usefull with pydantic (that comes with FastAPI).

## Thinking and Decisions of implementation

- The structure of the code follows a main.py file in root. The route is in the routes/api/ folder. There is also /tests folder for testing, a /utils folder for util functions and a /services folder for helper functions.
- The only endpoint allows to fetch the Aptoide API to get all relevent metadata from the package with the given name.
- If no parameter is provided, is None or empty, accepts com.facebook.katana as default parameter
- FastAPI was chosen because of the built-in swagger and also because it provides better run time than Django for instance.
- No API token authentication was implemented, I believed it wasn't necessary for this assignement.
- The testing is done by running docker compose. One of the images run the tests, whenever we run the command to start.
- There seems two be two endpoints (one is cache based, the other isn't). For this assignement the one used was the one that isn't (less optimal, but avoid cache misses???)

The base URLs are

```
GET https://ws75.aptoide.com/api/7/
GET https://ws2-cache.aptoide.com/api/7/
```
