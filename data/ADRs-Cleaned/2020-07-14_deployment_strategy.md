deployment strategy currently one environment development every change merged master deployed environment since want developer able continuously integrate change without interfering web application user decided create two environment uat user acceptance testing production since already github action deploy development environment due fact free easy configure decide deploy new environment different considered deployment strategy different environment one branch environment approach environment would branch would merge wanted promote specific environment flow would following push master deploys dev merge usertesting branch deploys usertesting merge production branch deploys production problem method app built separately environment clear rollback method three different version code greater complexity git history nonstandard open source project complex contributor manual trigger environment two possible flow approach push master deploys dev create prerelease deploys staging update prerelease release deploys staging problem approach easy make mistake release instead prerelease github push master deploys dev create tag deploys staging publish release deploys staging problem approach developer add tag branch trigger deploy production creating tag named proddeploy developer push proddeploy tag branch would trigger deployment production case could rollback tagging old commit release tag code pushed master deployed environment flow would following push master deploys dev user testing production feature toggle would disable new feature production approval problem method would store production uat development environment variable build would mean production user would able see detail environment push master would deploy production bug introduced would directly production deployment time would increase partial rollback feature could toggled final weve decided approach similar flow following push master code auto deployed development environment devdeployedxx tag added run local deploy script passing environment uat build deploy devdeployedxx add uatpendingxx tag updated uatdeployedxx deployment environment successful run local deploy script passing environment prod build deploy uatdeployedxx add prodpendingxx tag updated proddeployedxx deployment environment successful rollback local deploy script could run passing prod older build tag devdeployed may enforced build must deployed uat production case rollback would first deploy old build uat deploy uat production con approach application built every time deploy new environment opposed build artifact promote different environment tag trigger deployment uatpendingxx prodpendingxx added branch would trigger deployment despite issue mentioned weve decided approach due time constraint created new github issue investigate artifact link github issue investigate different deployment strategy github issue create uat production environment github issue investigate artifact github action