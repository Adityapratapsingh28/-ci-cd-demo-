# Task 3 - DevSecOps for a Healthcare System (demo)

Small demo: a tiny Flask "patient records" API with security gates in the pipeline.

## Security gates (in order)
1. Gitleaks  - scans source code for hardcoded secrets (passwords, keys, tokens)
2. Trivy     - scans the built container image for HIGH/CRITICAL CVEs
3. Trivy     - scans the kubernetes yaml for insecure configuration
4. Only if ALL pass -> push image and deploy

If any gate fails the pipeline stops and nothing reaches production.

## The demo
The app.py initially contains a hardcoded DB password (Hospital@123).
The gitleaks gate catches it and the pipeline FAILS at the security stage.
Fix: the password is replaced by an environment variable read at runtime.
Pipeline reruns -> all gates pass -> app deploys.

## Files
- task3/app/           flask app + Dockerfile
- task3/k8s/           deployment + NodePort service (port 30082)
- task3/Jenkinsfile    the devsecops pipeline
