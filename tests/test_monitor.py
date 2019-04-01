
from unittest import TestCase
from unittest.mock import MagicMock, Mock

import requests
import pytest
from websocket import WebSocket

from lily_monitor.monitor import Monitor


class MonitorTestCase(TestCase):

    @pytest.fixture(autouse=True)
    def initfixtures(self, mocker):
        self.mocker = mocker

    def setUp(self):
        self.m = Monitor()

    #
    # APPEND_TO_REPORT
    #
    def test_append_to_report(self):

        method = MagicMock(
            __name__='ALICE',
            __class__=MagicMock(__name__='JOHN'))

        self.m.append_to_report(method)

        assert self.m.report == [
            {'assertions': [], 'name': 'Monitor::ALICE'},
        ]

    #
    # STOP_REPORT
    #
    def test_stop_report(self):

        self.m.stop_report()

    #
    # CREATE_REPORT
    #
    def test_create_report(self):

        self.m.report = [
            {
                'name': 'Monitor::ALICE',
                'assertions': [
                    {
                        'name': 'test duration',
                        'success': True,
                        'result': 1829,
                        'expected': 1829,
                    },
                ],
            },
        ]

        self.m.create_report()

    #
    # SEND_TO_SLACK
    #
    def test_send_to_slack(self):

        self.m.send_to_slack('what what')

    #
    # GET_URL
    #
    def test_get_url(self):

        self.m.get_url('something')

    #
    # GET_AUTHORIZATION
    #
    def test_get_authorization(self):

        self.mocker.patch.object(requests, 'post').return_value = Mock(
            status_code=201,
            json=Mock(return_value={'token': 'secret'}))

        self.m.get_authorization()

    #
    # ASSERT_DURATION
    #
    def test_assert_duration__success(self):

        self.m.entry = {'assertions': []}

        self.m.assert_duration(
            Mock(
                elapsed=Mock(
                    total_seconds=Mock(return_value=1289))),
            1289)

    def test_assert_duration__fail(self):

        self.m.entry = {'assertions': []}

        self.m.assert_duration(
            Mock(
                elapsed=Mock(
                    total_seconds=Mock(return_value=1290))),
            1289)

    #
    # ASSERT_STATUS_CODE
    #
    def test_assert_status_code__success(self):

        self.m.entry = {'assertions': []}

        self.m.assert_status_code(Mock(status_code=200), 200)

    def test_assert_status_code__fail(self):

        self.m.entry = {'assertions': []}

        self.m.assert_status_code(Mock(status_code=201), 200)

    #
    # ASSERT_CAN_CONNECT_WEBSOCKETS
    #
    def test_assert_can_connect_websockets(self):

        self.mocker.patch.object(WebSocket, 'connect')
        self.m.entry = {'assertions': []}

        self.m.assert_can_connect_websockets('some_uri')
