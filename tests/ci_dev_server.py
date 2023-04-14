#!/usr/bin/env python3
"""
Starts hyperglass with the Flask development server
"""
import os
import sys
import json
from logzero import logger

working_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(working_directory)


def construct_test(test_query, location, test_target):
    """Constructs JSON POST data for test_hyperglass function"""
    return json.dumps(
        {"type": test_query, "location": location, "target": test_target}
    )


def flask_dev_server(host, port):
    """Starts Flask development server for testing without WSGI/Reverse Proxy"""
    try:
        sys.path.insert(0, parent_directory)

        from hyperglass import render
        from hyperglass import hyperglass

        render.css()
        logger.info("Starting Flask development server")
        hyperglass.app.run(host=host, debug=True, port=port)
    except:
        logger.error("Exception occurred while trying to start test server...")
        raise


if __name__ == "__main__":
    flask_dev_server("localhost", 5000)
