#!/usr/bin/env python3

from __future__ import print_function
import assisted_swarm_client.assisted_swarm as assisted_swarm


def new_swarm_client():
    configuration = assisted_swarm.Configuration()
    configuration.host = 'http://127.0.0.1:5566/api/assisted-swarm'
    return assisted_swarm.SwarmApi(assisted_swarm.ApiClient(configuration))
