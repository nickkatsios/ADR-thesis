adr multi tire gas price system changelog dec initial draft rejected abstract adr describes flexible mechanism maintain consensus level gas price one choose multitier gas price system eip like one configuration currently validator configures minimalgasprices appyaml setting proper minimal gas price critical protect network attack hard validators pick sensible value propose maintain gas price consensus level since tendermint supported mempool prioritization take advantage implement sophisticated gas fee system multitier price system propose multitier price system consensus provide maximum flexibility tier constant gas price could modified occasionally governance proposal tier dynamic gas price adjusted according previous block load tier dynamic gas price adjusted according previous block load higher speed gas price higher tier bigger lower tier transaction fee charged exact gas price calculated consensus parameter schema like protobuf message tierparams uint priority priority tendermint mempool coin initialgasprice uint parentgastarget target saturation block uint changedenominator decides change speed coin mingasprice optional lower bound price adjustment coin maxgasprice optional upper bound price adjustment message params repeated tierparams tier extension allow user specify tier service transaction support extensible way add extension authinfo protobuf message extensionoptionstieredtx uint feetier value feetier index tier parameter list also change semantic existing fee field instead charging user exact fee amount treat fee cap actual amount fee charged decided dynamically fee smaller dynamic one transaction wont included current block ideally stay mempool consensus gas price drop mempool eventually prune old transaction prioritization transaction prioritized based tier higher tier higher priority within tier follow default tendermint order currently fifo aware mempool ordering logic part consensus modified malicious validator mechanism easily composed prioritization mechanism add extra tier user control example user set tier protocol create tier example ibc transaction tier usertier user selected tier transaction tier example reserve tier special transaction type example tier reserved evidence submits banksend transaction set tier delegated tier max tier level available transaction example enforce transaction specific type specific tier example tier reserved evidence transaction evidence transaction always tier mingasprices deprecate current pervalidator mingasprices configuration since would confusing work together consensus gas price adjust block load tier tier transaction gas price adjusted according previous block load logic could similar eip python def adjustgaspricegasprice parentgasused tier parentgasused tierparentgastarget return gasprice elif parentgasused tierparentgastarget gasuseddelta parentgasused tierparentgastarget gaspricedelta maxgasprice gasuseddelta tierparentgastarget tierchangespeed return gasprice gaspricedelta else gasuseddelta parentgastarget parentgasused gaspricedelta gasprice gasuseddelta parentgastarget tierchangespeed return gasprice gaspricedelta block segment reservation ideally reserve block segment tier lower tiered transaction wont completely squeezed higher tier transaction force user higher tier system degraded single tier help tendermint implement implementation make tier gas price strategy fully configurable protocol parameter providing sensible default one pseudocode pythonlike syntax python interface tieredtx def tierself int pas def txtiertx isinstancetx tieredtx return txtier else default tier custom transaction return note add rule per prioritization section class tierparams gas price strategy parameter one tier priority int priority tendermint mempool initialgasprice coin parentgastarget int changespeed decimal mean dont adjust block load class params protocol parameter tier listtierparams class state consensus state total gas last block none first block parentgasused optionalint gas price last block tier gasprices listcoin def beginblock adjust gas price tier enumerateparamstiers stateparentgasused none initialized gas price first block stategaspricesi tierinitialgasprice else adjust gas price according gas previous block stategaspricesi adjustgaspricestategaspricesi stateparentgasused tier def mempoolfeetxhandlerchecktxctx minimalgasprice configured validator zero delivertx validatorprice ctxmingasprice consensusprice stategaspricestxtiertx minprice maxvalidatorprice consensusprice zero mean infinity gas price cap txgasprice txgasprice minprice return insufficient fee return nextchecktxctx def txpriorityhandlerchecktxctx err nextchecktxctx pas priority tendermint respriority paramstierstxtiertxpriority return err def endblock update block gas stateparentgasused blockgasmeterconsumed attack protection fully saturate block prevent transaction executing attacker transaction highest tier cost would significantly higher default tier attacker spam lower tier transaction user mitigate sending higher tier transaction consequence backwards compatibility new protocol parameter new consensus state newchanged field transaction body positive default tier keep predictable gas price experience client higher tier gas price adapt block load priority conflict custom priority based transaction type since proposal occupy three priority level possibility compose different priority rule tier negative wallet tool update support new tier parameter semantic fee field changed neutral reference httpseipsethereumorgeipseip httpsiohkioenblogpostsnetworktrafficandtieredpricing