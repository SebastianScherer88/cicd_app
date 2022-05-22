# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:33:40 2022

@author: bettmensch
"""

# Overview

This repository contains an example of a GCP-based CI/CD pipeline implemented
with Github actions. It covers the 
- testing of code
    - unit testing on Github actions
    - functional/integration testing on built container, 
- building of container image and pushing to a the GCP container registry, and
- deployment to Google Cloud Run.

The Github action pipeline is based on the following reference:
https://github.com/google-github-actions/setup-gcloud/tree/main/example-workflows/cloud-run.


It