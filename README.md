
# 🧠 Adaptive Learning Organism — v1.0 Foundation

[![CI/CD Pipeline](https://github.com/kraaam12/adaptive-learning-organism-v0.1/actions/workflows/python-app.yml/badge.svg)](https://github.com/kraaam12/adaptive-learning-organism-v0.1/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/gh/kraaam12/adaptive-learning-organism-v0.1/branch/main/graph/badge.svg)](https://codecov.io/gh/kraaam12/adaptive-learning-organism-v0.1)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository contains the v1.0 foundational prototype of the Adaptive Learning Organism, a project designed to serve as the **cognitive "spine"** for an autonomous learning ecosystem tailored for professional trades training.

## Vision

The vision is to build an intelligent instructional agent for a future **Mastery-as-a-Platform (MTPaaP)**. This prototype proves that an expert tutor's adaptive feedback loop can be codified into a modular, testable, and resilient system.

## Project Structure

See directory tree in repo.

## Getting Started

### Prerequisites
- Python 3.10+
- `pip` and `venv`

### Installation & Setup

```bash
git clone https://github.com/kraaam12/adaptive-learning-organism-v0.1.git
cd adaptive-learning-organism-v0.1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run the Simulation

```bash
python learning_organism_cli.py
```

## Run Tests

```bash
pytest --cov=src --cov-report=term-missing
```
