from fastapi.testclient import TestClient
from services.scraper_service import scrape_metadata
from main import app


client = TestClient(app)


def test_scrape_facebook():
    res : dict = scrape_metadata("com.facebook.katana")
    expected_metadata : dict = {
      "name": "Facebook",
      "size": 73126576,
      "downloads": 2000000000,
      "version": "543.0.0.56.73",
      "release_date": "2025-12-27 18:47:38",
      "min_screen": "SMALL",
      "supported_cpus": [
        "arm64-v8a"
      ],
      "package_id": "com.facebook.katana",
      "sha1_signature": "8A:3C:4B:26:2D:72:1A:CD:49:A4:BF:97:D5:21:31:99:C8:6F:A2:B9",
      "developer_cn": "Facebook Corporation",
      "organization": "Facebook Mobile",
      "local": "Palo Alto",
      "country": "US",
      "state_city": "CA"
    }
    expected_message : str = "Data retrieved with success"

    assert res["metadata"] == expected_metadata
    assert res["message"] == expected_message

def test_scrape_duolingo():
    res : dict = scrape_metadata("com.duolingo")
    expected_metadata : dict= {
      "name": "Duolingo - Learn Languages Free",
      "size": 37870664,
      "downloads": 500000000,
      "version": "3.106.5",
      "release_date": "2020-03-12 18:59:05",
      "min_screen": "SMALL",
      "supported_cpus": [
        "armeabi-v7a"
      ],
      "package_id": "com.duolingo",
      "sha1_signature": "A0:0B:B7:D9:2E:38:90:9C:2F:6C:04:A8:05:58:89:0E:52:94:9C:D9",
      "developer_cn": "Vicki Cheung",
      "organization": "Duolingo",
      "local": None,
      "country": None,
      "state_city": None
    }
    expected_message : str = "Data retrieved with success"

    assert res["metadata"] == expected_metadata
    assert res["message"] == expected_message

def test_scrape_youtube():
    res : dict = scrape_metadata("com.google.android.youtube")
    expected_metadata : dict = {
      "name": "YouTube",
      "size": 170753572,
      "downloads": 2000000000,
      "version": "20.51.39",
      "release_date": "2025-12-25 04:41:30",
      "min_screen": "SMALL",
      "supported_cpus": [
        "x86",
        "x86-64",
        "armeabi-v7a",
        "arm64-v8a"
      ],
      "package_id": "com.google.android.youtube",
      "sha1_signature": "F8:45:6B:1D:99:86:AC:F9:CE:21:FB:45:0B:0D:32:B8:95:F3:68:85",
      "developer_cn": "Android",
      "organization": "Google Inc.",
      "local": "Mountain View",
      "country": "US",
      "state_city": "California"
    }
    expected_message : str = "Data retrieved with success"

    assert res["metadata"] == expected_metadata
    assert res["message"] == expected_message

def test_scrape_remote_controller():
    res : dict = scrape_metadata("codematics.universal.tv.remote.control")
    expected_metadata : dict = {
      "name": "Universal TV Remote Control",
      "size": 9199046,
      "downloads": 100000000,
      "version": "2.5.8",
      "release_date": "2024-01-30 15:36:18",
      "min_screen": "SMALL",
      "supported_cpus": [],
      "package_id": "codematics.universal.tv.remote.control",
      "sha1_signature": "9F:E4:F7:36:B8:95:3B:03:45:09:42:D6:67:5B:DA:71:91:02:C5:0C",
      "developer_cn": "CodeMatics",
      "organization": None,
      "local": None,
      "country": None,
      "state_city": None
    }
    expected_message : str = "Data retrieved with success"

    assert res["metadata"] == expected_metadata
    assert res["message"] == expected_message

def test_scrape_gugugaga():
    res : dict = scrape_metadata("gugugaga")
    expected_message : str = "Application 'package:gugugaga' not found"

    assert res["message"] == expected_message

