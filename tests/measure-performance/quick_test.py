#!/usr/bin/env python3
"""
Quick Functionality Test Script

This script quickly verifies that the refactored API client works correctly
and that all service clients are properly sharing the HTTP client.
"""

import asyncio
import time
from crypticorn import ApiClient
from crypticorn.common import BaseUrl


async def quick_test():
    """Quick test to verify the refactored client works."""
    print("🚀 Quick functionality test for refactored API client")
    print("=" * 55)
    
    start_total = time.perf_counter()
    
    print("1️⃣  Creating ApiClient...")
    start = time.perf_counter()
    client = ApiClient(api_key="test-key", base_url=BaseUrl.PROD)
    creation_time = time.perf_counter() - start
    print(f"   ✅ Created in {creation_time:.4f}s")
    
    print("\n2️⃣  Testing service client access...")
    services = ["auth", "hive", "trade", "klines", "pay", "metrics"]
    
    for service_name in services:
        start = time.perf_counter()
        service_client = getattr(client, service_name)
        access_time = time.perf_counter() - start
        print(f"   ✅ {service_name:8} client: {access_time:.6f}s")
    
    # 3. Verify shared HTTP client
    print("\n3️⃣  Verifying shared HTTP client...")
    main_http = client._http_client
    print(f"   📍 Main HTTP client: {type(main_http).__name__}")
    print(f"   📍 Timeout: {main_http.timeout}")
    print(f"   📍 Connection limit: {main_http.connector.limit}")
    
    shared_count = 0
    for service_name in services:
        service_client = getattr(client, service_name)
        service_http = service_client.base_client.rest_client.pool_manager
        is_shared = service_http is main_http
        shared_count += is_shared
        status = "✅ SHARED" if is_shared else "❌ SEPARATE"
        print(f"   {service_name:8}: {status}")
    
    print("\n4️⃣  Testing configuration...")
    print(f"   📍 API Key: {'***' + client.api_key[-4:] if client.api_key else 'None'}")
    print(f"   📍 Base URL: {client.base_url}")
    print(f"   📍 HTTP Client Headers: {dict(main_http.headers)}")
    
    print("\n5️⃣  Cleaning up...")
    start = time.perf_counter()
    await client.close()
    cleanup_time = time.perf_counter() - start
    print(f"   ✅ Cleaned up in {cleanup_time:.4f}s")
    
    total_time = time.perf_counter() - start_total
    
    print("\n" + "=" * 55)
    print("📊 TEST SUMMARY")
    print("=" * 55)
    print(f"✅ Total test time: {total_time:.4f}s")
    print(f"✅ Client creation: {creation_time:.4f}s")
    print(f"✅ Shared HTTP clients: {shared_count}/{len(services)}")
    
    if shared_count == len(services):
        print("🏆 RESULT: All tests passed! Shared HTTP client working perfectly!")
    else:
        print("❌ RESULT: Some issues detected with HTTP client sharing")
    
    print("=" * 55)


if __name__ == "__main__":
    try:
        asyncio.run(quick_test())
    except KeyboardInterrupt:
        print("\n❌ Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
