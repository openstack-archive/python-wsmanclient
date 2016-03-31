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


class BaseClientException(Exception):

    msg_fmt = 'An unknown exception occurred'

    def __init__(self, message=None, **kwargs):
        message = self.msg_fmt % kwargs
        super(BaseClientException, self).__init__(message)


class RequestFailure(BaseClientException):
    msg_fmt = ('WSMan request failed')


class InvalidResponse(BaseClientException):
    msg_fmt = ('Invalid response received. Status code: "%(status_code)s", '
               'reason: "%(reason)s"')


class InvalidFilterDialect(BaseClientException):
    msg_fmt = ('Invalid filter dialect "%(invalid_filter)s". '
               'Supported options are %(supported)s')
