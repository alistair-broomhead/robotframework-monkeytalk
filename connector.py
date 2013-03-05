"""
class giving connection to monkeytalk
"""

__author__ = 'Alistair Broomhead'
MONKEYTALK_DEFAULT_PORT = 16863


class Connector(object):
    """ Low-level interface for monkeytalk on the device """

    def __init__(self, device_ip, device_port=MONKEYTALK_DEFAULT_PORT):
        self.device_ip = device_ip
        self.device_port = device_port

    @property
    def url(self):
        """ Monkeytalk endpoint URL """
        return "http://%(ip)s:%(port)r" % {
            'ip': self.device_ip, 'port': self.device_port}

    def __call__(self, data):
        import json
        import urllib2

        json_data_in = json.dumps(data)
        print json_data_in
        request = urllib2.Request(self.url, json_data_in)
        response = urllib2.urlopen(request)
        json_data_out = response.read()
        return json.loads(json_data_out)


class Connection(object):
    """ Mid-level interface for monkeytalk on the device """

    @property
    def component(self):
        """ The component to which you will be connecting """
        return self.state['componentType']

    @component.setter
    def component(self, comp=None):
        """
        The component to which you will be connecting
        :param comp: str
        """
        if comp is None:
            comp = 'View'
        elif not isinstance(comp, str):
            raise TypeError("Expected comp as a string or undefined")
        self.state['componentType'] = comp

    @property
    def thinktime(self):
        """ thinktime modifier """
        return self.state['modifiers']['thinktime']

    @thinktime.setter
    def thinktime(self, t):
        """
        thinktime modifier
        :param t: int
        """
        if not isinstance(t, int):
            raise TypeError("Expected t as an integer")
        self.state['modifiers']['thinktime'] = t

    @property
    def timeout(self):
        """ timeout modifier """
        return self.state['modifiers']['timeout']

    @timeout.setter
    def timeout(self, t):
        """
        timeout modifier
        :param t: int
        """
        if not isinstance(t, int):
            raise TypeError("Expected t as an integer")
        self.state['modifiers']['timeout'] = t

    @property
    def monkey_id(self):
        """ monkeyId to connect to """
        return self.state['monkeyId'] if 'monkeyId' in self.state else '*'

    @monkey_id.setter
    def monkey_id(self, id_=None):
        """
        monkeyId to connect to
        :param id_: str
        """
        if id_ is None:
            id_ = '*'
        elif not isinstance(id_, str):
            raise TypeError("Expected id_ as a string or undefined")
        self.state['monkeyId'] = id_

    @property
    def mtversion(self):
        """ monkeytalk version in use """
        return self.state['mtversion'] if 'mtversion' in self.state else 1

    @mtversion.setter
    def mtversion(self, vers=None):
        """
        monkeytalk version in use
        :param vers: int
        """
        if vers is None:
            vers = 1
        elif not isinstance(vers, int):
            raise TypeError("Expected vers as an integer or undefined")
        self.state['mtversion'] = vers

    def __init__(self,
                 device_ip,
                 device_port=MONKEYTALK_DEFAULT_PORT,
                 component=None,
                 thinktime=None,
                 timeout=None,
                 monkey_id=None,
                 mtversion=None
    ):
        self.connector = Connector(device_ip, device_port)
        self.state = {
            'modifiers': {},
            'mtcommand': 'PLAY'
        }
        self.component = component
        if thinktime is not None:
            self.thinktime = thinktime
        if timeout is not None:
            self.timeout = timeout
        self.monkey_id = monkey_id
        self.mtversion = mtversion

    def __call__(self,
                 action,
                 *args):
        data = self.state.copy()
        data['action'] = action
        data['args'] = args
        from time import time
        data['timestamp'] = int(time() * 1000)
        return self.connector(data)
