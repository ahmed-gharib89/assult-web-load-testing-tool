from typing import List, Dict


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
        self.requests = requests

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
        pass

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
        pass

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
        9.8466666667
        """
        pass

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
        pass