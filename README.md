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


# Flow

When pushing to **development**, the pipeline
- builds the container
- runs the unit tests inside the container
- run the integration tests inside the container
- pushes the image to the GCP container registry
- deploys the new image to Cloud Run's `cicd-sample-app` service in the `gcp-development` project

Since **`staging`** and **`production`** are protected, PRs are required to update their respective contents.

In the even of a PR against either of these branches the pipeline will
- check out the soure branch (assumed to be `development` if merging into `staging`, `staging` if merging into `production`)
- builds the container
- runs the unit tests inside the container
- run the integration tests inside the container

After these checks have completed, the PR is unlocked for merging. Once merged, the pipeline will
- rebuild the container
- push the image to the GCP container registry
- deploy the new image to Cloud Run's `cicd-sample-app` service in the `gcp-staging` or `gcp-production` project