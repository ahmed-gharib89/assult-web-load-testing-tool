import click
from .http import assault


@click.command()
@click.option("--requests", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrent requests")
@click.option("--json-file", "-j", default=None, help="Path to output json file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    """Prints the statistics for the given requests .

    Args:
        requests (int): Number of requests to make.
        concurrency (int): Number of concurrent requests.
        json_file (stirng): String path to output json file.
        url (stirng): String url to make requests to.
    """
    print(f"Requests: {requests}")
    print(f"Concurrency: {concurrency}")
    print(f"JSON File: {json_file}")
    print(f"URL: {url}")
    assault(url, requests, concurrency)


if __name__ == "__main__":
    cli()
