import click
import json
import sys
from typing import TextIO

from .http import assault
from .stats import Results


@click.command()
@click.option("--requests", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrent requests")
@click.option("--json-file", "-j", default=None, help="Path to output json file")
@click.argument("url")
def cli(requests: int, concurrency: int, json_file: str, url: str):
    """Prints the statistics for the given requests .

    Args:
        requests (int): Number of requests to make.
        concurrency (int): Number of concurrent requests.
        json_file (stirng): String path to output json file.
        url (stirng): String url to make requests to.
    """
    output_file = None
    if json_file:
        try:
            output_file = open(json_file, "w", encoding="utf-8")
        except IOError as e:
            print(f"Could not open {json_file} for writing: {e}")
            sys.exit(1)

    total_time, request_dicts = assault(url, requests, concurrency)
    results = Results(total_time, request_dicts)
    display(results, output_file)


def display(results: Results, json_file: TextIO):
    """Displays the results of the requests.

    Args:
        results (Results): Results object.
        json_file (string): String path to output json file.
    """
    if json_file:
        print(f"Writing to {json_file}")
        json.dump(results.to_dict(), json_file, indent=2)
    else:
        print("...Done!")
        print("--- Results ---")
        print(f"Successful requests: {results.successfull_requests(): <10}")
        print(f"Slowest requests:    {results.slowest(): <10.3f}")
        print(f"Fastest requests:    {results.fastest(): <10.3f}")
        print(f"Average time:        {results.average_time(): <10.3f}")
        print(f"Total time:          {results.total_time: <10.3f}")
        print(f"Request per minute:  {results.requests_per_minute(): <10}")
        print(f"Request per second:  {results.requests_per_second(): <10}")
