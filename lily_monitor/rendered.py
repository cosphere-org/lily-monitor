"""Rendered tests.

@sowj you can treat this as a result of rendering, we should get something that
looks similar to that.

"""

from unittest import TestCase

import requests  # pragma: no cover

from .monitor import Monitor, BASE_WS_API_URI  # pragma: no cover


m = Monitor()


class RenderedTestCase(TestCase):  # pragma: no cover

    def setup_method(self, method):
        m.append_to_report(method)

    @classmethod
    def tearDownClass(cls):
        m.stop_report()

    #
    # GATEWAY
    #
    def test_gateway__read_entrypoint(self):

        response = requests.get(m.get_url('/'))

        m.assert_status_code(response, 200)
        m.assert_duration(response, 1000)

    #
    # AUTH
    #
    def test_auth__read_focus_record_summary(self):

        response = requests.get(
            m.get_url('/focus_records/summary/'),
            headers=m.get_authorization())

        m.assert_status_code(response, 200)
        m.assert_duration(response, 1000)

    #
    # ENTITY
    #
    def test_entity__bulk_read_cards(self):

        response = requests.get(
            m.get_url('/cards/'),
            headers=m.get_authorization())

        m.assert_status_code(response, 200)
        m.assert_duration(response, 1000)

    #
    # MEDIA
    #
    def test_media__sign_process(self):

        response = requests.get(
            m.get_url('/mediafiles/processes/sign/'),
            params={
                'to_sign': 'd8s9d8s9xc8s9c8s',
                'datetime': '20181014T123232Z',
            },
            headers=m.get_authorization())

        m.assert_status_code(response, 200)
        m.assert_duration(response, 1000)

    #
    # FRAGMENT
    #
    def test_fragment__bulk_read_fragments(self):

        response = requests.get(
            m.get_url('/fragments/'),
            headers=m.get_authorization())

        m.assert_status_code(response, 200)
        m.assert_duration(response, 1000)

    #
    # CHANNELS
    #
    def test_channels__can_connect(self):

        m.assert_can_connect_websockets(f'{BASE_WS_API_URI}/')
