terraform directory structure amended terraform data structure consistent directory structure terraform beginning initial requirement want separate code data future open source code without disclosing implementation detail maybe keeping data private github repository want able encrypt sensitive data repository want support sensitive data encryption part process without manage secret different repository different script etc want create terraform module reuse code want separate terraform code different project one managing infrastructure tier application stack especially important separate resource govuk application initial solution present three directory data module project data directory contains subdirectory per terraform project store variable value customised per environment data directory also contains secret file sensitive data encrypted sop module directory contains subdirectory per terraform provider project directory contains terraform stackstiers project named deploy common infrastructure govuk prefix networking dns zone deploy application group application app prefix frontend puppetmaster data base commontfvars integrationtfvars myapplication commontfvars integrationtfvars integrationsecretsjson module aws routezone mysqldatabaseinstance network project base integrationbackend maintf variablestf myapplication integrationbackend maintf variablestf consequence manage secret explained going decrypt secret file run time make sure clean unencrypted file running terraform command set requires relative path import module terraform stack depend directory initialising project feel comfortable module well consider put github repository source terraform stack via url