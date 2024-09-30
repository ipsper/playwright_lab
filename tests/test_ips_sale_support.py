"""tests for test_ips_test_api_log_handler"""
import time
from app import play_sup

def test_series_title_in_index():
    """Test that title is 'Salesupport · Phoenix Framework' in all browsers"""
    start_time = time.time()
    browsers = ['chromium', 'firefox', 'webkit']
    len_browsers = len(browsers)
    url = "http://127.0.0.1:4000"
    title = 'Salesupport · Phoenix Framework'
    list = play_sup.play_sync_index_title(url, browsers)
    print(f'test_simple list {list}')
    assert play_sup.all_elements_is_same(title ,list, len_browsers) is True
    end_time = time.time()
    runtime = end_time - start_time
    print(f"runtime for test_series_title_in_index {runtime} seconds")

def test_parallel_title_in_index():
    """Test that title is 'Salesupport · Phoenix Framework' in all browsers"""
    start_time = time.time()
    browsers = ['chromium', 'firefox', 'webkit']
    len_browsers = len(browsers)
    url = "http://127.0.0.1:4000"
    title = 'Salesupport · Phoenix Framework'
    list = play_sup.play_async_index_title(url, browsers)
    print(f'test_simple list {list}')
    assert play_sup.all_elements_is_same(title ,list, len_browsers) is True
    end_time = time.time()
    runtime = end_time - start_time
    print(f"runtime for test_parallel_title_in_index {runtime} seconds")


def test_series_screenshot():
    """Test of get loggs api"""
    start_time = time.time()
    browsers = ['chromium', 'firefox', 'webkit']
    url = "http://127.0.0.1:4000"
    dicten = play_sup.play_sync_screenshot(url, browsers)
    print(f'test_simple dicten {dicten}')
    assert dicten['retur'] is True
    end_time = time.time()
    runtime = end_time - start_time
    print(f"runtime for test_simple {runtime} seconds")

def test_parallel_screenshot():
    """Test of get loggs api"""
    start_time = time.time()
    url = "http://127.0.0.1:4000"
    browsers = ['chromium', 'firefox', 'webkit']
    dicten = play_sup.play_async_screenshot(url, browsers)

    ipa = "127.0.0.1"
    dicten = log_gen.simple(ipa)
    print(f'test_simple dicten {dicten}')
    assert dicten['retur'] is True
    end_time = time.time()
    runtime = end_time - start_time
    print(f"runtime for test_simple {runtime} seconds")
