# CI/CD Final Project

[![Build Status](https://github.com/Riya160200/ci-cd-final-project/actions/workflows/workflow.yml/badge.svg?branch=main)](https://github.com/Riya160200/ci-cd-final-project/actions/workflows/workflow.yml)

## Project Name
Continuous Integration and Continuous Delivery (CI/CD) Final Project

## Overview
This repository contains a Python Flask Customer Accounts microservice and configuration for continuous integration using GitHub Actions, plus deployment pipeline scaffolding for OpenShift Pipelines (Tekton).

## Intended workflow
1. Clean the workspace.
2. Clone the source repository.
3. Run lint checks with Flake8.
4. Run unit tests with Nose.
5. Build the container image with Buildah.
6. Deploy the application using OpenShift client tooling.

## Build status
The badge above reports the current status of the GitHub Actions workflow. Open the badge to view the workflow runs.

## Project components
- Flask REST API for customer accounts
- GitHub Actions CI workflow
- Dockerfile and container configuration
- Tekton pipeline, tasks, and workspace configuration

## Validation note
The CI workflow is configured to run linting and unit tests. OpenShift/Tekton deployment must be run and verified in the course lab environment.
