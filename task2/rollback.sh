#!/bin/bash
# rollback.sh - instantly switch traffic back to the blue environment
# usage: ./rollback.sh
# this is the main selling point of blue-green: rollback in one command, no downtime
kubectl --kubeconfig /var/lib/jenkins/kube/config patch svc bg-app-svc -p '{"spec":{"selector":{"version":"blue"}}}'
echo "traffic switched back to BLUE"
kubectl --kubeconfig /var/lib/jenkins/kube/config get svc bg-app-svc -o jsonpath='{.spec.selector.version}'
