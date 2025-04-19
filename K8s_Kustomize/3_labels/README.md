# Use `labels` to manipulate the labels of the objects in an overlay Kustomization.

Add a label to the metadata of the example app's configuration in an overlay.

Show the differences between a base configuration and its customized overlays.

`diff <(kustomize build overlay/) <(kustomize build base/)`

In overlay customization exists label `app.kubernetes.io/env: dev`
