import asyncio
import os
import time
import requests

# Make the request and return the results
def fetch(url):
    """Fetch a url and return the response

    Args:
        url (string): The url to fetch

    Returns:
        string: The status code and the request time
    """
    started_at = time.monotonic()
    response = requests.get(url)
    request_time = time.monotonic() - started_at
    return {"status_code": response.status_code, "request_time": request_time}


# A function to take unmade requests from a queue, perform the work,
# and add result to the queue
async def worker(name, queue, results):
    """A worker that fetches the results from the queue and returns a list of results .

    Args:
        name (string): The name of the worker
        queue (asyncio.Queue): A Queue of urls to fetch
        results (list): list of results
    """
    loop = asyncio.get_event_loop()
    while True:
        url = await queue.get()
        if os.getenv("DEBUG"):
            print(f"{name} - Fetching {url}")
        future_result = loop.run_in_executor(None, fetch, url)
        result = await future_result
        results.append(result)
        queue.task_done()


# Divide up work into batches and collect final results
async def distribute_work(url, requests, concurrency, results):
    """Distribute the number of requests to a queue .

    Args:
        url (string): The url to fetch
        requests (int): Number of requests to make
        concurrency (int): Number of concurrent requests
        results (list): list of results
    """
    queue = asyncio.Queue()

    # Add an item to the queue for each request we want to make
    for _ in range(requests):
        queue.put_nowait(url)

    # Create workers to match the concurrency
    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker-{i+1}", queue, results))
        tasks.append(task)

    started_at = time.monotonic()
    await queue.join()
    total_time = time.monotonic() - started_at

    for task in tasks:
        task.cancel()

    return total_time


# Entrypoint to making requests
def assault(url, requests, concurrency):
    """Run the attack on a given URL .

    Args:
        url (string): The url to fetch
        requests (int): Number of requests to make
        concurrency (int): Number of concurrent requests
    """
    results = []
    total_time = asyncio.run(distribute_work(url, requests, concurrency, results))
    return total_time, results
