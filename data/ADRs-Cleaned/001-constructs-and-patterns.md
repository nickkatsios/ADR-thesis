construct pattern proposed aws cdk provides component two level abstraction cfncomponents map directly cloudformation resource whilst construct higher abstraction may create multiple related resource example autoscalinggroup construct also create launchconfig securitygroup resource useful abstraction allows define component required particular concept one place various pattern available aws supported open source pattern define entire stack based around common template example ecapp pattern might provide autoscalinggroup loadbalancer required role securitygroups pattern likely composed multiple constrcuts rather cfncomponents underthehood library aim standardise simplify process setting guardian stack providing reusable component level abstraction provided position provide construct construct would give team component get sensbile guardian setting default flexibility architect stack however choose provide construct pattern providing pattern construct give team flexibility construct required also ability standup standard stack minimal effort also brings even greater standardisation allows complex feature built free library define number guardian flavoured construct extend provided aws cdk library guardian default baked example guautoscalinggroup guapplicationloadbalancer construct multiple way provide utlity class common usage example policy construct gussmpolicy gulogshippingpolicy gugetsobjectpolicy built top also provide number pattern cover common guardian stack architecture example guecapp gulambdaapp pattern pattern encouraged entry point library construct outside standard case consequence providing pattern make developer experience far quicker simpler case developer standing standard stack type maintainence viewpoint add complexity designing building maintaing pattern