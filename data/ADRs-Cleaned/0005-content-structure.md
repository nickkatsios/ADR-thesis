content structure proposed consistent welldefined document specification required may develop api contract structure closely follows jsonapi document structure document root level root level always json object must contain least one following rootlevel member data document primary data resource object single resource object represented json object collection resource object represented array object error array error object single resource object json data meta collection resource object json data error meta link jsonapi state member data error must coexist document opgdata standard data resource object returned must error member however certain circumstance array error may returned alongside data resource collection see errorhandlingandstatuscodesmderrorsinx root json object may also contain following rootlevel member meta meta object contains nonstandard metainformation link link object related primary data typically pagination link data returned collection resource object see jsonap namely minimum every resource object must contain member type member value type member must string consistency avoidance confusion type must plural article people array attribute even empty data top level member present must link array containing minimum self member url must callable api resource object data attribute presented array named attribute resource object link presented object named link resource object relationship presented array named relationship resource object attribute relationship collectively called field json data type article attribute title first article description link self httpsapiexamplecomarticles next httpsapiexamplecomarticles relationship type article attribute title second article description link self httpsapiexamplecomarticles prev httpsapiexamplecomarticles relationship link meta relationship relationship defined separate adr meta see jsonapi error error response defined separate adr consequence consistent welldefined specification