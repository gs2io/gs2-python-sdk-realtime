# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_realtime_client.Gs2Realtime import Gs2Realtime


class CreateGatheringPoolRequest(Gs2BasicRequest):

    class Constant(Gs2Realtime):
        FUNCTION = "CreateGatheringPool"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateGatheringPoolRequest, self).__init__(params)
        if params is None:
            self.__name = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)

    def get_name(self):
        """
        ギャザリングプールの名前を取得
        :return: ギャザリングプールの名前
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        ギャザリングプールの名前を設定
        :param name: ギャザリングプールの名前
        :type name: unicode
        """
        if not isinstance(name, unicode):
            raise TypeError(type(name))
        self.__name = name

    def with_name(self, name):
        """
        ギャザリングプールの名前を設定
        :param name: ギャザリングプールの名前
        :type name: unicode
        :return: this
        :rtype: CreateGatheringPoolRequest
        """
        self.set_name(name)
        return self

    def get_description(self):
        """
        ギャザリングプールの説明を取得
        :return: ギャザリングプールの説明
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        ギャザリングプールの説明を設定
        :param description: ギャザリングプールの説明
        :type description: unicode
        """
        if not isinstance(description, unicode):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        ギャザリングプールの説明を設定
        :param description: ギャザリングプールの説明
        :type description: unicode
        :return: this
        :rtype: CreateGatheringPoolRequest
        """
        self.set_description(description)
        return self
