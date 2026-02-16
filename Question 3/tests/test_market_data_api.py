import requests
import random
import pytest

def test_high_greater_than_low():
    # Generate random value in the format 0.xxxxxxxxxxxxxxxxxx (17 digits)
    rand_val = f"0.{random.randint(10**16, 10**17-1)}"
    url = (
        f"https://www.szse.cn/api/market/ssjjhq/getTimeData?"
        f"random={rand_val}&marketId=1&code=000001&language=EN"
    )
    print("Request URL:", url)
    try:
        resp = requests.get(url, timeout=10)
        print("HTTP status", resp.status_code)
    except requests.RequestException as e:
        pytest.fail(f"Request failed: {e}")
        return
    if not resp.ok:
        print("Request failed, body:\n", resp.text)
        pytest.fail(f"HTTP error: {resp.status_code}")
        return
    try:
        data = resp.json()
    except Exception as e:
        print("Failed to parse JSON:", e)
        print("Raw response:", resp.text)
        pytest.fail("Response is not valid JSON")
        return
    print("Raw response data:", data)
    # Defensive extraction
    high = None
    low = None
    if isinstance(data, dict):
        d = data.get("data")
        if isinstance(d, dict):
            high = d.get("high")
            low = d.get("low")
    print("High:", high, "Low:", low)
    if high is None or low is None:
        pytest.fail("Could not find high/low in response")
        return
    try:
        high_f = float(high)
        low_f = float(low)
    except Exception as e:
        print(f"Could not convert high/low to float: {e}")
        pytest.fail("High/low values are not numeric")
        return
    assert high_f > low_f, f"High ({high}) is not greater than Low ({low})"
    print("Verification passed: High > Low")
