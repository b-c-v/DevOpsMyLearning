# Apply a JSON patch to remove some configuration inherited from the base

Patch the app's Deployment definition, so that it removes the security context used to force the pod to run as the root user. The patch will be a JSON patch this time. The build output will be compared with the output generated in the previous exercise.

1.  Perform a build of the Kustomization

`kustomize build overlay/`

Confirm that the Deployment includes `configMapRef: name: db`, which was added via the `deployment.env.patch.yaml` file, and that it does not include a securityContext, as it was removed by the `op: remove` operation in kustomization.yaml
