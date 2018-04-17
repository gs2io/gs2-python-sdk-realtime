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


class DeleteGatheringPoolRequest(Gs2BasicRequest):

    class Constant(Gs2Realtime):
        FUNCTION = "DeleteGatheringPool"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteGatheringPoolRequest, self).__init__(params)
        if params is None:
            self.__gathering_pool_name = None
        else:
            self.set_gathering_pool_name(params['gatheringPoolName'] if 'gatheringPoolName' in params.keys() else None)

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
        if gathering_pool_name and not (isinstance(gathering_pool_name, str) or isinstance(gathering_pool_name, unicode)):
            raise TypeError(type(gathering_pool_name))
        self.__gathering_pool_name = gathering_pool_name

    def with_gathering_pool_name(self, gathering_pool_name):
        """
        ギャザリングプールの名前を指定します。を設定
        :param gathering_pool_name: ギャザリングプールの名前を指定します。
        :type gathering_pool_name: unicode
        :return: this
        :rtype: DeleteGatheringPoolRequest
        """
        self.set_gathering_pool_name(gathering_pool_name)
        return self
