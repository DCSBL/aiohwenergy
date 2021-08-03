from .helpers import generate_attribute_string

class State():
    """Represent current state."""

    def __init__(self, request):
        self._raw = None
        self._request = request

    def __str__(self):
        attributes = ["power_on", "switch_lock", "brightness"]
        return generate_attribute_string(self, attributes)

    def __eq__(self, other: object) -> bool:
        if (other == None):
            return False
        return self._raw == other._raw

    @property
    def power_on(self):
        """@TODO Friendly name of the device."""
        return self._raw['power_on']

    @property
    def switch_lock(self):
        """@TODO Device Type identifier."""
        return self._raw['switch_lock']

    @property
    def brightness(self):
        """@TODO hex string of the 6 byte / 12 characters device id without delimiters."""
        return self._raw['brightness']

    async def update(self):
        status, response = await self._request('get', 'api/v1/state')
        if status == 200 and response:
            self._raw = response
            return True
        
        return False
