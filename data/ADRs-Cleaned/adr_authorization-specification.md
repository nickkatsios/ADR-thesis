adr authorization specification trello card deadline irrelevant since implementation pending author philipp pylipp discussion participant vahid vahidbazzaz roanna aerinsol han haguesto implementation ongoing first proposal authorization design found boxtribute application various organisation manage distribution aid good data stored contains personal confidential information individual vulnerable situation individual right privacy hence data must exposed unintended party implementation authorization measure required define enforce data excess depending current application user current document serf summary user authorization boxtribute application drive security exposure confidential data must prohibited legal ethical reason clarity make governing structure easy understand stakeholder user product management developer single source trust data controlling authorization must distributed simplicity development enforcing authorization straightforward developer guaranteeing security maintainability management role permission little overhead extensible integration dropapp boxtribute authorization boxtribute fundamental concept organisation base boxtribute partner organisation operate one site called base registered user belongs exactly one organisation one base subordinated organisation hence must granted access resource outside organisation base theyre assigned exception rule depending box transfer role role reflects user responsibility partner organisation currently role exist administrator head operation coordinator warehouse volunteer free shop volunteer library volunteer label creator god user note application administration role belong specific partner organisation permission depending user group user able perform certain action authorization concept action mirrored actionbased permission abp abps represent function application user granted abps execute example viewing inventory managing product name abp consists verb indicating action plural noun applicable separated underscore manageproducts viewinventory etc application backend however distinguished data user allowed access way achieved resourcebased permission rbp rbp refers resource database method user granted rbp execute method correspond database operation read select create insert edit update write insert update delete delete assign insert crossreference table naming convention rbp singular noun resource multiword noun concatenated underscore method name separated colon useredit beneficiarycreate tagrelationread etc every abp comprises one rbp abp managetags stand tagwrite stockread tagrelationread beneficiaryread mapping usergroup abps abp rbps listed document user management auth auth service managing user authentication authorization serf single source truth authenticated user get issued json web token jwt one two variant holding information token authentication information access token authorization information signing jwt algorithm token signed private signing key verified public signing key reason auth related adr user entity auth user registered boxtribute authorization data appmetadata stored auth database user attribute isgod god user otherwise usergroupid usergroup user belongs baseids list base user access organisationid organisation user belongs registration user manually get assigned role indicating usergroup base belong role named like basecoordinator user successfully logged custom auth postlogin action script run createdynamicpermissions script creates jwt content derived user authorization data role importantly script derives abps basespecific rbps current user see format auth permission assigned user currently effect specification custom jwt jwt access token unless specified otherwise contains standard custom field field name kind description usage standard name token issuer jwt decoding aud standard name token audience jwt decoding iat standard unix timestamp issuing datetime exp standard unix timestamp expiration datetime jwt decoding azp standard client jwt requested traceability application authentication gty standard grant type sub standard user see httpswwwboxtributecomemail custom user email httpswwwboxtributecomroles custom list user role httpswwwboxtributecombaseids custom list base user access see httpswwwboxtributecomorganisationid custom organisation user belongs see httpswwwboxtributecompermissions custom list rbps user hold access token see implementation authorization dropapp new base created following automatically created dropapp usergroups administrator created organisation created coordinator volunteer combination warehousefree shop volunteer warehouse volunteer free shop volunteer label creator auth role see role created dropapp database table usergroupsroles mapping user group role mapping user group dropapp role auth needed one user group assigned user dropapp multiple role assigned user auth user creatededited user group must assigned mapping corresponding role assigned auth user dropapp jwt since serverside application boxtribute frontend information jwt token work progress boxtribute backend user issue request backend authorization information pulled converted representation programmatically data accessed according request respective permission enforced current user decoding jwt valid request authenticated user backend contains jwt access token bearer string http authorization header url endpoint hit token extracted decoded authrequiresauth decoding routine authdecodejwt provided public key auth domain decoding fails response one following case happen token expired token audience issuer match value stored backend token decoding library fails unexpected error result response upon successful decoding jwt payload returned python dictionary representation current user current user programmatically represented authcurrentuser class readonly attribute user organisationid organisation user belongs user god user none isgod whether user god user default false baseids data structure indicating base user allowed access specific resource structure queried via currentuserauthorizedbaseids method passing rbp name timezone timezone identifier determined auth europeberlin decoded jwt payload converted currentuser instance following procedure list role custom claim contains boxtributegod attribute isgod set true organisationid custom claim copied eponymous attribute user extracted sub claim assigned isgod false permission custom claim parsed element form basexpermission permission rbp form resourcemethod result entry permission baseids multiple base given grouped basexypermission result permission order reduce payload size write edit create delete permission method implies read permission resource element basex prefix custom claim baseids form entry permission baseids example please see currentuserfromjwt enforcement rbp resolvers graphql resolvers function called graphql server resolve requested field data level resolvers allow finegrained access data resource hence suited enforce rbp every resolver must enforce rbp one way described resolvers either directly return single resource entry directly return list resource entry load one resource entry data loader enforcement rbp work differently case enforcement rbp singleresource resolver explicitly called developer authzauthorize function current user authorized access resource acc given argument function return otherwise raise exceptionsforbidden exception resulting error particular graphql field resolved current user god user function instantly return authzauthorize accepts following combination argument developer must select one suitable enforcement argument type description condition successful authorization permission string baseagnostic rbp name categoryread current user granted given permission least one base permission baseid string integer baserelated rbp name base current user granted given permission specified base permission baseids string list integer baserelated rbp name base current user granted given permission least one specified base organisationid integer organisation current user member organisation given organisationids list integer organisation current user member one organisation given userid integer user current user match given user combination argument handled function considered development error argument given function raise exception note distinguished baseagnostic box state product category size range baserelated resource box beneficiary product tag former listed baseagnosticresources authz module resource missing list assumed baserelated enforcing baserelated rbp via authorize either baseid baseids argument must provided filter applied select resource entry base user authorized achieved via authorizedbasesfiltermodel function enforces permission resource corresponding specified model hood loading resource data loader one omit enforcement rbp loader however loader batchloadfn method one authorize authorizedbaseids must called reduces permission enforcement overhead consequence