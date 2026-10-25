"""
Controller for counter service routes.
"""
from flask import abort, jsonify, url_for
from service import app
from service.common import status

COUNTER = {}


@app.route("/health")
def health():
    """Return the service health status."""
    return jsonify(status="OK"), status.HTTP_200_OK


@app.route("/")
def index():
    """Return information about the service."""
    app.logger.info("Request for Base URL")
    return jsonify(
        status=status.HTTP_200_OK,
        message="Hit Counter Service",
        version="1.0.0",
        url=url_for("list_counters", _external=True),
    )


@app.route("/counters", methods=["GET"])
def list_counters():
    """List all counters."""
    app.logger.info("Request to list all counters")
    counters = [dict(name=name, counter=value) for name, value in COUNTER.items()]
    return jsonify(counters)


@app.route("/counters/<name>", methods=["POST"])
def create_counters(name):
    """Create a counter."""
    app.logger.info("Request to create counter: %s", name)
    if name in COUNTER:
        return abort(status.HTTP_409_CONFLICT, f"Counter {name} already exists")
    COUNTER[name] = 0
    location_url = url_for("read_counters", name=name, _external=True)
    return jsonify(name=name, counter=0), status.HTTP_201_CREATED, {"Location": location_url}


@app.route("/counters/<name>", methods=["GET"])
def read_counters(name):
    """Read a counter."""
    app.logger.info("Request to read counter: %s", name)
    if name not in COUNTER:
        return abort(status.HTTP_404_NOT_FOUND, f"Counter {name} does not exist")
    return jsonify(name=name, counter=COUNTER[name])


@app.route("/counters/<name>", methods=["PUT"])
def update_counters(name):
    """Increment a counter."""
    app.logger.info("Request to update counter: %s", name)
    if name not in COUNTER:
        return abort(status.HTTP_404_NOT_FOUND, f"Counter {name} does not exist")
    COUNTER[name] += 1
    return jsonify(name=name, counter=COUNTER[name])


@app.route("/counters/<name>", methods=["DELETE"])
def delete_counters(name):
    """Delete a counter if it exists."""
    app.logger.info("Request to delete counter: %s", name)
    COUNTER.pop(name, None)
    return "", status.HTTP_204_NO_CONTENT


def reset_counters():
    """Reset counters during tests."""
    global COUNTER  # pylint: disable=global-statement
    if app.testing:
        COUNTER = {}
