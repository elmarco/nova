# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2013 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
HTTP proxy that is compatible with OpenStack Nova SPICE.
"""

import os
import sys

from oslo.config import cfg

from nova import config
from nova.console import spicehttpproxy

opts = [
    cfg.StrOpt('spicehttpproxy_host',
               default='0.0.0.0',
               help='Host on which to listen for incoming requests'),
    cfg.IntOpt('spicehttpproxy_port',
               default=6083,
               help='Port on which to listen for incoming requests'),
    ]

CONF = cfg.CONF
CONF.register_cli_opts(opts)


def main():
    # Setup flags
    config.parse_args(sys.argv)

    # Create and start the NovaWebSockets proxy
    proxy = spicehttpproxy.HTTPProxy(
        (CONF.spicehttpproxy_host,
         CONF.spicehttpproxy_port))
    proxy.start_server()
