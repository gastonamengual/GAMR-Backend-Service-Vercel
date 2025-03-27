# GAMR MLOps Project

This repo is part of the GAMR MLOps project, designed to showcase a flexible and scalable MLOps architecture. By integrating multiple clients and model registries, it simulates real-world industry scenarios where different components need to work together seamlessly. The goal is to demonstrate how a well-structured, decoupled system can make AI deployments more efficient, adaptable, and easy to maintain.

# Backend API Service

This repository contains the backend API service of the project. Built with FastAPI, it handles request validation, authentication, and communication between the client application and the model registries. The API supports both image classification and iris flower recognition by interacting with dedicated model registries.

## Architecture Overview
The client is part of a layered MLOps architecture:
- **Client:** Streamlit-based UI for user interaction.
- **Backend:** FastAPI service handling request validation and authentication, hosted both in Render as a Docker Image and on Vercel.
- **Model Registry:**
  - Hugging Face model for image classification.
  - MLFlow model hosted on Render in a Docker container for iris classification.

## Usage

1. Open the app in [https://gamr-image-recognition.streamlit.app](https://gamr-image-recognition.streamlit.app).

2. Chose either object detection or flower classification.

3. View predictions and results in real-time.

- **For image classification:** Upload an image, and the model will return the predicted class.
- **For iris classification:** Input sepal/petal measurements, and the model will predict the iris species.


## WIP and Future Enhancements
- 100% test coverage.
- Enhanced authentication and security features.
- Optimized API performance and logging.

---

Feel free to suggest improvements!
