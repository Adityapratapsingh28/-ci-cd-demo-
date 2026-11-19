# Task 2 - Blue-Green Deployment with Jenkins, Docker and Kubernetes

Small demo setup.

## What it does
Two identical environments (BLUE = old version, GREEN = new version) run side by side.
Jenkins builds both images, deploys both, smoke-tests green, then waits for a human
to approve the traffic switch. The switch itself is a one-line change of the service
selector, so it is instant and there is zero downtime.

## Files
- task2/blue/          blue app (version 1.0) + Dockerfile
- task2/green/         green app (version 2.0) + Dockerfile
- task2/k8s/           blue-deployment, green-deployment, service (NodePort 30081)
- task2/Jenkinsfile    the pipeline with approval gate
- task2/rollback.sh    one command to switch traffic back to blue

## How the switch works
The service picks pods by label. Only thing that changes between blue and green
is the label value in the service selector:

    selector:
      app: bg-app
      version: blue    <- change to green and traffic flips instantly
