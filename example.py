#!/usr/bin/env python3
"""Example for using Package."""

import argparse
import logging
import asyncio

from aiohwenergy import HomeWizardEnergy

parser = argparse.ArgumentParser(description="Example application for aiohwenergy.")
parser.add_argument("host", help="Hostname or IP Address of the device")
parser.add_argument(
    "--loglevel",
    choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    default="INFO",
    help="Define loglevel, default is INFO.",
)

args = parser.parse_args()


async def main():
    """Run the example."""

    logging.basicConfig(level=args.loglevel)

    # Make contact with a energy device
    async with HomeWizardEnergy(args.host) as api:
        await api.initialize()

        # Use the data
        print(api.device.product_name)
        print(api.device.serial)
        print(api.device)

        print(api.data)
        print(api.state)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
