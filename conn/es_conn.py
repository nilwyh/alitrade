# Copyright 2012-2013 eNovance <licensing@enovance.com>
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

import requests
import ujson as json
from common import log as LOG

class ESConnection(object):

    def __init__(self, index_prefix, doc_type):

        self.uri = 'http://localhost:9200/'
        if self.uri.strip()[-1] != '/':
            self.uri += '/'

        self.doc_type = doc_type
        self.index_prefix = index_prefix
        self.drop_data = False
        self.index = '_v1'
        self.id_field = 'id'

        self.search_path = '%s%s*/%s/_search' % (self.uri,
                                                 self.index_prefix,
                                                 self.doc_type)
        LOG.debug('ElasticSearch Connection initialized successfully!')

    def create(self, obj):
        LOG.debug('Prepare to create obj.')
        if self.drop_data:
            return
        else:
            # figure out id situation
            _id = ''
            if self.id_field:
                _id = obj.get(self.id_field)
                if not _id:
                    LOG.debug('Msg does not have required id field %s' %
                              self.id_field)
                    return 400
            # index may change over the time, it has to be called for each
            # request

            path = '%s%s%s/%s/%s/%s' % (self.uri, self.index_prefix,
                                     self.index, self.doc_type, _id, '_create')
            msg = json.dumps(obj)
            res = requests.post(path, data=msg)
            LOG.debug('Msg post target=%s' % path)
            LOG.debug('Msg posted with response code: %s' % res.status_code)
            return res.status_code

    # def get_messages(self, cond, q_string=""):
    #     LOG.debug('Prepare to get messages.')
    #     if cond:
    #         data = json.dumps(cond)
    #     else:
    #         data = {}
    #     return requests.post(self.search_path + "?" + q_string, data=data)
    #
    # def get_message_by_id(self, id):
    #     LOG.debug('Prepare to get messages by id.')
    #     path = self.search_path + '?q=_id:' + id
    #     LOG.debug('Search path:' + path)
    #     res = requests.get(path)
    #     LOG.debug('Msg get with response code: %s' % res.status_code)
    #     return res
    #
    # def post_messages(self, msg, id):
    #     LOG.debug('Prepare to post messages.')
    #     if self.drop_data:
    #         return 204
    #     else:
    #         index = self.index_strategy.get_index()
    #         path = '%s%s%s/%s/' % (self.uri, self.index_prefix,
    #                                index, self.doc_type)
    #
    #         res = requests.post(path + id, data=msg)
    #         LOG.debug('Msg post with response code: %s' % res.status_code)
    #         return res.status_code
    #
    # def put_messages(self, msg, id):
    #     LOG.debug('Prepare to put messages.')
    #     if self.drop_data:
    #         return 204
    #     else:
    #         index = self.index_strategy.get_index()
    #         path = '%s%s%s/%s/' % (self.uri, self.index_prefix,
    #                                index, self.doc_type)
    #
    #         res = requests.put(path + id, data=msg)
    #         LOG.debug('Msg put with response code: %s' % res.status_code)
    #         return res.status_code
    #
    # def del_messages(self, id):
    #     LOG.debug('Prepare to delete messages.')
    #     if self.drop_data:
    #         return 204
    #     else:
    #         index = self.index_strategy.get_index()
    #         path = '%s%s%s/%s/' % (self.uri, self.index_prefix,
    #                                index, self.doc_type)
    #
    #         res = requests.delete(path + id)
    #         LOG.debug('Msg delete with response code: %s' % res.status_code)
    #         return res.status_code