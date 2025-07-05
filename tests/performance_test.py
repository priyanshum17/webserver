
import requests
import time
import threading
import sys

URL = sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:8080'
NUM_REQUESTS = 10000
NUM_THREADS = 100

latencies = []

def make_request():
    start_time = time.time()
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            latencies.append(time.time() - start_time)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def main():
    threads = []
    start_time = time.time()

    for _ in range(NUM_REQUESTS):
        thread = threading.Thread(target=make_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Total requests: {len(latencies)}")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Throughput: {len(latencies) / total_time:.2f} requests/second")
    print(f"Average latency: {sum(latencies) / len(latencies):.4f} seconds")
    print(f"Median latency: {sorted(latencies)[len(latencies) // 2]:.4f} seconds")
    print(f"95th percentile latency: {sorted(latencies)[int(len(latencies) * 0.95)]:.4f} seconds")

if __name__ == '__main__':
    main()
