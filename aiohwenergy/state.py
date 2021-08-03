import logging
from .helpers import generate_attribute_string

Logger = logging.getLogger(__name__)

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

    async def set(self, power_on=None, switch_lock=None, brightness=None):
        state = {}
        if isinstance(power_on, bool):
            state["power_on"] = power_on
        if isinstance(switch_lock, bool):
            state["switch_lock"] = switch_lock
        if isinstance(brightness, int):
            state["brightness"] = brightness
        
        if state == {}:
            Logger.error("At least one state update is required")
            return False, ""
            
        status, response = await self._request('put', 'api/v1/state', state)
        if status == 200 and response:
            # Zip result and original
            self._raw = {**self._raw, **response}
            return True, response
        
        Logger.error("Failed to set state: %s" % response)
        return False, response
        
    @property
    def power_on(self) -> bool:
        """@TODO Friendly name of the device."""
        return self._raw['power_on']

    @property
    def switch_lock(self) -> bool:
        """@TODO Device Type identifier."""
        return self._raw['switch_lock']

    @property
    def brightness(self) -> int:
        """@TODO hex string of the 6 byte / 12 characters device id without delimiters."""
        return self._raw['brightness']

    async def update(self) -> bool:
        status, response = await self._request('get', 'api/v1/state')
        if status == 200 and response:
            self._raw = response
            return True
        
        return False
