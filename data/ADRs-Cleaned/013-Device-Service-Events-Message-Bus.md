device service send event via message bus message bus implementation device sdk device sdk core data persistence event dto validation message envelope application service messagebus topic configuration device service messagequeue core data messagequeue application service messagebus binding secure connection consequence approved currently edgex event sent device service via http core data put event messagebus optionally persisting database adr detail device service send edgex event service via edgex messagebus note though design centered device service cross cutting impact edgex service module note adr dependent secret provider link tbd provide secret secure message bus connection message bus implementation multiple device service may publishing event messagebus concurrently zmq valid multiple device service configured publish zmq allows single publisher zmq still valid one device service publishing event mqtt redis stream valid multiple device service required support multiple publisher implementation currently available service base device service yet messagebus implementation see device sdk detail note documentation clear zmq device sdk device sdk take advantage existing gomodmessaging module enable edgex messagebus new bootstrap handler created initializes messagebus client based configuration see configuration section detail device sdk enhanced optionally publish event messagebus anywhere currently post event core data publish post controlled configuration publish default see configuration section detail device sdk device sdk implement messagebus abstraction similar one gomodmessaging first implementation type mqtt redis stream tbd abstraction allows future implementation added case warrant additional implementation sdk sdk enhanced optionally publish event messagebus anywhere currently post event core data publish post controlled configuration publish default see configuration section detail core data persistence design event sent directly application service going core data thus persisted unless change made core data allow event optionally continue persisted core data become additional secondary optional subscriber event messagebus event persisted received core data also retain ability receive event via http persist publish messagebus done today allows flexibility device service configured post event configured publish event transition device service capability publishing event future new publish approach proven may decide remove posting event core data device sdks existing persistdata setting ignored code path subscribing event since reason persist event race condition marked pushed core data persisting event received messagebus core data may finished persisting event application service processed event requested event marked pushed decided remove mark pushed capability rely time based scrubbing old event event dto development part ireland release event published messagebus event dto already implemented core data addevent api validation service receiving event dto messagebus log validation error stop processing event message envelope edgex service currently custom message envelope data published messagebus envelope wrap data metadata contenttype json cbor correlationid obsolete checksum checksum data cbor encoded identify event api mark pushed checksum longer needed event dto requires set device service always api mark event pushed message envelope updated remove property sdk recreate message envelope application service part api consumption work ireland app service sdk changed expect receive event dtos rather event model also updated longer expect checksum currently message envelope note change must occur consumption directly tied effort app service sdk enhanced secure messagebus connection described see secure connection detail messagebus topic note change recommended required design provides good opportunity adopt currently core data publishes event simple event topic application service running receive every event published whether want event filtered filterbydevicename filterbyresourcename pipeline function application service still receives every event process event extent could cause load issue deployment many device large volume event various device verbose device application service interested note current filterbydevicename good device name known statically instance device defined deviceprofilename really filterbydeviceprofilename allows multiple instance device filtered rather single instance api adding deviceprofilename event ireland filter possible pubsub system advanced topic schema take advantage application service filter event application service actual want publisher event must add deviceprofilename devicename sourcename topic form edgexeventsdeviceprofilenamedevicenamesourcename sourcename resource command name create event allows application service filter event device want subscribing deviceprofilenames specific devicenames specific sourcenames example subscribe topic schema edgexevents event core data subscribe topic schema edgexeventsrandomintegerdevice event device created randomintegerdevice device profile edgexeventsrandomintegerdevicerandomintegerdevice event randomintegerdevice device edgexeventsrandomintegerdeviceint event reading fromint device resource device created randomintegerdevice device profile edgexeventsmodbusdevicehvacvalues event reading hvacvalues device command device created modbusdevice device profile messagebus abstraction allows multiple subscription application service could specify receive data multiple specific device profile device creating multiple subscription edgexeventsrandomintegerdevice edgexeventsrandombooleandevice currently app sdk allows single subscription topic configured could easily expanded handle list subscription see configuration section detail core data existing publishing event would also changed new topic schema one challenge core data doesnt currently know deviceprofilename devicename receives cbor encoded event doesnt decode event published messagebus also core data doesnt know sourcename api enhanced change addevent endpoint event eventprofiledevicesource deviceprofilename devicename sourcename always know matter request encoded new topic approach enabled via publisher publishtopic deviceprofilename devicenameand sourcename added configured publishtopicprefix toml publishtopicprefix edgexevents added publish topic prefix see configuration section detail configuration device service device service following additional configuration allow connecting publishing messagebus describe messagebus topic section publishtopic include deviceprofilename devicename messagequeue messagequeue section added similar core data today publishtopicprefix instead topicto enable secure connection username password replaced clientauth secretpath see secure connection section detail added enabled property control whether device service publishes messagebus post core data toml messagequeue enabled true protocol tcp host localhost port type mqtt publishtopicprefix edgexevents deviceprofilenamedevicenamesourcename added publish topic prefix messagequeueoptional default mqtt specific enable environment variable override client identifier clientid device service key connection information qos quality sevice value least exactly keepalive second must greater retained false autoreconnect true connecttimeout second skipcertverify false certkey file certkey pemblock specified clientauth none valid value none usernamepassword clientcert secretpath messagebus path secret store clientauth none core data core data also require additional configuration able subscribe receive event messagebus describe messagebus topic section publishtopicprefix deviceprofilename devicename added create actual public topic messagequeue messagequeue section changed topic property change publishtopicprefix subscribeenabled subscribetopic added device service configuration username password replaced clientauth secretpath secure connection see secure connection section detail addition boolean subscribeenabled property control service subscribes event messagebus toml messagequeue protocol tcp host localhost port type mqtt publishtopicprefix edgexevents deviceprofilenamedevicenamesourcename added publish topic prefix subscribeenabled true subscribetopic edgexevents messagequeueoptional default mqtt specific enable evnironment variable override client identifier clientid edgexcoredata connection information qos quality sevice value least exactly keepalive second must greater retained false autoreconnect true connecttimeout second skipcertverify false certkey file certkey pemblock specified clientauth none valid value none usernamepassword clientcert secretpath messagebus path secret store clientauth none application service messagebus similar application service messagebus configuration change allow secure connection messagebus username password replaced clientauth secretpath secure connection see secure connection section detail toml messagebusoptional mqtt specific client identifier clientid app sevice key connection information qos quality sevice value least exactly keepalive second must greater retained false autoreconnect true connecttimeout second skipcertverify false certkey file certkey pemblock specified clientauth none valid value none usernamepassword clientcert secretpath messagebus path secret store clientauth none binding binding configuration section require change subscribe topic scheme described messagebus topic section filter event specific device profile device subscribetopic change string property containing single topic subscribetopics string property containing comma separated list topic allows flexibility property single topic wild card application service receives event today receive event randomintegerdevice randombooleandevice profile toml binding typemessagebus subscribetopicsedgexeventsrandomintegerdevice edgexeventsrandombooleandevice receive event randomintegerdevice randomintegerdevice profile toml binding typemessagebus subscribetopicsedgexeventsrandomintegerdevicerandomintegerdevice receives event toml binding typemessagebus subscribetopicsedgexevents secure connection stated earlier adr dependent secret provider alllink tbd adr provide common secret provider edgex service access secret available messagebus connection secured via following configurable client authentication mode follows similar implementation secure mqtt export secure mqtt trigger application service none authentication usernamepassword username password authentication clientcert client certificate key authentication secret specified pulled secret provider configured secretpath secret injected secret provider scope adr covered secret provider link tbd adr consequence sdk doesnt support zmq redis stream must mqtt broker running device service configured publish messagebus since weve adopted publish topic scheme deviceprofilename devicename api must restrict character device name allowed topic issue api already exists restricting allowable character rfc suffice newer zmq may allow multiple publisher requires investigation likely rework zmq implementation gomodmessaging alternative found mark push api removed core data core data client app sdk consider moving app service binding writable scope adr