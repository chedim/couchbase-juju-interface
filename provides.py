from charmhelpers.core import hookenv
from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint


class Couchbase(Endpoint):
    def publish_connection_info(self, endpoint, username, password):
        for relation in self.relation:
            relation.to_publish['endpoint'] = endpoint;
            relation.to_publish['username'] = username;
            relation.to_publish['password'] = password;

    def set_ready(self, ready):
        if ready:
            set_flag(self.expand_name('{endpoint_name}.available'))
        else
            clear_flag(self.expand_name('{endpoint_name}'.available))

    @when('endpoint.{endpoint_name}.joined')
    def _joined(self):
        set_flag(self.expand_name('{endpoint_name}.connected'))
