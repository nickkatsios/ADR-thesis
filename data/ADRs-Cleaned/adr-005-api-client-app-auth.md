geoprocessing api allow anonymous request client app creating proper publicly documented api around analyze rwd endpoint geoprocessing api analyze rwd endpoint always allowany access wed like secure via token authentication better track individual user prevent user sending many request revoke access problematic user day maybe add paid tier enforcing token authentication previously open endpoint cause problem client app client app consumes api want continue allow unauthenticated user access endpoint via app way identify client app special case app allow unrestricted request everything send client exposed app user mechanism give client app identify fairly easy uncover fake anyone trying get unchecked access api mind solution prioritize overly complicateddifficult know there truly secure solution barring rendering serverside possibility give environment client app api token keep single system api authentication easy reason bonus allow cycle client apps token someone decides start set special isclientapp flag api would check determine authentication necessary set flag wed know request client app first place preliminary check via httpreferer unsuccessful would leave via custom header part request setting xisclientapp custom header might overly naive hacky could result lot conditional logic also enforce httpreferer header expected domain google map even though header easily spoofed client outside browser theyre fairly effective browserbased apps naive nonbrowser client give client app api token setting client app api token result cleaner architecture api user token exception addition simpler mental model api token method provides well also gain added level token enforcement api user try programmatically client apps token instead well able easily cycle client apps token deincentivize one easy way cycle token managepy drfcreatetoken clientappusername always implement enhancement later client app send token geoprocessing api request whether there loggedin user token available continue user credential needed application endpoint client app get token hardcode token frontend anywhere well deploy time cycle token instead pas token client app via clientsettings server get token get token put client setting server look token authtokentoken table via client apps userid userid remain secret there programmatic way get token outside swiping client app consequence backdoor api discussed allowing client app make request without user creates backdoor api acceptable weve allowed unrestricted api access havent advertised api something could there also sensitive data available via api ideal someone could client app token make unlimited resourceintensive request unchecked least allow cycle token whenever there issue complex throttling want throttle user api client app another regular user api token would get throttled guest mmw user world would share cumalitive number request per minute fix well treat client apps token special case throttling token client app dont throttle cache number request per like anonratethrottle may difficulty related drf may load balancer instead client also may cause issue classroom user set low else cache number request per token like userratethrottle dev setup userid app server get client token fairly constant life staging production developer machine however different database instance therefore different client app userids could special email name like clientapp app server look userid get token would add level indirection would allow production staging local machine share migration creates user share code look there precedence setup azavea raster foundry airflow user store userid environment variable migration could create user write envfile would include envfile gitignore careful tamper