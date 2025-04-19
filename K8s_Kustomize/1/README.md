# Create the base configuration using a Kustomize overlay

1. Create a Kustomization in the base directory.

```
cd base
kustomize create --autodetect
cat kustomization.yaml
```

2. Build of the Kustomization in the base directory and check its content includes the Deployment and Service, but unaltered.

```
kustomize build .
```

3.  Generates a kustomization.yaml file and adds a reference to a directory (e.g., ../base) containing Kubernetes manifests or another Kustomization base.

```
cd ../overlay
kustomize create --resources ../base
cat kustomization.yaml
```

4. Add build metadata to the Kustomization, so that the rendered object definitions contain the 'managed by' label.

```
kustomize edit add buildmetadata managedByLabel
cat kustomization.yaml
```

5.  Perform a build of the Kustomization in the overlay directory and check its
    content includes the Deployment and Service, but with the 'managed by'
    label added.

```
kustomize build .
```
