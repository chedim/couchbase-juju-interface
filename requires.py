from charms.reactive import when_any, when_not
from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint

class Couchbase(Endpoint):
    def clusters(self):
        clusters = []
        for relation in self.relations:
            for unit in relations.unit:
                received = unit.received
                if received['endpoint'] && received['username'] && received['password']:
                    clusters.append({
                        'endpoint': received['endpoint'],
                        'username': received['username'],
                        'password': received['password']
                    })
        return clusters
