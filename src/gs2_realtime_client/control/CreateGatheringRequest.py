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


class CreateGatheringRequest(Gs2BasicRequest):

    class Constant(Gs2Realtime):
        FUNCTION = "CreateGathering"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateGatheringRequest, self).__init__(params)
        if params is None:
            self.__gathering_pool_name = None
            self.__name = None
            self.__user_ids = None
        else:
            self.set_gathering_pool_name(params['gatheringPoolName'] if 'gatheringPoolName' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_user_ids(params['userIds'] if 'userIds' in params.keys() else None)

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
        self.__gathering_pool_name = gathering_pool_name

    def with_gathering_pool_name(self, gathering_pool_name):
        """
        ギャザリングプールの名前を指定します。を設定
        :param gathering_pool_name: ギャザリングプールの名前を指定します。
        :type gathering_pool_name: unicode
        :return: this
        :rtype: CreateGatheringRequest
        """
        self.set_gathering_pool_name(gathering_pool_name)
        return self

    def get_name(self):
        """
        ギャザリング名を取得
        :return: ギャザリング名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        ギャザリング名を設定
        :param name: ギャザリング名
        :type name: unicode
        """
        self.__name = name

    def with_name(self, name):
        """
        ギャザリング名を設定
        :param name: ギャザリング名
        :type name: unicode
        :return: this
        :rtype: CreateGatheringRequest
        """
        self.set_name(name)
        return self

    def get_user_ids(self):
        """
        カンマ区切りのギャザリングへの参加を許可するユーザIDリストを取得
        :return: カンマ区切りのギャザリングへの参加を許可するユーザIDリスト
        :rtype: unicode
        """
        return self.__user_ids

    def set_user_ids(self, user_ids):
        """
        カンマ区切りのギャザリングへの参加を許可するユーザIDリストを設定
        :param user_ids: カンマ区切りのギャザリングへの参加を許可するユーザIDリスト
        :type user_ids: unicode
        """
        self.__user_ids = user_ids

    def with_user_ids(self, user_ids):
        """
        カンマ区切りのギャザリングへの参加を許可するユーザIDリストを設定
        :param user_ids: カンマ区切りのギャザリングへの参加を許可するユーザIDリスト
        :type user_ids: unicode
        :return: this
        :rtype: CreateGatheringRequest
        """
        self.set_user_ids(user_ids)
        return self
