dynamodb stream enqueuer partially superseeds adr proposer trestini deciders trestini problem statement adr state main purpose dynamodb hold historical data must state holder particular schedule ready delayer queue however state changed new processed exactly schedule posted delayer queue proposal aim change behavior removing record already delayer queue instead change processed driver cost able deal thousand schedule way increase provisioned capacity dynamodb hundred thousand even million record acceptable thousand considered move solution based ttl dynamo stream pro con move solution based ttl dynamo stream good increase performance reduces cost bad add complexity notsoobvious solution outcome chosen move solution based dynamo stream proposed solution doesnt ttl since according aws doc deletion expired record occurs within hour case acceptable solution based fact record generates event dynamodb consumed lambda function sense new schedule deleted delete event raised function schedule proper pointintime hand schedule placed within delayer period timeframe event waiting delayer queue function deletes record generates another delete handled schedule delayer period stored taskminuteenqueuer find deletes record hey apischedulepost dont simply put que delayer queue directly short answer lambda top data transformation lambda restrict apischedulepost function responsible handle post request api gateway handle transform data store somewhere reason exists function information processed later concern mind stage development keep integrity design important fine performance tunning new role involved lambda taskminuteenqueuer function still triggered cloudwatch event simply deletes record entered delayer period streamdynamodbfasttrackenqueuer send record raised delete event sqs queue event insert delayer period deletes record positive consequence keep entire architecture design push based important serverless architecture style keep integrity flow lambda sends record sqs lambda insert record dynamodb event push record sqs always negative consequence still keep increased writes dynamodb delete dynamo count write operation link refers adr