logging approach deciders daniel grant robert kenny technical story identity utilise approach log management aligns wellcome collection existing logging requirement infrastructure problem statement identity platform consists numerous interconnected component responsible generating log output log output driven implementation logging within component others provided outofthebox managed service either case log file must readily accessible queryable persisted long period driver collation log single centralised platform utilised platform wellcome collection technical estate minimal infrastructure configuration required component utilise centralised logging platform considered aws cloudwatch elasticsearch logstash kibana elk outcome container deployed aws aws fargate wellcome collection existing elk stack utilised log pushed stack via firelens sidecar container log generating service lambda function api gateway log default aws cloudwatch configuration