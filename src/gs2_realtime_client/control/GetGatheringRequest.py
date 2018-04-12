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


class GetGatheringRequest(Gs2BasicRequest):

    class Constant(Gs2Realtime):
        FUNCTION = "GetGathering"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetGatheringRequest, self).__init__(params)
        if params is None:
            self.__gathering_pool_name = None
        else:
            self.set_gathering_pool_name(params['gatheringPoolName'] if 'gatheringPoolName' in params.keys() else None)
        if params is None:
            self.__gathering_name = None
        else:
            self.set_gathering_name(params['gatheringName'] if 'gatheringName' in params.keys() else None)

    def get_gathering_pool_name(self):
        """
        ギャザリングプールの名前を指定します。を取得
        :return: ギャザリングプールの名前を指定します。
        :rtype: unicode
        """
        return self.__gathering_pool_name

    def set_gathering_pool_name(self, gathering_pool_name):
        """
        ギャザリングプールの名前を指定します。を設定
        :param gathering_pool_name: ギャザリングプールの名前を指定します。
        :type gathering_pool_name: unicode
        """
        if not isinstance(gathering_pool_name, unicode):
            raise TypeError(type(gathering_pool_name))
        self.__gathering_pool_name = gathering_pool_name

    def with_gathering_pool_name(self, gathering_pool_name):
        """
        ギャザリングプールの名前を指定します。を設定
        :param gathering_pool_name: ギャザリングプールの名前を指定します。
        :type gathering_pool_name: unicode
        :return: this
        :rtype: GetGatheringRequest
        """
        self.set_gathering_pool_name(gathering_pool_name)
        return self

    def get_gathering_name(self):
        """
        ギャザリングの名前を指定します。を取得
        :return: ギャザリングの名前を指定します。
        :rtype: unicode
        """
        return self.__gathering_name

    def set_gathering_name(self, gathering_name):
        """
        ギャザリングの名前を指定します。を設定
        :param gathering_name: ギャザリングの名前を指定します。
        :type gathering_name: unicode
        """
        if not isinstance(gathering_name, unicode):
            raise TypeError(type(gathering_name))
        self.__gathering_name = gathering_name

    def with_gathering_name(self, gathering_name):
        """
        ギャザリングの名前を指定します。を設定
        :param gathering_name: ギャザリングの名前を指定します。
        :type gathering_name: unicode
        :return: this
        :rtype: GetGatheringRequest
        """
        self.set_gathering_name(gathering_name)
        return self
