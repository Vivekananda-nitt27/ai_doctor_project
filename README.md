🩺 Doctor AI – Vision, Voice & Chat Backend

A production-ready AI Doctor Backend built using FastAPI, Docker, and AWS, designed to analyze medical images with patient context and generate human-like medical guidance for educational purposes only.

Live Backend URL:
http://44.222.166.201/

Project Overview

Doctor AI is a modular, cloud-ready backend system that:

Accepts medical images and patient text

Processes them through a doctor-style reasoning pipeline

Returns a natural, human-like medical response

Is fully Dockerized

Is structured for CI/CD and AWS deployment

Disclaimer:
This project is strictly for learning and educational purposes and does not replace professional medical consultation.

System Architecture

Client (Gradio / Postman / Frontend)
→ FastAPI Backend (Docker)
→ Doctor Reasoning Service
→ JSON Response

Architecture highlights:

FastAPI for backend stability

Docker-first development

Service-oriented design

No global mutable state

AWS EC2 deployment ready

CI/CD compatible

Project Structure

doctor-ai/
├── app/
│ ├── main.py – FastAPI entrypoint
│ ├── api/
│ │ └── diagnose.py – Diagnose API
│ ├── services/
│ │ └── doctor_brain.py – Core medical reasoning logic
│ └── core/
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md

Live Deployment Details

Cloud Provider: AWS EC2
Container Runtime: Docker
Backend Framework: FastAPI
Port: 8000

Health Check Endpoint:
GET http://44.222.166.201/health

Response:
{"status":"ok"}

API Documentation
Health Check API

Endpoint:
GET /health

Purpose:

Confirms backend is running

Used by Docker, CI/CD, and cloud monitoring

Diagnose API

Endpoint:
POST /diagnose

Description:
Analyzes a medical image along with patient-provided text and returns a doctor-style response.

Request Type:
multipart/form-data

Parameters:
patient_text – string (optional)
image – file (required)

Example (curl):
curl -X POST http://44.222.166.201/diagnose

-F "patient_text=I am experiencing pain in this area"
-F "image=@sample.jpg"

Response:
{
"diagnosis": "With what I see I think you may be experiencing..."
}

Local Docker Deployment (QA Verified)

Step 1: Build Docker Image
docker build -t doctor-ai .

Step 2: Run Docker Container
docker run -p 8000:8000 doctor-ai

Step 3: Verify
Open browser:
http://localhost:8000/health

Expected response:
{"status":"ok"}

Docker Configuration

Uses python:3.10-slim

Installs system dependencies (ffmpeg, libgl1)

No .env or venv copied into image

Clean, lightweight, production-safe image

Same image used locally, in CI/CD, and on AWS

CI/CD Ready Design

This project is structured for CI/CD with:

Docker image build

Push to AWS ECR

Deployment on AWS EC2

Health-check based validation

Supported tools:

GitHub Actions

AWS ECR

AWS EC2

Security and Best Practices

No secrets committed

No global state

No UI logic in backend

Stateless APIs

Clean container builds

Future Enhancements

Voice input and output

Multi-turn chat memory

Automated medical report (PDF)

Vision and LLM integration

Gradio or React frontend

Authentication and rate limiting

Author Note

Built as a learning-oriented AI and DevOps project focusing on:

Real-world backend engineering

Docker and AWS deployment

AI system design best practices

License

This project is released for educational use only.
No medical or commercial liability is assumed.

Status: Live and Stable
Live URL: http://44.222.166.201/
