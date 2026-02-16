"""
UI Automation tests using Appium.
"""

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
import time
import datetime
import re

class TestUIAutomation:
    """Minimal suite: launch app and press Agree."""

    def test_app_launch(self, driver_android):
        """Launch app and press the Agree button."""
        wait = WebDriverWait(driver_android, 20)
        agree_id = "hko.MyObservatory_v1_0:id/btn_agree"
        el = wait.until(EC.element_to_be_clickable((AppiumBy.ID, agree_id)))
        el.click()
        time.sleep(1)
        el.click()
        time.sleep(1)
        print("Clicked Agree")

        # After Agree, click the system/dialog positive button if present
        try:
            ok_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1")))
            ok_btn.click()
        except Exception:
            pass

        time.sleep(1)
        # Click the app's exit button up to twice. Some versions display two
        # buttons simultaneously, others replace the element on first click.
        # Use an explicit wait each time so we can log what happened.
        for attempt in range(2):
            try:
                exit_btn = wait.until(EC.element_to_be_clickable(
                    (AppiumBy.ID, "hko.MyObservatory_v1_0:id/exit_btn")
                ))
                print(f"exit_btn found on attempt {attempt}, clicking")
                exit_btn.click()
                time.sleep(2)
            except Exception as exc:
                # nothing more to do if the button isn't present/clickable
                print(f"exit_btn not clickable on attempt {attempt}: {exc}")
                break

        time.sleep(2)
        print("Finished exit_btn clicks")

        # Finally, click 'Do not show again' if present
        try:
            dna = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "hko.MyObservatory_v1_0:id/do_not_show_again_btn")))
            print("do_not_show_again button located, clicking")
            dna.click()
        except Exception as exc:
            print(f"do_not_show_again not clicked: {exc}")
        print("Finished do_not_show_again step")

    def test_open_forecast(self, driver_android):
        """Open the hamburger menu, expand first collapsed item, and select the forecast option."""
        wait = WebDriverWait(driver_android, 20)

        # 1) Click hamburger menu with retry for stale elements
        menu_xpath = '//android.widget.ImageButton[@content-desc="Open menu"]'
        for _ in range(3):
            try:
                el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, menu_xpath)))
                el.click()
                break
            except StaleElementReferenceException:
                time.sleep(0.3)
                continue
            except WebDriverException:
                time.sleep(0.3)
                continue
        time.sleep(0.5)

        # 2) Click the first collapsed arrow (with retry)
        arrow_xpath = '(//android.widget.ImageView[@content-desc="Collapsed"])[1]'
        for _ in range(3):
            try:
                el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, arrow_xpath)))
                el.click()
                break
            except StaleElementReferenceException:
                time.sleep(0.3)
                continue
            except WebDriverException:
                time.sleep(0.3)
                continue
        time.sleep(0.5)

        # 3) Click the specified recycler option
        option_xpath = '(//androidx.recyclerview.widget.RecyclerView[@resource-id="hko.MyObservatory_v1_0:id/recycler_view"])[2]/android.widget.FrameLayout[5]/android.widget.LinearLayout'
        for _ in range(3):
            try:
                el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, option_xpath)))
                el.click()
                break
            except StaleElementReferenceException:
                time.sleep(0.3)
                continue
            except WebDriverException:
                time.sleep(0.3)
                continue
        time.sleep(1)

        driver_android.save_screenshot('open_forecast.png')
        print('Opened forecast option')

    def test_verify_firstdate(self, driver_android):
        """Collect TextView content-desc dates and ensure the smallest date == today."""
        wait = WebDriverWait(driver_android, 5)
        today = datetime.date.today()

        # collect TextView elements that have a content-desc attribute
        elems = driver_android.find_elements(AppiumBy.XPATH, '//android.widget.TextView[@content-desc]')
        candidates = []
        pattern = re.compile(r'^(\d{1,2})\s+([A-Za-z]+)(?:\s+(\d{4}))?$', re.IGNORECASE)
        for el in elems:
            desc = el.get_attribute('content-desc') or el.get_attribute('text') or ''
            if not desc:
                continue
            m = pattern.match(desc.strip())
            if not m:
                continue
            day = int(m.group(1))
            month_name = m.group(2)
            year = int(m.group(3)) if m.group(3) else None
            # resolve month number
            try:
                month = datetime.datetime.strptime(month_name, '%B').month
            except ValueError:
                try:
                    month = datetime.datetime.strptime(month_name, '%b').month
                except Exception:
                    continue
            candidates.append((day, month, year, desc.strip()))

        print('Found candidate raw date strings:')
        for c in candidates:
            print('  ', c[3])

        assert candidates, 'No date-like content-desc TextView elements found'

        resolved = []
        for day, month, year, raw in candidates:
            y = year if year else today.year
            try:
                parsed = datetime.date(y, month, day)
            except Exception:
                continue
            # handle possible year rollover when year omitted
            if not year:
                if parsed < today and (month - today.month) % 12 > 6:
                    parsed = datetime.date(y + 1, month, day)
            resolved.append((parsed, raw))

        print('Resolved parsed dates:')
        for d, r in resolved:
            print('  ', d, '->', r)

        assert resolved, 'No resolvable dates from candidates'

        resolved.sort(key=lambda x: x[0])
        smallest, raw = resolved[0]
        print('Smallest parsed date:', smallest)
        print('Today is:', today)
        assert smallest == today, f'Smallest date {smallest} (raw: {raw}) does not match today {today}'
        driver_android.save_screenshot('first_date.png')
        print('Verified smallest forecast date:', smallest, 'raw:', raw)
    # test_verify_9_day_dates removed per request
