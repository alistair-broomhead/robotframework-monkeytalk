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
                           component,
                           monkey_id,
                           action,
                           arguments='',
                           timeout='',
                           thinktime=''):
        """ Runs the given command. If given arguments should be an iterable """
        if not timeout:
            timeout = self.timeout
        if not thinktime:
            thinktime = self.thinktime
        connection = Connection(device_ip=self.device_ip,
                                device_port=self.device_port,
                                component=component,
                                thinktime=thinktime if thinktime else None,
                                timeout=timeout if timeout else None,
                                monkey_id=monkey_id,
                                mtversion=self.mtversion)
        if not arguments:
            ret = connection(action)
        else:
            ret = connection(action, *arguments)
        assert ret['result'] == 'OK'
