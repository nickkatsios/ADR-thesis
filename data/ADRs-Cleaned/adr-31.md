jetstream direct get metadata value author ivan derekcollison alberto tbeets ripienaar implemented tag jetstream client server revision author info tbeets initial design ripienaar add multi batch behavior server motivation initial design jetstream reading message stream directly via consumer delivery thought administrative function api read routed current stream leader underlying stream store read call tracked administrative incur tracking overhead case notably key get stream materialized view desirable spread message read load multiple server accessing message store local bypass administrative api overhead feature direct get jetstream direct get feature enables stream peer stream leader respond stream read call service responder queue group responder source local message store direct get number server eligible respond read request replica count stream extended feature mirror direct get responder stream direct get enabled also upstream source mirror stream mirror peer server also participate responder queue group direct get call upstream manner message read spread many additional server mirror cluster upstream server respond direct get request upstream strategically placed client latencyreduction different geographic location serving distributed client also read availability enhanced mirror may available client upstream offline note readafterwrite coherency existing get api jsapistreammsggetstream provides readafterwrite coherency routing request stream current peer leader single server client publishes message stream ack assured subsequent call get api return message read server defines current contrast direct get assure readafterwrite coherency responder may nonleader stream server may yet applied latest consensus writes mirror downstream server yet consumed latest consensus writes upstream implementation stream property allow direct stream configuration add new allow direct boolean property allowdirect allow direct always set true server maximum message per subject maxmsgspersubject configured max limit specified user pass allow direct explicitly stream create edit request value overriden based maxmsgspersubject allow direct set automatically based inferred case stream maximum message per subject telltale stream bucket direct get api allow direct true stream server configures responder subscribes jsapidirectgetstream fixed queue group sys note allow direct false responder direct get api stream client make request receive reply message time request client may make request payload get message api populating following server struct text seq uint jsonseqomitempty lastfor string jsonlastbysubjomitempty nextfor string jsonnextbysubjomitempty batch int jsonbatchomitempty maxbytes int jsonmaxbytesomitempty starttime timetime jsonstarttimeomitempty example request payload seq number get message sequence lastbysubj string get last message subject nextbysubj string get first message lowest seq specified subject starttime string get first message newer time specified rfc format since server seq number nextbysubj string get first message seq input seq specified subject seq number batch number nextbysubj string get batch number message seq specified subject seq number batch number nextbysubj string maxbytes number limited maximum size message received byte subjectappended direct get api purpose form environment may choose apply subjectbased interest restriction user permission within account andor crossaccount exportimport grant specific subject stream may read subject stream allow direct true stream server also subscribe jsapidirectgetstream fixed queue group sys request api endpoint interpreted shortcut lastbysubj request lastbysubj derived token series token following stream name rather request payload error client call subjectappended direct get includes request payload batched request batch maxbytes key one request multiple message single api call server send multiple message without flow control reply subject send maxbytes message maxbytes unset server maxpending configuration setting server default currently batch sent zero length payload message sent natsnumpending natslastsequence header set client determine batch call needed would also header set description header eob request made server support batch first response received nothing follow old server detected absence natsnumpending header first reply multisubject request multiple subject requested manner batch requested mode support consistent point time read allowing group subject read point time assuming stream hold enough historical data help inform proper feature consumer multisubject request may allow matching subject result reply request like multilastkvusers latest value subject wildcard returned specific data user could requested multilastkvusersname kvusersaddress rather getting user data value two specific key returned facilitate consistent multi key read uptoseq uptotime key added restrict result certain point time imagine new bucket nats put user name bob message seq nats put user surname smith message seq nats put user address main street message seq nats put user address oak lane message seq update message normal multi read multilastkvusers would get address oak lane returned however get record certain point past could supply sequence time adding uptoseq request return address main street along data likewise assuming noticeable gap time changing address uptotime could form temporal querying batch parameter added restrict result set certain size otherwise server decide end batch eob marker message seen batched mode addition natsuptosequence header server cannot send data respond like batch zerolength payload message including natsnumpending natslastsequence header enabling client determine batch call needed addition would also header set description header eob natsuptosequence header set indicating last message stream matched criterion number would subsequent request uptoseq value ensure batch multigets done around consistent point time response format response may include code indicates end batch message description header would value eob request valid matching message found stream request empty invalid multi subject get match many subject error code returned header nats bad request success returned nats code direct get reply contain message along following message header natsstream stream name natssequence message sequence number natstimestamp message publish timestamp natssubject message subject natsnumpending batched number message left stream matching batch parameter natslastsequence batched stream sequence previous message natsuptosequence multi subject get sequence following request ensure consistent read regular jsonencoded nats message returned stream store example call direct get lastbysubj request text pub jsapidirectgetkvmykv inboxztubeqxiczlnaiueipqmmlzadfe lastbysubjkvmykvmykey reply text hmsg inboxztubeqxiczlnaiueipqmmlzadfe nats natsstream kvmykv natssubject kvmykvmykey natssequence natstimestamp utc hello direct get nextbysub starting seq request text pub jsapidirectgetkvmykv inboxpodfghxuaxqsjwrawoyxjczucy seq nextbysubjkvmykvmykey reply text hmsg inboxpodfghxuaxqsjwrawoyxjczucy nats natsstream kvmykv natssubject kvmykvmykey natssequence natstimestamp utc goodbye subjectappended direct get request text pub jsapidirectgetkvmykvkvmykvmykey inboxqoxafqhfzqnnqrgnplgdypxjry reply text hmsg inboxqoxafqhfzqnnqrgnplgdypxjry nats natsstream kvmykv natssubject kvmykvmykey natssequence natstimestamp utc hello illegal subjectappended direct get request text pub jsapidirectgetkvmykvkvmykvmykey inboxnogkopzkewtqhfhfiujvyoteep seq nextbysubjkvmykvmykey reply text hmsg inboxnogkopzkewtqhfhfiujvyoteep nats bad request