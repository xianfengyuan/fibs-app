The following API calls are defined in the Fibonacci REST API service:

- GET /ping
- GET /fibs/<int:seq_no>

To run the tests, follow the steps below:

- setup virtual python env (python3 -mvenv .venv)
- go into venv (source .venv/bin/activate)
- setup running python env (pip install -r requirements.txt; pip install -r requirements-dev.txt)
- run the test suites (pytest tests/)
- exit from virtual python env (deactivate)

