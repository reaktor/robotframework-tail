# rflogging

![Log example image](https://raw.githubusercontent.com/reaktor/rflogging/master/examplelog.png)

How to get this started:

Clone this repository with git.

RFLogging.py is the actual listener. It requires websocket-client ( https://github.com/websocket-client/websocket-client ). `pip install websocket-client`.

Log is shown by a web server. Web server uses node and yarn. So install node and yarn.

Node from https://nodejs.org/en/

Yarn from https://yarnpkg.com/en/docs/install

To get everything running:

First time run `yarn install`.

To get the server running `yarn start` on the project directory.

Open browser to http://localhost:3000 (this is the page where the log will be shown).

Run robot / pabot tests with option `--listener TailListener.py` and a log will be shown on runtime with swimlanes for parallel tests.
