adr improvement time api internal representation serialization changelog created adr time type defined tendermint provide data type time calculation better safety ergonomics prostdictated timestamp struct defined tendermintproto based google common protobuf message description concern raised type api however currently lack wellsupported library rust ecosystem would provide desirable formatting serde enforce range usable value domain type seems necessary current api time following problem newtype struct publicly exposing datetimeutc inner value provided chrono crate chrono known issue soundness security eta yet getting fixed dependency chrono trigger cargo audit failure every project tendermint library range usable value supported time explicitly defined enforced currently time allows value cant valid rfc representation whose equivalent unix timestamp value allowed google protobuf specification timestamp serde implementation time proto timestamp struct always serialize expect value string even serialization format humanreadable allow efficient binary representation arithmetic operator provided time via addsub trait implementation however result output type surprising make poor usability overloaded operator arithmetic comparison operation much slower parsed datetime structure integer timestamp representation time meant performancesensitive workload operation datetime value offsetting duration time difference time comparison internal representation optimized integer arithmetic timeasrfc conversion method named improperly regard rust naming guideline make change possibly step make inner member time struct private specify datetimes year range inclusive represented time value match restriction specified google protobuf message definition timestamp remove conversion fromto chronodatetime introducing impls instead impl tryfromtimeoffsetdatetime time fallible due additional range restriction impl fromtime timeoffsetdatetime change serde implementation tendermintprototimestamp derivingviaconversions tenderminttime memberwise struct serialization nonhumanreadable serializers remove add sub impls time replacing operator overloading checkedadd checkedsub method fashion systemtime timeoffsetdatetime provides speed bump api user must take care potential range overflow way force parenthesis appended error handling cruft nested expression tree change internal representation time unix timestamp nanosecond rename timeasrfc back timetorfc also tendermintproto public helper function named serializerstimestampasrfcnanos similarly renamed proposed consequence positive time get clear purpose documented validity range implementation detail time made private changed future little breakage api consumer interfacing ecosystem library time computation made optional enabled via featuregated conversion particular chrono completely cut localtimer issue fixed giving tendermint library consumer cargo audit peace checkedadd checkedsub method replacing arithmetic operator time conventional chainable duration arithmetic integer timestamp value fast changing internal representation unix timestamp put treatment leap second outside tendermintrs making aligned representation time tendermint protocol none rust library explicitly support google hour linear smear standard utc chrono idea representing leap second rather complex hard correctly negative breaking change api application developer prefer chrono despite fault lose convenient way convert time chronodatetime timestampbased internal representation time memoryefficient parsed time struct inconclusive performance code retrieve human time representation time timestamp affected case supported internally redesigned time api parsing formatting including serde implementation humanreadable format case added conversion overhead negligible proportion parsingformatting logic application convert time value timeoffsetdatetime potentially chronodatetime foreign crate type may become popular future value computation reference issue httpsgithubcominformalsystemstendermintrsissues httpsgithubcominformalsystemstendermintrsissues httpsgithubcominformalsystemstendermintrsissues implementation httpsgithubcominformalsystemstendermintrspull