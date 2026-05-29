# Python Network Monitoring App V2
## Purpose of the Project

This project demonstrates how Python can be used to build a modern web-based network monitoring system capable of capturing, analyzing, and visualizing network traffic in real time.

## Overview

I created a complete Python network monitoring app project using:

- Python
- Flask
- PyShark
- REST API
- Tailwind CSS
- Vanilla JavaScript
- SQLite

---

# Features

✅ Live packet capture  
✅ REST API endpoints  
✅ Real-time dashboard UI  
✅ Traffic statistics monitoring  
✅ SQLite database logging  
✅ Responsive Tailwind CSS frontend  
✅ Vanilla JavaScript integration  
✅ Future feature roadmap  
✅ Docker deployment example  

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| PyShark | Packet capture and analysis |
| SQLite | Database logging |
| REST API | Backend communication |
| Tailwind CSS | Responsive UI design |
| Vanilla JavaScript | Frontend interactions |
| Docker | Containerized deployment |

---

# Core Functionalities

## Live Packet Capture

The application captures network packets in real time using PyShark and displays live traffic data through the dashboard.

## REST API

Provides API endpoints for:

- Packet statistics
- Traffic logs
- Device monitoring
- Network status

## Dashboard UI

A modern responsive dashboard built with Tailwind CSS featuring:

- Traffic charts
- Live packet updates
- Device status cards
- Monitoring panels

## SQLite Logging

Stores captured traffic data locally for:

- Historical logs
- Traffic analysis
- Report generation

---

# Frontend Features

- Responsive layout
- Dark mode ready
- Real-time updates
- Tailwind CSS components
- JavaScript API integration

---

# Future Features To Add

- Intrusion Detection System (IDS)
- Email alerts
- WebSocket live updates
- Multi-device monitoring
- User authentication
- Role-based access control
- Export reports (PDF/CSV)
- AI-based anomaly detection
- SNMP monitoring
- Grafana integration

---

# Docker Deployment Example

```bash
docker build -t network-monitor .
docker run -p 5000:5000 network-monitor
