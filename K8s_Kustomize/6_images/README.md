# Change aspects of a workload's image, whether that's name, tag or digest

Redefine the container image name used by the application in the `dev` overlay. This demonstrates how to serve different versions of the app based on the target deployment environment.

1. Perform a build of the revised Kustomization in the overlay.

`kustomize build overlay/`

2. Make a comparison of the two builds, ensure the tag is now `dev` instead of `v1.0`.

`diff <(kustomize build overlay/) <(kustomize build base/) | grep image`


