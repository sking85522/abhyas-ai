# Abhyas Platform (SaaS Platform)

A future-ready Modular Monolith transitioning to Microservices architecture for an AI-powered SaaS product.

## High-Level Architecture

* **Backend**: FastAPI
* **Database**: PostgreSQL
* **Cache**: Redis
* **Queue**: RabbitMQ
* **OCR**: Tesseract + EasyOCR
* **AI/NLP**: PyTorch + Transformers + spaCy
* **Search**: Elasticsearch
* **Storage**: MinIO
* **Containerization**: Docker
* **Deployment**: Kubernetes
* **Monitoring**: Prometheus + Grafana
* **Frontend**: Next.js
* **Mobile**: Flutter

## Directories Overview
* `apps/` - Gateways and UI applications (API Gateway, Admin Panel, Web App, Mobile API).
* `services/` - Independent domain services following the Isolation Rule (Own DB, Own API, Own Models).
* `shared/` - Shared libraries, constants, and utilities for services.
* `infrastructure/` - Deployment and operations configurations.
* `domains/` - Business logic division mapped to services.
* `developer-portal/` - APIs, SDK docs, and onboarding materials.
* `architecture/ADR/` - Architecture Decision Records.

## Principles
1. **Service Isolation**: Every service owns its code, database, API, and tests.
2. **No Direct Imports**: Services communicate via REST APIs or Event Queues (RabbitMQ/Kafka).
3. **API Contract First**: Define endpoints via OpenAPI/Swagger before implementation.
