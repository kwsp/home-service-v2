# Home Service

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.com/NieTiger/home-service-v2.svg?branch=master)](https://travis-ci.com/NieTiger/home-service-v2)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c87f3ff20eec8984e620/test_coverage)](https://codeclimate.com/github/tiega/home-service-v2/test_coverage)

Home service is a simple IoT server that serves REST endpoints for
IoT devices to post sensor data, and a simple web interface for monitoring.

Invoking the command `home-service` will start the server. This is preferably
wrapped in a systemd service and ran as a daemon. Containerised deployment options
are being worked on.


### Installation

Using pip:

```bash
python3 -m pip install home-service
```

### Usage

```bash
Usage: home-service [options]
```

### Options

```bash
Options:
    --version, -v      Get version info and exit
    --help, -h         Print this message and exit

    --port, -p         TCP port to run the server, defaults to port 6613
```
