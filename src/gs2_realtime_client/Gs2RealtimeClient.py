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

import json

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2RealtimeClient(AbstractGs2Client):

    ENDPOINT = "realtime"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2RealtimeClient, self).__init__(credential, region)


    def create_gathering(self, request):
        """
        ギャザリングを作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_realtime_client.control.CreateGatheringRequest.CreateGatheringRequest
        :return: 結果
        :rtype: gs2_realtime_client.control.CreateGatheringResult.CreateGatheringResult
        """
        body = { 
            "userIds": request.get_user_ids(),
            "name": request.get_name(),
        }

        headers = { 
        }
        from gs2_realtime_client.control.CreateGatheringRequest import CreateGatheringRequest

        from gs2_realtime_client.control.CreateGatheringResult import CreateGatheringResult
        return CreateGatheringResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/gatheringPool/" + str(("null" if request.get_gathering_pool_name() is None else request.get_gathering_pool_name())) + "/gathering",
            service=self.ENDPOINT,
            module=CreateGatheringRequest.Constant.MODULE,
            function=CreateGatheringRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_gathering_pool(self, request):
        """
        ギャザリングプールを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_realtime_client.control.CreateGatheringPoolRequest.CreateGatheringPoolRequest
        :return: 結果
        :rtype: gs2_realtime_client.control.CreateGatheringPoolResult.CreateGatheringPoolResult
        """
        body = { 
            "name": request.get_name(),
            "description": request.get_description(),
        }

        headers = { 
        }
        from gs2_realtime_client.control.CreateGatheringPoolRequest import CreateGatheringPoolRequest

        from gs2_realtime_client.control.CreateGatheringPoolResult import CreateGatheringPoolResult
        return CreateGatheringPoolResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/gatheringPool",
            service=self.ENDPOINT,
            module=CreateGatheringPoolRequest.Constant.MODULE,
            function=CreateGatheringPoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def delete_gathering(self, request):
        """
        ギャザリングを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_realtime_client.control.DeleteGatheringRequest.DeleteGatheringRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_realtime_client.control.DeleteGatheringRequest import DeleteGatheringRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/gatheringPool/" + str(("null" if request.get_gathering_pool_name() is None else request.get_gathering_pool_name())) + "/gathering/" + str(("null" if request.get_gathering_name() is None else request.get_gathering_name())) + "",
            service=self.ENDPOINT,
            module=DeleteGatheringRequest.Constant.MODULE,
            function=DeleteGatheringRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_gathering_pool(self, request):
        """
        ギャザリングプールを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_realtime_client.control.DeleteGatheringPoolRequest.DeleteGatheringPoolRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_realtime_client.control.DeleteGatheringPoolRequest import DeleteGatheringPoolRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/gatheringPool/" + str(("null" if request.get_gathering_pool_name() is None else request.get_gathering_pool_name())) + "",
            service=self.ENDPOINT,
            module=DeleteGatheringPoolRequest.Constant.MODULE,
            function=DeleteGatheringPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def describe_gathering(self, request):
        """
        ギャザリングの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_realtime_client.control.DescribeGatheringRequest.DescribeGatheringRequest
        :return: 結果
        :rtype: gs2_realtime_client.control.DescribeGatheringResult.DescribeGatheringResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_realtime_client.control.DescribeGatheringRequest import DescribeGatheringRequest

        from gs2_realtime_client.control.DescribeGatheringResult import DescribeGatheringResult
        return DescribeGatheringResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/gatheringPool/" + str(("null" if request.get_gathering_pool_name() is None else request.get_gathering_pool_name())) + "/gathering",
            service=self.ENDPOINT,
            module=DescribeGatheringRequest.Constant.MODULE,
            function=DescribeGatheringRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_gathering_pool(self, request):
        """
        ギャザリングプールの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_realtime_client.control.DescribeGatheringPoolRequest.DescribeGatheringPoolRequest
        :return: 結果
        :rtype: gs2_realtime_client.control.DescribeGatheringPoolResult.DescribeGatheringPoolResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_realtime_client.control.DescribeGatheringPoolRequest import DescribeGatheringPoolRequest

        from gs2_realtime_client.control.DescribeGatheringPoolResult import DescribeGatheringPoolResult
        return DescribeGatheringPoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/gatheringPool",
            service=self.ENDPOINT,
            module=DescribeGatheringPoolRequest.Constant.MODULE,
            function=DescribeGatheringPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_gathering(self, request):
        """
        ギャザリングを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_realtime_client.control.GetGatheringRequest.GetGatheringRequest
        :return: 結果
        :rtype: gs2_realtime_client.control.GetGatheringResult.GetGatheringResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_realtime_client.control.GetGatheringRequest import GetGatheringRequest

        from gs2_realtime_client.control.GetGatheringResult import GetGatheringResult
        return GetGatheringResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/gatheringPool/" + str(("null" if request.get_gathering_pool_name() is None else request.get_gathering_pool_name())) + "/gathering/" + str(("null" if request.get_gathering_name() is None else request.get_gathering_name())) + "",
            service=self.ENDPOINT,
            module=GetGatheringRequest.Constant.MODULE,
            function=GetGatheringRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_gathering_pool(self, request):
        """
        ギャザリングプールを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_realtime_client.control.GetGatheringPoolRequest.GetGatheringPoolRequest
        :return: 結果
        :rtype: gs2_realtime_client.control.GetGatheringPoolResult.GetGatheringPoolResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_realtime_client.control.GetGatheringPoolRequest import GetGatheringPoolRequest

        from gs2_realtime_client.control.GetGatheringPoolResult import GetGatheringPoolResult
        return GetGatheringPoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/gatheringPool/" + str(("null" if request.get_gathering_pool_name() is None else request.get_gathering_pool_name())) + "",
            service=self.ENDPOINT,
            module=GetGatheringPoolRequest.Constant.MODULE,
            function=GetGatheringPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def update_gathering_pool(self, request):
        """
        ギャザリングプールを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_realtime_client.control.UpdateGatheringPoolRequest.UpdateGatheringPoolRequest
        :return: 結果
        :rtype: gs2_realtime_client.control.UpdateGatheringPoolResult.UpdateGatheringPoolResult
        """
        body = { 
            "description": request.get_description(),
        }

        headers = { 
        }
        from gs2_realtime_client.control.UpdateGatheringPoolRequest import UpdateGatheringPoolRequest

        from gs2_realtime_client.control.UpdateGatheringPoolResult import UpdateGatheringPoolResult
        return UpdateGatheringPoolResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/gatheringPool/" + str(("null" if request.get_gathering_pool_name() is None else request.get_gathering_pool_name())) + "",
            service=self.ENDPOINT,
            module=UpdateGatheringPoolRequest.Constant.MODULE,
            function=UpdateGatheringPoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))


