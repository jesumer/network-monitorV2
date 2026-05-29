import asyncio
import pyshark

from monitor.database import Session, PacketLog

interface_name = 'Ethernet',


def start_capture():

    # Create event loop for thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    capture = pyshark.LiveCapture(interface=interface_name, use_json=True)

    for packet in capture.sniff_continuously():

        try:
            
            if 'IP' not in packet:
                continue

            src = packet.ip.src
            dst = packet.ip.dst
            
            protocol = packet.transport_layer
            length = packet.length

            print(f'{src} -> {dst} | {protocol}')

            session = Session()

            log = PacketLog(
                source_ip=src,
                destination_ip=dst,
                protocol=protocol,
                length=length
            )

            session.add(log)
            session.commit()
            session.close()

        except Exception as e:
            print(e)