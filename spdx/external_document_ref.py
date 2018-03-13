
# Copyright (c) 2018 Yash M. Nisar
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from functools import total_ordering


@total_ordering
class ExternalDocumentRef(object):
    """
    External Document References entity that contains the following fields :
    - external_document_id: A unique string containing letters, numbers, '.',
        '-' or '+'.
    - spdx_document_uri: The unique ID of the SPDX document being referenced.
    - check_sum: The checksum of the referenced SPDX document.
    """

    def __init__(self, external_document_id=None, spdx_document_uri=None,
                 check_sum=None):
        self.external_document_id = external_document_id
        self.spdx_document_uri = spdx_document_uri
        self.check_sum = check_sum

    def __eq__(self, other):
        return (
            isinstance(other, ExternalDocumentRef)
            and self.external_document_id == other.external_document_id
            and self.spdx_document_uri == other.spdx_document_uri
            and self.check_sum == other.check_sum
        )

    def __lt__(self, other):
        return (
            (self.external_document_id, self.spdx_document_uri,
             self.check_sum) <
            (other.external_document_id, other.spdx_document_uri,
             other.check_sum,)
        )

    def validate(self, messages=None):
        """
        Validate all fields of the ExternalDocumentRef class and update the
        messages list with user friendly error messages for display.
        """
        messages = messages if messages is not None else []

        return (self.validate_ext_doc_id(messages) and
                self.validate_spdx_doc_uri(messages) and
                self.validate_chksum(messages)
        )

    def validate_ext_doc_id(self, messages=None):
        messages = messages if messages is not None else []

        if self.external_document_id:
            return True
        else:
            messages.append('ExternalDocumentRef has no External Document ID.')
            return False

    def validate_spdx_doc_uri(self, messages=None):
        messages = messages if messages is not None else []

        if self.spdx_document_uri:
            return True
        else:
            messages.append('ExternalDocumentRef has no SPDX Document URI.')
            return False

    def validate_chksum(self, messages=None):
        messages = messages if messages is not None else []

        if self.check_sum:
            return True
        else:
            messages.append('ExternalDocumentRef has no Checksum.')
            return False
