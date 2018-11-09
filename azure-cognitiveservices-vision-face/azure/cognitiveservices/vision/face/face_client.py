# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.face_operations import FaceOperations
from .operations.person_group_person_operations import PersonGroupPersonOperations
from .operations.person_group_operations import PersonGroupOperations
from .operations.face_list_operations import FaceListOperations
from .operations.large_person_group_person_operations import LargePersonGroupPersonOperations
from .operations.large_person_group_operations import LargePersonGroupOperations
from .operations.large_face_list_operations import LargeFaceListOperations
from . import models


class FaceClientConfiguration(Configuration):
    """Configuration for FaceClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        base_url = '{Endpoint}/face/v1.0'

        super(FaceClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-vision-face/{}'.format(VERSION))

        self.endpoint = endpoint
        self.credentials = credentials


class FaceClient(SDKClient):
    """An API for face detection, verification, and identification.

    :ivar config: Configuration for client.
    :vartype config: FaceClientConfiguration

    :ivar face: Face operations
    :vartype face: azure.cognitiveservices.vision.face.operations.FaceOperations
    :ivar person_group_person: PersonGroupPerson operations
    :vartype person_group_person: azure.cognitiveservices.vision.face.operations.PersonGroupPersonOperations
    :ivar person_group: PersonGroup operations
    :vartype person_group: azure.cognitiveservices.vision.face.operations.PersonGroupOperations
    :ivar face_list: FaceList operations
    :vartype face_list: azure.cognitiveservices.vision.face.operations.FaceListOperations
    :ivar large_person_group_person: LargePersonGroupPerson operations
    :vartype large_person_group_person: azure.cognitiveservices.vision.face.operations.LargePersonGroupPersonOperations
    :ivar large_person_group: LargePersonGroup operations
    :vartype large_person_group: azure.cognitiveservices.vision.face.operations.LargePersonGroupOperations
    :ivar large_face_list: LargeFaceList operations
    :vartype large_face_list: azure.cognitiveservices.vision.face.operations.LargeFaceListOperations

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        self.config = FaceClientConfiguration(endpoint, credentials)
        super(FaceClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.face = FaceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.person_group_person = PersonGroupPersonOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.person_group = PersonGroupOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.face_list = FaceListOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.large_person_group_person = LargePersonGroupPersonOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.large_person_group = LargePersonGroupOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.large_face_list = LargeFaceListOperations(
            self._client, self.config, self._serialize, self._deserialize)
