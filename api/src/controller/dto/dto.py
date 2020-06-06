'''
DTO interface
'''

import json


class DTO:
    def serialize(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)
