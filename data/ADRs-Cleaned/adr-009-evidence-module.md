adr evidence module changelog july initial draft october initial implementation order support building highly secure robust interoperable blockchain application vital cosmos sdk expose mechanism arbitrary evidence submitted evaluated verified resulting agreed upon penalty misbehavior committed validator equivocation doublevoting signing unbonded signing incorrect state transition future etc furthermore mechanism paramount ibc crosschain validation protocol implementation order support ability misbehavior relayed back collateralized chain primary chain equivocating validators slashed implement evidence module cosmos sdk supporting following functionality provide developer abstraction interface necessary define custom evidence message message handler method slash penalize accordingly misbehavior support ability route evidence message handler module determine validity submitted misbehavior support ability governance modify slashing penalty evidence type querier implementation support querying params evidence type params submitted valid misbehavior type first define evidence interface type xevidence module may implement type many chain counterfactualevidence addition module may implement evidence type similar manner governance extensible important note concrete type implementing evidence interface may include arbitrary field infraction time want evidence type remain flexible possible submitting evidence xevidence module concrete type must provide validators consensus address known xslashing module assuming infraction valid height infraction occurred validators power height infraction occurred type evidence interface route string type string string string hash hexbytes validatebasic error consensus address malicious validator time infraction getconsensusaddress consaddress height infraction occurred getheight int total power malicious validator time infraction getvalidatorpower int total validator set power time infraction gettotalpower int routing handling evidence type must map specific unique route registered xevidence module accomplishes router implementation type router interface addrouter string handler router hasrouter string bool getroutepath string handler seal upon successful routing xevidence module evidence type passed handler handler responsible executing corresponding business logic necessary verifying evidence valid addition handler may execute necessary slashing potential jailing since slashing fraction typically result form static function allow handler provides greatest flexibility example could evidencegetvalidatorpower onchain parameter controlled governance evidence type provide external information necessary order handler make necessary state transition error returned evidence considered valid type handler funccontext evidence error submission evidence submitted msgsubmitevidence message type internally handled xevidence module submitevidence type msgsubmitevidence struct evidence func handlemsgsubmitevidencectx keeper keeper msg msgsubmitevidence result err keepersubmitevidencectx msgevidence err nil return errresult emit event return result xevidence module keeper responsible matching evidence module router invoking corresponding handler may include slashing jailing validator upon success submitted evidence persisted func keeper submitevidencectx evidence evidence error handler keeperroutergetrouteevidenceroute err handlerctx evidence err nil return errinvalidevidencekeepercodespace err keepersetevidencectx evidence return nil genesis finally represent genesis state xevidence module module list submitted valid infraction necessary params module order handle submitted evidence xevidence module naturally define route native evidence type itll likely slashing penalty constant type genesisstate struct params params infraction evidence consequence positive allows state machine process misbehavior submitted onchain penalize validators based agreed upon slashing parameter allows evidence type defined handled module allows slashing jailing defined complex mechanism solely rely tendermint submit evidence negative easy way introduce new evidence type governance live chain due inability introduce new evidence type corresponding handler neutral persist infraction indefinitely rather rely event reference ibc architecture tendermint fork accountability