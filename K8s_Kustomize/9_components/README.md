# Kustomize Components

Application can be refactored using Kustomize components, enabling greater modularity, reusability, and configurability—without altering the final rendered output.

`kustomize cfg tree`

The `kustomization.yaml` files in `overlays/prod` and `overlays/qa` reference modular configuration via the `components:` field. These components are defined under the shared `./components` directory and enable optional, reusable, environment-specific configuration.

The overlay is the `prod` overlay, and differentiates from the `qa` overlay in the way it exposes the app beyond the cluster for client requests. It uses an Ingress instead of a `LoadBalancer` service.

`prod` Kustomization includes the Ingress Component.It also has some extra build metadata defined; an annotation which provides the origin of the element of configuration for each object.
