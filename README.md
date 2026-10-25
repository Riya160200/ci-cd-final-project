# CI/CD Final Project

## Project Name
Continuous Integration and Continuous Delivery (CI/CD) Final Project

## Overview
This repository contains the application and configuration files for a CI/CD workflow using GitHub Actions and OpenShift Pipelines (Tekton).

## Intended workflow
1. Clean the workspace.
2. Clone the source repository.
3. Run lint checks with flake8.
4. Run unit tests with nose.
5. Build the container image with Buildah.
6. Deploy the application using OpenShift client tooling.

## Status
Project scaffold. Pipeline execution and OpenShift deployment must be configured and validated in the lab environment.
