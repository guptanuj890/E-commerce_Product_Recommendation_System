# 🛍️ E-commerce Product Recommendation System (End-to-End)

This repository details an end-to-end **E-commerce Product Recommendation System** using a modern, scalable architecture. It covers the full machine learning operations (MLOps) lifecycle, from data ingestion to cloud deployment and monitoring.

---

## 🌟 Key Features

* **Modular Pipeline:** A structured flow from configuration, data conversion, and ingestion to the RAG chain and web UI.
* **Recommendation Logic:** Utilizes a **RAG (Retrieval-Augmented Generation) Chain** for product recommendation.
* **Demo Application:** A **Flask-based** web application (HTML/CSS) to query and demonstrate recommendations.
* **Containerization:** Full setup with **Dockerfile** and **Kubernetes manifests** for portability and orchestration.
* **Cloud Deployment:** Tested deployment on a **GCP Compute Engine VM** using **Minikube**.
* **Monitoring & Observability:** Integration with **Prometheus** for scraping application metrics and **Grafana** for visualization.

---

## ⚙️ Tech Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.8+ | Core development and ML pipeline |
| **Web** | Flask, HTML, CSS | Recommendation API and demo UI |
| **Data & ML** | Pandas, NumPy, scikit-learn, (Embeddings) | Data manipulation and recommendation model components |
| **Containerization** | Docker | Packaging the application and its dependencies |
| **Orchestration** | Kubernetes (Minikube) | Managing the containerized deployment |
| **Cloud** | Google Cloud Platform (GCP VM) | Hosting the environment |
| **Monitoring** | Prometheus, Grafana | Metrics collection and dashboard visualization |
| **Dev Tools** | Git, GitHub | Version control and collaboration |

---

## 🏛️ Repository Structure

E-commerce_Product_Recommendation_System/ ├── app/ # Flask application and web resources │ ├── app.py # Main Flask application │ ├── templates/ # HTML templates for the UI │ └── static/ # CSS/JS and static assets ├── src/ # Core pipeline: config, converter, ingestion, RAG │ ├── config.py # Project configurations │ ├── data_converter.py # Raw data conversion logic │ ├── data_ingestion.py # Data storage/DB ingestion │ ├── rag_chain.py # Logic for RAG structure/embeddings │ └── recommend.py # Offline recommendation execution ├── deployment/ │ ├── Dockerfile # Docker build file for the app │ ├── k8s/ # Kubernetes deployment manifests │ │ ├── deployment.yaml │ │ ├── service.yaml │ │ ├── prometheus-deploy.yaml │ │ └── grafana-deploy.yaml ├── docs/ │ └── Flipkart_product_recommender_Workflow.png # Project architecture diagram ├── data/ # Placeholder for raw/processed data ├── notebooks/ # EDA, experimentation, and evaluation scripts ├── requirements.txt # Python dependency list ├── README.md # This file └── scripts/ ├── build_and_push.sh # Script to build and push Docker image └── deploy_minikube.sh # Script to deploy K8s manifests on Minikube


---

## 🛠️ Local Development (Quickstart)

### 1. Clone & Install Dependencies

```bash
git clone [https://github.com/guptanuj890/E-commerce_Product_Recommendation_System.git](https://github.com/guptanuj890/E-commerce_Product_Recommendation_System.git)
cd E-commerce_Product_Recommendation_System

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows (alternative)

pip install -r requirements.txt


2. Configuration
Edit src/config.py (or environment variables) to set necessary paths and settings:

Data file paths

Model checkpoint/embedding paths

Flask server host/port

Prometheus metrics endpoint path

3. Run Pipeline Steps
Run the data preprocessing and ingestion steps:

python src/data_converter.py      # Convert raw data format
python src/data_ingestion.py      # Ingest data into persistent storage (DB/local)

Run the RAG chain setup (building retrieval structures/embeddings):

python src/rag_chain.py          # Builds retrieval structures, embeddings
python src/recommend.py --user_id 123  # Test recommendation offline

4. Start the Flask Demo

cd app
python app.py
# Open http://localhost:5000 in your browser.

🐳 Docker & Kubernetes Deployment
Build and Push Docker Image
Build the Image: (From the repository root)

Bash

docker build -t <your-dockerhub-username>/product-recommender:latest -f deployment/Dockerfile .
Push to Registry:

Bash

docker push <your-dockerhub-username>/product-recommender:latest
Kubernetes (Local with Minikube)
The K8s manifests are in deployment/k8s/.

Bash

# Apply application deployment and service
kubectl apply -f deployment/k8s/deployment.yaml
kubectl apply -f deployment/k8s/service.yaml
Tip: If using Minikube with a local Docker daemon, use minikube image load <your-image> to skip pushing to Docker Hub.

☁️ Cloud Deployment (GCP VM + Minikube)
This section describes deploying the system on a GCP Compute Engine VM using Minikube.

1. Prepare GCP VM
Create a Compute Engine VM instance (e.g., Ubuntu, sufficient CPU/RAM).

SSH into the VM.

2. Install Docker, Minikube & Kubectl on VM
Bash

# On VM (Ubuntu example)
sudo apt-get update
sudo apt-get install -y docker.io
# Install minikube and kubectl
curl -LO [https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64](https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64)
sudo install minikube-linux-amd64 /usr/local/bin/minikube
curl -LO "[https://dl.k8s.io/release/$(curl](https://dl.k8s.io/release/$(curl) -L -s [https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl](https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl)"
sudo install kubectl /usr/local/bin/kubectl

# Start Minikube
minikube start --driver=docker
3. Deploy Application to Minikube
Load the pushed image into Minikube's context:

Bash

minikube image load <your-dockerhub-username>/product-recommender:latest
Apply the Kubernetes manifests:

Bash

kubectl apply -f deployment/k8s/deployment.yaml
kubectl apply -f deployment/k8s/service.yaml
4. Set up Monitoring (Prometheus & Grafana)
Apply the monitoring manifests:

Bash

kubectl apply -f deployment/k8s/prometheus-deploy.yaml
kubectl apply -f deployment/k8s/grafana-deploy.yaml
Access Grafana:

Forward the Grafana service port to your local machine:

Bash

kubectl port-forward svc/grafana 3000:3000
# Visit http://localhost:3000
Default Credentials: Often admin/admin—change immediately on first login.

📊 Monitoring (Prometheus + Grafana)
Application Instrumentation
The Flask application, using a library like prometheus_client, exposes key metrics at the /metrics endpoint, including:

Request latency and count

Recommendation response time

Cache hit/miss ratio (if caching is implemented)

Custom model inference time

Prometheus Configuration
The prometheus-deploy.yaml sets up a Prometheus server to scrape metrics from:

The application pods (app:5000/metrics).

Kubernetes system metrics (optional).

Grafana Dashboards
Grafana is configured to use Prometheus as a data source. Example dashboards should track:

App Performance: Request latency, throughput, error rate.

Infrastructure: Pod CPU/memory utilization.

Model Health: Custom model inference time graphs.