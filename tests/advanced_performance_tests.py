import requests
import time
import threading
import numpy as np
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def single_request(url, session, payload=None, headers=None, network_latency_ms=0):
    """
    Makes a single request, simulates network latency, and returns performance metrics.
    """
    # Simulate network latency before sending the request
    if network_latency_ms > 0:
        time.sleep(network_latency_ms / 1000.0)

    start_time = time.time()
    try:
        with session.get(url, params=payload, headers=headers, timeout=20) as response:
            latency = time.time() - start_time
            return latency, response.status_code, len(response.content)
    except requests.exceptions.RequestException:
        return time.time() - start_time, 500, 0

def run_test_scenario(url, num_requests, concurrency, payload=None, headers=None, network_latency_ms=0):
    """
    Runs a generic test scenario with detailed configuration.
    """
    latencies = []
    status_codes = []
    response_sizes = []
    start_wall_time = time.time()

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        with requests.Session() as session:
            futures = [executor.submit(single_request, url, session, payload, headers, network_latency_ms) for _ in range(num_requests)]
            
            for future in as_completed(futures):
                latency, status_code, response_size = future.result()
                latencies.append(latency)
                status_codes.append(status_code)
                response_sizes.append(response_size)
    
    end_wall_time = time.time()
    total_wall_time = end_wall_time - start_wall_time

    successful_requests = sum(1 for sc in status_codes if sc == 200)
    failed_requests = len(status_codes) - successful_requests
    error_rate = (failed_requests / num_requests) * 100 if num_requests > 0 else 0
    throughput = successful_requests / total_wall_time if total_wall_time > 0 else 0

    return {
        'concurrency': concurrency,
        'total_requests': num_requests,
        'successful_requests': successful_requests,
        'failed_requests': failed_requests,
        'error_rate_percent': error_rate,
        'avg_latency_s': np.mean(latencies) if latencies else 0,
        'median_latency_s': np.median(latencies) if latencies else 0,
        'p95_latency_s': np.percentile(latencies, 95) if latencies else 0,
        'p99_latency_s': np.percentile(latencies, 99) if latencies else 0,
        'throughput_rps': throughput,
        'total_time_s': total_wall_time,
        'avg_response_bytes': np.mean(response_sizes) if response_sizes else 0
    }

def spike_test(base_url, endpoint, base_concurrency, spike_concurrency, spike_duration_s, total_duration_s):
    """
    Simulates a sudden spike in traffic.
    """
    url = f"{base_url}/{endpoint}"
    results = []
    print(f"Starting Spike Test for endpoint: {endpoint}")
    start_time = time.time()
    while time.time() - start_time < total_duration_s:
        current_time = time.time() - start_time
        if current_time < spike_duration_s:
            concurrency = spike_concurrency
            phase = "Spike"
        else:
            concurrency = base_concurrency
            phase = "Baseline"
        
        print(f"  Running {phase} phase with concurrency: {concurrency}")
        result = run_test_scenario(url, num_requests=concurrency*2, concurrency=concurrency)
        result['phase'] = phase
        result['timestamp'] = current_time
        results.append(result)
        time.sleep(1) # Interval between measurements
    print("Spike Test finished.")
    return results

def soak_test(base_url, endpoint, concurrency, duration_minutes):
    """
    Tests server stability under a sustained load for a long duration.
    """
    url = f"{base_url}/{endpoint}"
    results = []
    print(f"Starting Soak Test for endpoint: {endpoint} for {duration_minutes} minutes.")
    start_time = time.time()
    end_time = start_time + duration_minutes * 60
    
    while time.time() < end_time:
        print(f"  Soak test running... {int(end_time - time.time())}s remaining.")
        result = run_test_scenario(url, num_requests=concurrency*5, concurrency=concurrency)
        result['elapsed_time_s'] = time.time() - start_time
        results.append(result)
        time.sleep(5) # Interval between measurements
    print("Soak Test finished.")
    return results

def payload_variation_test(base_url, endpoint, concurrency, payload_sizes_kb):
    """
    Tests how different request payload sizes affect performance.
    (Simulated via query parameters for a GET request).
    """
    url = f"{base_url}/{endpoint}"
    results = []
    print(f"Starting Payload Variation Test for endpoint: {endpoint}")
    for size_kb in payload_sizes_kb:
        print(f"  Testing with payload size: {size_kb} KB")
        payload = {'data': 'a' * size_kb * 1024} # Create a payload of the desired size
        result = run_test_scenario(url, num_requests=100, concurrency=concurrency, payload=payload)
        result['payload_size_kb'] = size_kb
        results.append(result)
    print("Payload Variation Test finished.")
    return results

def mixed_workload_test(base_url, endpoints, concurrency, duration_minutes):
    """
    Simulates a realistic workload by hitting multiple endpoints concurrently.
    """
    results = []
    print(f"Starting Mixed Workload Test for {duration_minutes} minutes.")
    start_time = time.time()
    end_time = start_time + duration_minutes * 60

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        with requests.Session() as session:
            while time.time() < end_time:
                print(f"  Mixed workload running... {int(end_time - time.time())}s remaining.")
                # Create a mix of requests to random endpoints
                futures = [executor.submit(single_request, f"{base_url}/{random.choice(endpoints)}", session) for _ in range(concurrency)]
                
                for future in as_completed(futures):
                    latency, status_code, _ = future.result()
                    results.append({
                        'latency_s': latency,
                        'status_code': status_code,
                        'timestamp': time.time() - start_time
                    })
                time.sleep(1)
    print("Mixed Workload Test finished.")
    return results