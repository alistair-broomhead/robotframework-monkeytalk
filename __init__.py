"""
Robotframework interface for Monkeytalk
"""
from connector import Connection, MONKEYTALK_DEFAULT_PORT
__author__ = 'Alistair Broomhead'


class MonkeyTalk(object):
    """ Provides interface
    """
    def __init__(self,
                 device_ip,
                 device_port=MONKEYTALK_DEFAULT_PORT,
                 thinktime=None,
                 timeout=None,
                 mtversion=None):
        self.device_ip = device_ip
        self.device_port = device_port
        self.thinktime = thinktime
        self.timeout = timeout
        self.mtversion = mtversion

    # noinspection PyDocstring
    def monkeytalk_command(self,
                           component="View",
                           monkey_id='*',
                           action='*',
                           arguments=None,
                           timeout=None,
                           thinktime=None):
        """ Runs the given command. If given arguments should be an iterable """
        if timeout is None:
            timeout = self.timeout
        if thinktime is None:
            thinktime = self.thinktime
        connection = Connection(device_ip=self.device_ip,
                                device_port=self.device_port,
                                component=component,
                                thinktime=thinktime,
                                timeout=timeout,
                                monkey_id=monkey_id,
                                mtversion=self.mtversion)
        if arguments is None:
            arguments = []
        connection(action, *arguments)
