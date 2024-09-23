""" A script to replace the response body with a custom message. 
"""

from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    """Replaces the response body with a custom message.

    Args:
        flow (http.HTTPFlow): An HTTP flow represented by mitmproxy.
    """
    flow.response.content = flow.response.content.decode().replace("Helloooo! I'm a legit site!", "Hi... You're now seeing eve's contents!").encode()
