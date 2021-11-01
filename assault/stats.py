from typing import List, Dict
from statistics import mean


class Results:
    """
    Results handles calculating statistics based on a list of requests that were made.
    Here's an example of what the information will look like:

    $ assault https://example.com
    .... Done!
    --- Results ---
    Successful requests 500
    Slowest 0.010s
    Fastest 0.001s
    Average 0.003s
    Total time 0.620s
    Requests Per Minute 48360
    Requests Per Second 806
    """

    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = sorted(requests, key=lambda r: r["request_time"])

    def slowest(self) -> float:
        """
        Returns the slowest request's completion time

        >>> results = Results(
        ...    10.6,
        ...    [
        ...        {"status_code": 200, "request_time": 3.4},
        ...        {"status_code": 500, "request_time": 6.1},
        ...        {"status_code": 200, "request_time": 1.04},
        ...    ],
        ... )
        >>> results.slowest()
        6.1
        """
        return self.requests[-1]["request_time"]

    def fastest(self) -> float:
        """
        Returns the fastest request's completion time

        >>> results = Results(
        ...     10.6,
        ...     [
        ...         {"status_code": 200, "request_time": 3.4},
        ...         {"status_code": 500, "request_time": 6.1},
        ...         {"status_code": 200, "request_time": 1.04},
        ...     ],
        ... )
        >>> results.fastest()
        1.04
        """
        return self.requests[0]["request_time"]

    def average_time(self) -> float:
        """
        Returns the average time request completion time

        >>> results = Results(
        ...     10.6,
        ...     [
        ...         {"status_code": 200, "request_time": 3.4},
        ...         {"status_code": 500, "request_time": 6.1},
        ...         {"status_code": 200, "request_time": 1.04},
        ...     ],
        ... )
        >>> results.average_time()
        3.513333333333333
        """
        return mean([r["request_time"] for r in self.requests])

    def successfull_requests(self) -> int:
        """
        Returns the number of successfull requests

        >>> results = Results(
        ...     10.6,
        ...     [
        ...         {"status_code": 200, "request_time": 3.4},
        ...         {"status_code": 500, "request_time": 6.1},
        ...         {"status_code": 200, "request_time": 1.04},
        ...     ],
        ... )
        >>> results.successfull_requests()
        2
        """
        return sum(1 for r in self.requests if r["status_code"] in range(200, 300))

    def requests_per_minute(self) -> int:
        """
        Returns the number of requests per minute

        >>> results = Results(
        ...     10.6,
        ...     [
        ...         {"status_code": 200, "request_time": 3.4},
        ...         {"status_code": 500, "request_time": 6.1},
        ...         {"status_code": 200, "request_time": 1.04},
        ...     ],
        ... )
        >>> results.requests_per_minute()
        17
        """
        return round(60 / self.total_time * len(self.requests))

    def requests_per_second(self) -> int:
        """
        Returns the number of requests per minute

        >>> results = Results(
        ...     1.54,
        ...     [
        ...         {"status_code": 200, "request_time": 0.4},
        ...         {"status_code": 500, "request_time": 0.1},
        ...         {"status_code": 200, "request_time": 1.04},
        ...     ],
        ... )
        >>> results.requests_per_second()
        2
        """
        return round(len(self.requests) / self.total_time)

    def to_dict(self) -> Dict:
        """
        Returns a dictionary representation of the results

        >>> results = Results(
        ...     10.6,
        ...     [
        ...         {"status_code": 200, "request_time": 3.4},
        ...         {"status_code": 500, "request_time": 6.1},
        ...         {"status_code": 200, "request_time": 1.04},
        ...     ],
        ... )
        >>> results.to_dict()
        {'total_time': 10.6, 'slowest': 6.1, 'fastest': 1.04, 'average_time': 3.513333333333333, 'successfull_requests': 2, 'requests_per_minute': 17, 'requests_per_second': 0}
        """
        return {
            "total_time": self.total_time,
            "slowest": self.slowest(),
            "fastest": self.fastest(),
            "average_time": self.average_time(),
            "successfull_requests": self.successfull_requests(),
            "requests_per_minute": self.requests_per_minute(),
            "requests_per_second": self.requests_per_second(),
        }
