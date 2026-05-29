from flask import Blueprint, jsonify
from monitor.database import Session, PacketLog

api_bp = Blueprint('api', __name__)


@api_bp.route('/packets')
def get_packets():
    session = Session()

    packets = session.query(PacketLog).order_by(PacketLog.id.desc()).limit(50).all()

    data = []

    for packet in packets:
        data.append({
            'id': packet.id,
            'source_ip': packet.source_ip,
            'destination_ip': packet.destination_ip,
            'protocol': packet.protocol,
            'length': packet.length
        })

    session.close()

    return jsonify(data)