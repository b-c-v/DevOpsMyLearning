# Strategic Merge patch

Patch the app's Deployment definition, so that it references the generated ConfigMap that holds the `SQLITE_DB_LOCATION` variable and its value.

1. The content of the Strategic Merge patch in the `./overlay/deployment.env.patch.yaml` contains the necessary YAML syntax to allow Kustomize to identify the Deployment as the definition to patch.

2. In `./overlay/kustomization.yaml` included path to patch file

3. Perform a build of the revised Kustomization in the overlay. It contains the generated ConfigMap, and that the same is
   referenced in the app's Deployment definition.

`kustomize build overlay/`
