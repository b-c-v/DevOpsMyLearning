# Use the `configMapGenerator` create the ConfigMap to supply an alternative value for the variable `SQLITE_DB_LOCATION`

`configMapGenerator` should be implemented in the `./base/kustomization.yaml` because it is not patchable in the same way that other resources are.

1. Perform a build of the base Kustomization and check that it includes the generated ConfigMap. Pay particular attention to the name, which should have a suffix appended.

`kustomize build /base`

2. Change the value of the `SQLITE_DB_LOCATION` variable in the `./base/kustomization.yaml` the sub-directory should be `/tmp/db/todo.db` instead of `/tmp/todos/todo.db`. The change in the content of the data provides Kustomize with the opportunity to generate a new ConfigMap. This, in turn, precipitates a change to the definition of the Deployment, which results in a workload update when applied to the cluster.

3. Perform a build of the base Kustomization and check that it includes the revised ConfigMap. **The ConfigMap should have a different suffix** this time,computed from the revised data content.

`kustomize build /base`
