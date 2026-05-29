async function fetchPackets() {
    const response = await fetch('/api/packets');
    const data = await response.json();

    const table = document.getElementById('packetTable');

    table.innerHTML = '';

    let tcp = 0;
    let udp = 0;
    let icmp = 0;

    data.forEach(packet => {

        if (packet.protocol === 'TCP') tcp++;
        if (packet.protocol === 'UDP') udp++;
        if (packet.protocol === 'ICMP') icmp++;

        table.innerHTML += `
            <tr class="border-b border-gray-700 hover:bg-gray-700">
                <td class="p-4">${packet.id}</td>
                <td class="p-4">${packet.source_ip}</td>
                <td class="p-4">${packet.destination_ip}</td>
                <td class="p-4">${packet.protocol}</td>
                <td class="p-4">${packet.length}</td>
            </tr>
        `;
    });

    document.getElementById('totalPackets').innerText = data.length;
    document.getElementById('tcpCount').innerText = tcp;
    document.getElementById('udpCount').innerText = udp;
    document.getElementById('icmpCount').innerText = icmp;
}

setInterval(fetchPackets, 2000);

fetchPackets();