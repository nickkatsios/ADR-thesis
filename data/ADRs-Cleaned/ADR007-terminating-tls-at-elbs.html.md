title adr terminating elbs adr terminating elbs needed decide terminate connection public tenant facing endpoint manage corresponding private key previously decided support http deployed application cloud foundry endpoint time writing endpoint consider deployed application gorouter accessed public api accessed tenant uaa accessed tenant loggregator accessed tenant ssh proxy theory accessed tenant working environment existing credential store suitable storing private key rest small number engineer within team access one make iam change accountwide terraform config placing elbs front publicfacing service architectural pattern advised amazon order reduce attack surface specifically advise help withstand volumetric denial service attack elb handle tcp connection therefore responsibility handling ddos layer resides elb team spike attempted place everything publicfacing tenantfacing behind elbs found http mode elbs support web socket known break loggregator relies log streaming would also prevent tenant web socket within application elb tcp mode way communicating client address downstream service practical consequence would tenant would unable see log service access control based client address attempting solve second problem explored elb support proxy protocol unfortunately none downstream service gorouter support seemed simple add support gorouter could introduce another intermediary proxy haproxy understands proxy protocol add appends xforwardedfor header client address provided via proxy protocol decided elb terminate elb tcp mode submit proxy protocol support gorouter logging ensure address client endpoint consequence played spike investigate setting xforwardedfor correctly produced upstream add proxy protocol support gorouter another introduce xforwardedproto header interim measure gorouter gained support added intermediate haproxy introduce xforwardedfor xforwardedproto header