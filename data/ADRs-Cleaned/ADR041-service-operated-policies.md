adr service operator provisioned policy serviceoperator allows service team provision various aws service declaratively defining resource submitting via kubernetes api resource require iam authorise provisioned service type action performed example service operator allows provisioning bucket bucket configuration apiversion storagegovsvcukvbeta kind sbucket metadata name sbucketsample spec aws lifecyclerules expiration day versioning enabled true order access provisioned bucket via aws sdk user require iam rolepolicy allows access want thing like bucket acl versioning configuration lifecycle policy defined declaratively via resource manifest see example continuously managed service operator want user provisioned bucket able read back configuration able fully utilise specific bucket reading writing managing object within provisioned bucket want avoid giving permission user could cause conflict property managed service operator reconcile loop example given example manifest would like avoid giving permission would allow user alter expiration lifecyclerules since change user made would periodically overwritten service operator reconciliation provision policy give full access user provisioned service avoid provisioning policy allows user create destroy configure provisioned service remain declarative domain serviceoperator consequence single policy provisioned provisioned service way currently request required permission may practicing principle least privilege