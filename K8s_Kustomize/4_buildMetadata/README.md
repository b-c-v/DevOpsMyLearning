# Use `buildMetadata` that provides a mechanism to influence the metadata injected during the build process.

Add a label to the metadata of the example app's configuration in an overlay

Show the differences between a base configuration and its customized overlays.

`diff <(kustomize build overlay/) <(kustomize build base/)`

In overlay customization exists label `app.kubernetes.io/managed-by: kustomize-v5.6.0` and
annotation that indicate the origin of the resources `config.kubernetes.io/origin: |  path: ../base/deployment.yaml`
