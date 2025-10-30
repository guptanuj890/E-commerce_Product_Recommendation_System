#E-commerce Product Recommendation System (End-to-End)
##Overview

This repository contains an end-to-end E-commerce Product Recommendation System with:

data ingestion and preprocessing,

a RAG (Retrieval-Augmented Generation) chain and recommendation logic,

a Flask web application (HTML/CSS) for demonstration,

containerization (Docker), Kubernetes manifests for deployment,

cloud deployment on a GCP VM running Minikube, and

monitoring using Prometheus and Grafana.

The architecture follows the workflow illustrated in Flipkart product recommender Workflow.png (project diagram): local development → containerization → K8s manifests → deploy on GCP VM (Minikube) → monitor with Prometheus/Grafana.

##Key Features

Modular pipeline: configuration → data conversion → ingestion → RAG chain → web UI

Flask-based demo application (HTML/CSS) to query recommendations

Dockerfile and Kubernetes manifests for containerized deployment

Prometheus metrics exposed by the app and scraped by Prometheus

Grafana dashboards to visualize app & infrastructure metrics

Version control workflow for CI/CD style commit & push integration

##Tech Stack

Language: Python 3.8+

Web: Flask, HTML, CSS, (optionally JS)

Data & ML: Pandas, NumPy, scikit-learn, (embedding libraries or transformer usage if applicable)

Containerization: Docker

Orchestration: Kubernetes (manifests included) — tested on Minikube inside a GCP VM

Cloud: Google Cloud Platform (Compute Engine VM)

Monitoring: Prometheus, Grafana

Dev tools: Git, GitHub


E-commerce_Product_Recommendation_System/
├── app/                          # Flask application and web resources
│   ├── app.py
│   ├── templates/
│   └── static/
├── src/                          # Core pipeline: config, converter, ingestion, RAG
│   ├── config.py
│   ├── data_converter.py
│   ├── data_ingestion.py
│   ├── rag_chain.py
│   └── recommend.py
├── deployment/
│   ├── Dockerfile
│   ├── k8s/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── prometheus-deploy.yaml
│   │   └── grafana-deploy.yaml
├── docs/
│   └── Flipkart_product_recommender_Workflow.png
├── data/                         # raw/processed data (or instructions to fetch)
├── notebooks/                    # EDA and experiments
├── requirements.txt
├── README.md
└── scripts/
    ├── build_and_push.sh
    └── deploy_minikube.sh
