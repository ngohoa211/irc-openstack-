# Copyright 2019 - Viettel
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


class KapacitorProperties(object):
    ID = 'id'
    RESOURCE_TYPE = 'resource_type'
    RESOURCE_NAME = 'resource_name'
    DETAILS = 'details'
    STATUS = 'status'
    HOST = 'host'
    PRIORITY = 'priority'
    TIMESTAMP = 'timestamp'
    KAPACITOR_TIMESTAMP_FORMAT = '%Y.%m.%d %H:%M:%S'
    MESSAGE = 'message'
    KAPACITOR_RESOURCE_NAME = 'kapacitor_resource_name'


class KapacitorState(object):
    OK = 'ok'
    INFO = 'info'
    WARNING = 'warning'
    CRITICAL = 'critical'