#!/usr/bin/env python3

import argparse
import logging
import asyncio

from aiohwenergy import HomeWizardEnergy

async def main(args):
    
    # Make contact with a energy device
    device = HomeWizardEnergy(args.host)
    
    # Update device value
    await device.update()
    
    # Use the data
    print(device.device.product_name)
    print(device.device.serial)
    
    print(device.data)
    print(device.state)
    
    # Close connection
    await device.close()

if __name__ == '__main__':

    ## Commandlineoptions
    parser = argparse.ArgumentParser(description='Example application for aiohwenergy.')

    parser.add_argument( 'host',
                         help='Hostname or IP Address of the device' )

    parser.add_argument( '--loglevel',
                         choices= ['DEBUG', 'INFO','WARNING','ERROR','CRITICAL'],
                         default='INFO',
                         help='Define loglevel, default is INFO.' )

    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args))

    loop.close()
