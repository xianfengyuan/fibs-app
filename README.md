The following API calls are defined in the Fibonacci REST API service:

- GET /ping
- GET /fibs/<int:seq_no>

Example responses:

- <SERVER_ADDRESS>/ping => {"message":"pong"}
- <SERVER_ADDRESS>/fibs/2 => 1
- <SERVER_ADDRESS>/fibs/10 => 55

To run the tests, follow the steps below:

- setup virtual python env (python3 -mvenv .venv)
- go into venv (source .venv/bin/activate)
- setup running python env (pip install -r requirements.txt; pip install -r requirements-dev.txt)
- run the test suites (pytest tests/)
- exit from virtual python env (deactivate)

A docker-compose.yaml file is also provided to run the app with docker-compose, which can include
 multiple interactive containers.

A docker-compose.debug.yaml file is used to help debugging the Flask app in Visual Studio Code IDE.
