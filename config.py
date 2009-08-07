import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

web.config.session_parameters['cookie_name'] = 'webpy_session_id'