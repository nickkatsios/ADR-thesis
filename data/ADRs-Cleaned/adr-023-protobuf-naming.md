adr protocol buffer naming versioning convention changelog april initial draft august update guideline protocol buffer provide basic style guide buf build upon extent possible want follow industry guideline wisdom effective usage protobuf deviating clear rationale case adoption adoption googleprotobufany recommended approach encoding interface type opposed oneof make package naming central part encoding fullyqualified message name appear encoded message current directory organization thus far mostly followed bufs default recommendation minor deviation disabling packagedirectorymatch although convenient developing code come warning buf bad time many protobuf plugins across various language adoption grpc query adr grpc adopted protobuf native query full grpc service path thus becomes key part abci query path future grpc query may allowed within persistent script technology cosmwasm query route would stored within script binary goal adr provide thoughtful naming convention encourage good user experience user interact directly proto file fullyqualified protobuf name balance conciseness possibility either overoptimizing making name short cryptic underoptimizing accepting bloated name lot redundant information guideline meant act style guide cosmos sdk thirdparty module starting point adopt default checker bufs including packagedirectorymatch except packageversionsuffix servicesuffix guideline described principle concise descriptive name name descriptive enough convey meaning distinguish name given fullyqualifed name within googleprotobufany well within grpc query route aim keep name concise without going overboard general rule thumb shorter name would convey else thing pick shorter name instance cosmosbankmsgsend byte conveys roughly information cosmossdkxbankvmsgsend byte concise conciseness make name pleasant work take space within transaction wire also resist temptation overoptimize making name cryptically short abbreviation instance shouldnt try reduce cosmosbankmsgsend csmbkmsnd save byte goal make name concise cryptic name client first package type name chosen benefit user necessarily legacy concern related codebase plan longevity interest longterm support plan name choose usage long time opportunity make best choice future versioning guideline stable package version general schema evolution way update protobuf schema mean new field message rpc method added existing schema old field message rpc method maintained long possible breaking thing often unacceptable blockchain scenario instance immutable smart contract may depend certain data schema host chain host chain break schema smart contract may irreparably broken even thing fixed instance client software often come high cost instead breaking thing make every effort evolve schema rather breaking buf breaking change detection stable nonalpha beta package prevent breakage mind different stable version package considered different package last resort approach upgrading protobuf schema scenario creating may make sense want create new module similar functionality existing module adding natural way case really two different similar module different apis want add new revamped api existing module cumbersome add existing package putting cleaner user case care made deprecate support actively immutable smart contract guideline unstable alpha beta package version following guideline recommended marking package alpha beta marking something alpha beta last resort putting something stable package preferred package marked alpha active discussion remove significantly alter package near future package marked beta active discussion significantly refactorrework functionality near future remove module type stable unstable alpha beta package alpha beta avoid responsibility maintaining compatibility whenever code released wild especially blockchain high cost changing thing case instance immutable smart contract breaking change may impossible fix marking something alpha beta maintainer ask question cost asking others change code benefit maintaining optionality change plan moving affect user alpha beta really communicate change planned case study grpc reflection package grpcreflectionvalpha hasnt changed since widely software like grpcurl folk probably production service actually went changed package grpcreflectionv software would break probably dont want valpha package defacto let following guideline working nonstable package bufs recommended version suffix valpha nonstable package nonstable package generally excluded breaking change detection immutable smart contract module cosmwasm block smart contractspersistent script interacting alphabeta package omit suffix instead bufs recommended version suffix omit package dont actually second version allows concise name common case like cosmosbanksend package second third version indicate package naming adopt short unique toplevel package name toplevel package adopt short name known collide name common usage within cosmos ecosystem near future registry created reserve index toplevel package name within cosmos ecosystem cosmos sdk intended provide toplevel type cosmos project toplevel package name cosmos recommended usage within cosmos sdk instead longer cosmossdk specification could consider short toplevel package like based upon standard number limit subpackage depth subpackage depth increased caution generally single subpackage needed module library even though module source code denote module often unnecessary proto file module primary thing subpackages item known infrequently deep subpackage depth cosmos sdk recommended simply write cosmosbank cosmosgov etc rather cosmosxbank practice nonmodule type straight cosmos package introduce cosmosbase package needed note naming change package name cosmosbank protobuf package still live xbank message naming message type name concise possible without losing clarity sdkmsg type transaction retain msg prefix provides helpful service rpc naming adr specifies module implement grpc query service consider principle conciseness query service rpc name may called persistent script module cosmwasm also user may query path tool like grpcurl example shorten cosmossdkxbankvqueryservicequerybalance cosmosbankquerybalance without losing much useful information rpc request response type follow servicenamemethodnamerequest servicenamemethodnameresponse naming convention rpc method named balance query service request response type would querybalancerequest querybalanceresponse selfexplanatory balancerequest balanceresponse query query service instead bufs default service suffix recommendation simply shorter query query service type grpc service consider sticking bufs default recommendation omit get query query service rpc name get query omitted query service name redundant fullyqualified name instance cosmosbankqueryquerybalance say query twice without new information future improvement registry toplevel package name created coordinate naming across ecosystem prevent collision also help developer discover useful schema simple starting point would git repository communitybased governance consequence positive name concise easier read type transaction shorter sdkx removed proto file import standard without thirdpartyproto path code generation easier client proto file single proto directory copied rather scattered throughout cosmos sdk negative neutral proto file reorganized refactored module may marked alpha beta reference