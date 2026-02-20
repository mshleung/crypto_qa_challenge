import requests
import random

def test_high_greater_than_low():
    # Generate random value in the format 0.xxxxxxxxxxxxxxxxxx (17 digits)
    rand_val = f"0.{random.randint(10**16, 10**17-1)}"
    url = (
        f"https://www.szse.cn/api/market/ssjjhq/getTimeData?"
        f"random={rand_val}&marketId=1&code=000001&language=EN"
    )
    resp = requests.get(url)
    print("Request URL:", url)
    print("HTTP status", resp.status_code)
    assert resp.ok, f"Request failed: {resp.text}"
    data = resp.json()
    #print("Raw response data:", data)
    high = data.get("data", {}).get("high")
    low = data.get("data", {}).get("low")
    print("High:", high, "Low:", low)
    assert high is not None and low is not None, "Could not find high/low in response"
    assert float(high) > float(low), f"High ({high}) is not greater than Low ({low})"
    print("Verification passed: High > Low")
