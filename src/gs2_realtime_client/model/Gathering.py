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

class Gathering(object):

    def __init__(self, params=None):
        if params is None:
            self.__host_id = None
            self.__name = None
            self.__ip_address = None
            self.__user_ids = None
            self.__gathering_pool_id = None
            self.__secret = None
            self.__create_at = None
            self.__gathering_id = None
            self.__owner_id = None
            self.__update_at = None
            self.__port = None
        else:
            self.set_host_id(params['hostId'] if 'hostId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_ip_address(params['ipAddress'] if 'ipAddress' in params.keys() else None)
            self.set_user_ids(params['userIds'] if 'userIds' in params.keys() else None)
            self.set_gathering_pool_id(params['gatheringPoolId'] if 'gatheringPoolId' in params.keys() else None)
            self.set_secret(params['secret'] if 'secret' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_gathering_id(params['gatheringId'] if 'gatheringId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)
            self.set_port(params['port'] if 'port' in params.keys() else None)


    def get_host_id(self):
        """
        ホストGRNを取得
        :return: ホストGRN
        :rtype: unicode
        """
        return self.__host_id

    def set_host_id(self, host_id):
        """
        ホストGRNを設定
        :param host_id: ホストGRN
        :type host_id: unicode
        """
        self.__host_id = host_id

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

    def get_ip_address(self):
        """
        ホストIPアドレスを取得
        :return: ホストIPアドレス
        :rtype: unicode
        """
        return self.__ip_address

    def set_ip_address(self, ip_address):
        """
        ホストIPアドレスを設定
        :param ip_address: ホストIPアドレス
        :type ip_address: unicode
        """
        self.__ip_address = ip_address

    def get_user_ids(self):
        """
        参加可能なユーザIDリストを取得
        :return: 参加可能なユーザIDリスト
        :rtype: list[unicode]
        """
        return self.__user_ids

    def set_user_ids(self, user_ids):
        """
        参加可能なユーザIDリストを設定
        :param user_ids: 参加可能なユーザIDリスト
        :type user_ids: list[unicode]
        """
        self.__user_ids = user_ids

    def get_gathering_pool_id(self):
        """
        通知GRNを取得
        :return: 通知GRN
        :rtype: unicode
        """
        return self.__gathering_pool_id

    def set_gathering_pool_id(self, gathering_pool_id):
        """
        通知GRNを設定
        :param gathering_pool_id: 通知GRN
        :type gathering_pool_id: unicode
        """
        self.__gathering_pool_id = gathering_pool_id

    def get_secret(self):
        """
        暗号鍵を取得
        :return: 暗号鍵
        :rtype: unicode
        """
        return self.__secret

    def set_secret(self, secret):
        """
        暗号鍵を設定
        :param secret: 暗号鍵
        :type secret: unicode
        """
        self.__secret = secret

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_gathering_id(self):
        """
        購読GRNを取得
        :return: 購読GRN
        :rtype: unicode
        """
        return self.__gathering_id

    def set_gathering_id(self, gathering_id):
        """
        購読GRNを設定
        :param gathering_id: 購読GRN
        :type gathering_id: unicode
        """
        self.__gathering_id = gathering_id

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def get_port(self):
        """
        ホストポートを取得
        :return: ホストポート
        :rtype: int
        """
        return self.__port

    def set_port(self, port):
        """
        ホストポートを設定
        :param port: ホストポート
        :type port: int
        """
        self.__port = port

    def to_dict(self):
        return { 
            "hostId": self.__host_id,
            "name": self.__name,
            "ipAddress": self.__ip_address,
            "userIds": self.__user_ids,
            "gatheringPoolId": self.__gathering_pool_id,
            "secret": self.__secret,
            "createAt": self.__create_at,
            "gatheringId": self.__gathering_id,
            "ownerId": self.__owner_id,
            "updateAt": self.__update_at,
            "port": self.__port,
        }