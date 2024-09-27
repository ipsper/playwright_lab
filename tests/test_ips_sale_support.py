"""tests for test_ips_test_api_log_handler"""
import time
from app import play_sup

def test_series_screenshot():
    """Test of get loggs api"""
    start_time = time.time()
    url = "http://127.0.0.1:4000"
    dicten = play_sup.play_sync_screenshot(url)
    print(f'test_simple dicten {dicten}')
    assert dicten['retur'] is True
    end_time = time.time()
    runtime = end_time - start_time
    print(f"runtime for test_simple {runtime} seconds")

def test_parallel_screenshot():
    """Test of get loggs api"""
    start_time = time.time()
    url = "http://127.0.0.1:4000"
    dicten = play_sup.async_screenshot(url)

    ipa = "127.0.0.1"
    dicten = log_gen.simple(ipa)
    print(f'test_simple dicten {dicten}')
    assert dicten['retur'] is True
    end_time = time.time()
    runtime = end_time - start_time
    print(f"runtime for test_simple {runtime} seconds")
