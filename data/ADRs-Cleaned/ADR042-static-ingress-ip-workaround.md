adr static ingres workaround production system existing requirement static ingres external userscompanies relying able safelist ingres current ingres architecture namespace within cluster dynamically provisioned nlb network load balancer directs traffic namespaces ingressgateway see adr detail architecture static address create complication dynamic ephemeral infrastructure system would like continue push back kind static configuration add little security great cost complexity however meantime way allocate static ingres already provisioned advertised potential ingres relevant external party eips yet allocated possible attach eips existing nlb without recreating research space merged kubernetes change allows allocating eips dynamically provisioned loadbalancer service would allow provision static aws elastic attach ingres load balancer require unfortunately time writing eks expect reach around month aws global accelerator crossregion loadbalancer service provides static allows forwarding traffic regionalloadbalancers directly instance could manually provision global accelerator point clusterprovisioned ingres nlb could manually provision new nlb point worker node designated nodeport could terraform provision global accelerator new nlb point clusterprovisioned ingres nlb supported terraform time could create controller manage provisioning global accelerator point clusterprovisioned ingres nlb based custom andor service resource configuration could create controller manage provisioning new nlb point worker node designated nodeport based custom andor service resource configuration manually provision global accelerator pointing ingres nlb aws console point clusterprovisioned ingres nlb intended temporary solution running version eks control plane support attaching eips loadbalancer service choose global accelerator rather second loadbalancer traffic shaping feature offer good route deprecating workaround future complicated attempting duplicate required targetgroups dynamically provisioned worker node choose write controller manage provisioning due expectation temporary solution expect anyone else benefit engineering effort consequence since ingres nlbs dynamically managed eks potential nlb get disconnected manually provisioned endpoint workaround affect designated namespaces potentially lead difference stagingtesting production deployment configuration appendix note brief spike configuration found global accelerator spike note