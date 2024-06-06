adr storage smt state commitment changelog draft draft implemented abstract sparse merkle tree smt version merkle tree various storage performance optimization adr defines separation state commitment data storage cosmos sdk transition iavl smt currently cosmos sdk iavl state commitment data storage iavl effectively become orphaned project within cosmos ecosystem proven inefficient state commitment data structure current design iavl data storage merkle tree state commitment iavl meant standalone merkelized keyvalue database however engine store tree node node stored separate record cause many inefficiency problem object query requires tree traversal root subsequent query object cached cosmos sdk level edge traversal requires query creating snapshot expensive take second export state march update iavl may trigger tree reorganization possible ologn hash recomputation become cpu bottleneck node structure pretty expensive contains standard tree node element key value left right element additional metadata height version required cosmos sdk entire node hashed hash key underlying database ref moreover iavl project lack support maintainer already see better wellestablished alternative instead optimizing iavl looking solution storage state commitment propose separate concern state commitment needed consensus state storage needed state machine finally replace iavl celestias smt celestia smt based diem called jellyfish design computeoptimised smt replacing subtrees default value single node approach ethereum implement compact proof storage model presented doesnt deal data structure serialization keyvalue database key value binary storage user responsible data serialization decouple state commitment storage separation storage commitment smt allow optimization different component according usage access pattern smt commit data compute merkle proof directly access data avoid collision separate storage namespace could database underneath store record directly mapping key value key value smt merkle tree structure dont store key directly every key value pair hashkey leaf path hash key uniformly distribute leaf tree hashvalue leaf content tree structure specified depth data access propose additional bucket implemented namespaces keyvalue pair sometimes called column family key value principal object storage state machine behind cosmos sdk kvstore interface provides direct access key allows prefix iteration backend must support hashkey key reverse index get key smt path internally smt store key value prefix hashkey hashvalue get object value composing hashkey could bucket optimize app usage needed propose database store interface allow physical backend well two separate latter allows separation different hardware unit providing support complex setup scenario improving overall performance one different backends rocksdb badger well independently tuning underlying configuration requirement state storage requirement range query quick key value access creating snapshot historical versioning pruning garbage collection state commitment requirement fast update tree path short query historical commitment proof standard pruning garbage collection smt state commitment sparse merkle tree based idea complete merkle tree intractable size assumption size tree intractable would leaf node valid data block relative tree size rendering sparse tree full specification found celestia summary smt consists binary merkle tree constructed fashion described certificate transparency rfc hashing function sha defined fips leaf internal node hashed differently onebyte prepended leaf node prepended internal node default value given leaf node empty leaf rule sufficient precompute value intermediate node root empty subtrees simplification extend default value node root empty subtrees byte zero default value rule take precedence one internal node root subtree contains exactly one nonempty leaf replaced leaf leaf node snapshot storage sync state versioning simple snapshot refer database snapshot mechanism abci snapshot sync latter referred snapshot sync directly snapshot described database snapshot view state certain time transaction full copy database would big usually snapshot mechanism based copy write allows state efficiently delivered certain stage engine support snapshotting hence propose reuse functionality state sync versioning described limit supported engine one efficiently implement snapshot final section discus evaluated one stargate core feature snapshot sync delivered snapshot package provides way trustlessly sync blockchain without repeating transaction genesis feature implemented cosmos sdk requires storage support currently iavl supported backend work streaming client snapshot certain version together header chain new database snapshot created every endblocker identified block height root store keep track available snapshot offer certain version root store implement rootstore interface described essence rootstore encapsulates committer interface committer commit setpruning getpruning function creating removing snapshot rootstorecommit function creates new snapshot increment version call check remove old version update smt interface implement committer interface note commit must called exactly per block otherwise risk going sync version number block height note cosmos sdk storage may consider splitting interface committer pruningcommitter multiroot implement pruningcommitter cache prefix store dont pruning number historical version abciqueryrequest state sync snapshot part node configuration chain configuration configuration implied blockchain consensus configuration allow specify number past block number past block modulo number past block one snapshot every block past block archival node keep past version pruning old snapshot effectively done database whenever update record smt wont update node instead creates new node update path without removing old one since snapshotting block change mechanism immediately remove orphaned node database safe operation snapshot keep track record make available accessing past version manage active snapshot either max number snapshot available remove snapshot endblocker latter done efficiently identifying snapshot block height calling store function remove past version accessing old state version one functional requirement access old state done abciqueryrequest structure version specified block height query object key block height number old version supported abciqueryrequest configurable accessing old state done available snapshot abciqueryrequest doesnt old state unless provetrue parameter set smt merkle proof must included abciqueryresponse snapshot requested version moreover cosmos sdk could provide way directly access historical state however state machine shouldnt since number snapshot configurable would lead nondeterministic execution positively validated versioning snapshot mechanism querying old state regard database evaluated state proof object stored state store corresponding object proof object identified key branch path corresponds key hashk leaf hashk rollback able process transaction rollback state update transaction fails done following way transaction processing keep state change request writes cachewrapper abstraction done today finish block processing endblocker commit root store time change written smt snapshot created committing object without saving identified usecases module save object commitment without storing object sometimes client receiving complex object way prove correctness object without knowing storage layout case would easier commit object without storing directly refactor multistore stargate store implementation storev add additional layer sdk store construction multistore structure multistore exists support modularity cosmos sdk module instance iavl current implementation instance share database latter indicates however implementation doesnt provide true modularity instead cause problem related race condition atomic commits see discussion propose reduce multistore concept sdk single instance rootstore object avoid confusion rename multistore interface rootstore rootstore following interface method configuring tracing listener omitted brevity readonly access version needed type basicrootstore interface store getkvstorestorekey kvstore cacherootstore cacherootstore main app state replacing commitmultistore type commitrootstore interface basicrootstore committer snapshotter getversionuint basicrootstore error setinitialversionuint error trace listen method replaces cachemultistore branched state type cacherootstore interface basicrootstore write trace listen method example constructor parameter concrete type type rootstoreconfig struct upgrade storeupgrades initialversion uint reserveprefixstorekey storetype contrast multistore rootstore doesnt allow dynamically mount substores provide arbitrary backing individual substores note module able special commitment example module proof state store commit proof rootstore usually single record manage specialized store privately low level interface compatibility support ease transition new interface user create shim wrap commitmultistore provides commitrootstore interface expose function safely create access underlying commitmultistore new rootstore supporting type implemented storevalpha package avoid breaking existing code merkle proof ibc currently ibc merkle proof path consists two element storekey recordkey key corresponding separate proof verified according individual spec result hash step committed value next step root commitment hash obtained root hash proof recordkey hashed storekey validate app hash compatible rootstore store record single merkle tree structure wont produce separate proof store recordkey ideally storekey component proof could omitted updated noop spec recordkey however ibc verification code hardcodes ibc prefix applies sdk proof separate element proof path isnt possible without breaking change breaking behavior would severely impact cosmos ecosystem already widely adopts ibc module requesting update ibc module across chain time consuming effort easily feasible workaround rootstore two separate smts could underlying one ibc state one everything else simple merkle map reference smts act merkle tree create final app hash merkle map stored constructed runtime ibc substore key must ibc workaround still guarantee atomic syncs proposed backends support atomic transaction efficient rollback commit phase presented workaround ibc module fully upgraded support singleelement commitment proof optimization compress module key prefix consider compression prefix key creating mapping module key integer serializing integer varint coding varint coding assures different value dont common byte prefix merkle proof cant prefix compression apply key moreover prefix compression applied module namespace precisely module namespace accessing module namespace create kvstore embedded prefix prefix compressed accessing managing assure code wont change fix mapping static variable provided app state special key todo make key compression optimization key compression object may saved key contains protobuf message type key long could save lot space map protobuf message type varints todo finalize move another adr migration new store require migration migration proposed genesis export reset blockchain history place migration reuse upgradekeepersetupgradehandler provide migration logic appupgradekeepersetupgradehandleradr funcctx sdkcontext plan upgradetypesplan moduleversionmap moduleversionmap error storevmigrateiavlstore vstore runmigrations return versionmap updated module consensusversions return appmmrunmigrationsctx migrate function read entry storev save combined store cache layer operation must finish single commit call inserting record smt component bottleneck unfortunately smt doesnt support batch transaction adding batch transaction layer considered feature main release consequence backwards compatibility adr doesnt introduce cosmos sdk level api change change storage layout state machine storage hard fork network upgrade required incorporate change smt provides merkle proof functionality however compatible updating proof compatibility required positive decoupling state state commitment introduce better engineering opportunity optimization better storage pattern performance improvement joining smt based camp wider proven adoption iavl example project decided smt ethereum diem libra trillan tezos celestia multistore removal fix longstanding issue current multistore design simplifies merkle proof module except ibc one pas merkle proof negative storage migration smt doesnt support pruning add test functionality key overhead key prefix doesnt impact key size hashed neutral deprecating iavl one core proposal cosmos whitepaper alternative design alternative design evaluated state commitment storage report ethereum research published verkle trie idea combining polynomial commitment merkle tree order reduce tree height concept good potential think early implement current smt based design could easily updated verkle trie research implement necessary library main advantage design described adr separation state commitment data storage designing powerful interface discussion evaluated database verified existing database database evaluating snapshot support following database provide efficient snapshot mechanism badger rocksdb pebble database dont provide support production ready boltdb leveldb goleveldb membdb lmdb rdbms rdbms instead simple store state rdbms require cosmos sdk api breaking change kvstore interface allow better data extraction indexing solution instead saving object single blob byte could save record table state storage layer hashkey protobufobject smt outlined verify object registered rdbms one committed smt one load rdbms marshal protobuf hash smt search chain store discussing case module support database automatically committed module responsible sound storage model optionally feature discussed committing object without saving section reference iavl whats next iavl overview state state commitment storage report celestia lazyledger smt facebook diem libra smt design trillian revocation transparency trillian verifiable data structure design implementation discussion upgrade ibc chain client adr effect ibc