#!/usr/bin/env python3
"""Example usage for device discovery."""

from zeroconf import ServiceBrowser, Zeroconf


class MyListener:
    """mDNS listener."""

    def remove_service(self, zeroconf, type, name):
        """Service removed from network."""
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        """Service added to network."""
        info = zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_hwenergy._tcp.local.", listener)

try:
    print("Searching for HomeWizard Energy devices")
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()
