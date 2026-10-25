"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

# Import after Flask app creation to avoid circular initialization issues.
from service import routes  # noqa: E402,F401
from service.common import log_handlers  # noqa: E402

log_handlers.init_logging(app, "gunicorn.error")
app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
