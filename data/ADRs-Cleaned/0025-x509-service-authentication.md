support based service authentication currently implemented one flow want access service bind service application create service key creates vcap env variable entry including clientid clientsecret information ask xsuaa issue token access service different grant type available token clientgrant usergrant change slightly want certificate secret request token xsuaa per default xsuaa accepts authentication type configure security descriptor json json xsappname somename oauthconfiguration credentialtypes bindingsecret bind service create service key usual createservicekey myservice myservicekey parametersjson parametersjson json credentialtype keylength validity validitytype day want support multiple credentialtypes create multiple service key binding lead certificate key property vcap service variable add certificate http client mtls making call xsuaa instead clientsecret payload xsuaa return token access desired service advantage first glance seems like one string service key json apiurl httpsapiauthenticationsaphanaondemandcom clientid someid clientsecret somesecret credentialtype instancesecret replaced another string certificate key json apiurl httpsapiauthenticationsaphanaondemandcom certificate begin certificateend certificatenbegin certificateend certificatenbegin certificateend certificaten clientid someid credentialtype key begin rsa private keyend rsa private keyn however certificate based approach advantage secret part http traffic layer customer switch http trace see secret log lifetime certificate set even token retrieval old stolen secret disadvantage still investigating detail afraid higher support load assume following flow customer creates new application sdk bind xsuaa destination service application per default credentialstype xsuaa manages certificate everything work fine initially day certificate expires support request sdk throw error course configure duration certificate validity seems limited maximum one year rollout compatibility existing binding service key nothing change xsuaa accept service like destination connectivity note service key credentialtype clientsecret property current state sdk fail case sdk relevant service like xsuaa destination connectivity support rolled internally self managed certificate discussed xsuaa managed flow know case certificate created xsuaa also possible bring certificate create service key json credentialtype certificate begin certificateend certificate ensureuniqueness false certificatepinning true case key property part vcap service variable bring outside selfmanaged certificate find secure way customer pas private part certificate application first version considered implementation easy security question extend current code could extend current code support authentication would require current change ensure right service credential found vcap already case investigate credentialtype instancesecret depending value http client certificate clientsecret get token note xsuaa endpoint different httpsauthenticationcertoauthtoken clientsecret httpsauthenticationoauthtoken change token retrieval xssec library would following replace existing call lib ensure right service credential found vcap already case lib take care evaluation type service key comparison versus winner library futureproof thing come also security point view xssec homemade implementation consequence sdk support token retrieval via credentialtype