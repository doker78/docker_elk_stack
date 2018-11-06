export POD_NAME=$(kubectl get pods -o go-template --template '\n')
echo Name of the Pod: $POD_NAME
