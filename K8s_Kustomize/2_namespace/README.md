# Use a transformer `NamespaceTransformer` to mutate the base configuration of the app in an overlay variant

Change the namespace part of the metadata for the example app's configuration. It's undefined in the
base, but the overlay will serving for setting the namespace value for all
objects to 'dev'.

`overlay/namespace.yaml` defines a Namespace object that ensures the namespace exists in the Kubernetes cluster before any other resources are applied into it (creates the Namespace). By including this manifest in the `resources:` section of `overlay/kustomization.yaml`, it guarantees that the `dev` namespace will be created as part of the apply process.
Without this, applying namespaced resources will fail if the dev namespace does not already exist in the cluster.

Field `namespace: dev` in `overlay\kustomization.yaml` instructs Kustomize to set the `metadata.namespace` field to `dev` on all rendered namespaced objects

1.  Perform a build of the Kustomization in the overlay directory and check its
    content includes the Namespace, and that all objects have their namespace
    set to `dev` accordingly.

`kustomize build overlay/`
