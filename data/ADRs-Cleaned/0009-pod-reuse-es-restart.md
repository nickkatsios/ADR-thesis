reusing pod restarting process new configuration rejected implementation removed july favor moving towards statefulset way rolling restarts processmanager also picture dont reuse pod main benefit code architecture simplicity well respecting standard deciders cloudonks team problem statement design proposal focused best handle elasticsearch process restart inside pod catch configuration change primary case switching one license type another network configuration change example switching cluster basic license cluster gold license requires full cluster restart possible replace pod new one would data migrated pod cannot communicate others reusing persistentvolumes could solution may play well local persistent volume bound particular node node get scheduled another pod inbetween migration reusing pod may also useful situation simply restarting elasticsearch process way faster efficient replacing pod minor configuration change plugin change driver must possible perform full cluster restart reuse existing pod configuration change propagated volume mount pod spec operator client cache inconsistency must taken consideration dont restart pod time stale cache volume propagation time must taken consideration take minute restart must happen new configuration resilient operator restart considered there single outlined proposal issue contains draft algorithm implementation considered good enough dont handle full cluster restart license change reject unsupported license migration snapshot cluster create new one restore snapshot requires snapshot repository perform license upgrade stop cluster create new one reusing first one persistent volume play well local persistent volume new pod may schedulable node already full overview pod comparison expected actual able decide pod reused effectively mean changing mounted configuration restarting process actual process restart performed processmanager running elasticsearch pod listens http api authenticated request operator restart divided step stop start map different api call operator control pod restarts state machine persisted annotation pod within given state operation idempotent configuration passed secret volume mount pod avoid restarting outofdate configuration operator request process manager checksum current configuration mounted inside pod restarting process cluster orchestrated operator restarts coordinated full cluster restart performed rolling fashion configuration secret volume move away storing elasticsearch setting elasticsearchyml pod environment variable prevents reusing pod instead store elasticsearchyml file secret volume mounted elasticsearch pod secret volume configmap volume may contain secret slack email credential order creation order create pod configuration volume important approach creating secret first create secret create pod secret volume benefit volume already pod pod run immediately operator restarts inbetween step pod wasnt created yet next reconciliation create new one concern volume ownership cannot set pod since pod exist yet garbagecollect secret associated pod approach creating pod first create pod secret volume exist yet create secret benefit secret owner reference set pod automatically garbagecollected concern pod cannot immediately start enter error state volume available significantly delay pod startup time operator could restart inbetween two step secret configuration reconciliation must done every reconciliation pod creation time chosen approach first one create secret first impact startup time important detecting configuration change eligible pod reuse configuration setting compatible pod reuse license type plugins minor setting tweak arent increasing amount ram pod easily plugged existing comparison mechanism report end comparison whether expected actual match also case mismatch reuse existing pod propagate configuration change change license special may provoke full cluster restart full cluster restart required moving basic trial gold platinum enable xpack security moving trial gold platinum basic disable xpack security reconciliation loop algorithm note represent entire reconciliation loop focus piece interested get cluster spec compute expected pod spec compare expected actual compare pod spec compare actual config secret content expected config content actual config exist yet requeue stale cache comparison result return pod create pod delete attempt find match reuse pod create pod delete deterministic among multiple iteration executing algorithm twice lead match pod create pod delete pod reuse maybe create new pod check pod expectation create configuration secret create pod maybe delete deprecated pod exclude pod shard allocation check pod hold primary shard requeue delete pod delete configuration secret would garbage collected still handle pod reuse pod restarts always executed annotate pod reuse unless already annotated restartphase schedule restarting process operator reason apply human could restartphase schedulerolling restarting process one one operator would apply perform safe restart default case restartphase schedulecoordinated process full cluster restart operator would apply switch setting following license change basic gold handle pod schedule phase annotated schedule annotate restartphase stop annotated schedulerolling pod another phase stop requeue else deterministically pick best pod get started annotate restartphase stop annotated schedulecoordinated annotate restartphase stopcoordinated handle pod stop phase annotated stop disable shard allocation cluster avoids shard temporarily stopped node moved around perform sync flush fast recovery restarts request stop process manager post esstop idempotent check stopped get esstatus requeue annotate pod restartphase start annotated stopcoordinated apply step stop annotation wait process stopped instead current pod one annotate pod restartphase startcoordinated handle pod start phase annotated start pod marked reuse update configuration secret new expected configuration else well current one check config expected one reuse else current one propagated pod requesting process manager get esstatus return configuration file checksum requeue update pod label required new node type start process post esstart idempotent wait process started get esstatus enable shard allocation remove restartphase annotation pod annotated startcoordinated perform step start annotation wait process started enabling shard allocation garbagecollect useless resource configuration secret match pod existed min safe delete state machine specific reconciliation loop algorithm important note step given phase idempotent instance run step stop phase transition next step resilient stale cache pod annotated start phase perform step stop phase noop however cache cannot back time reach start phase must perform stop phase next iteration apiserver cache implementation consistency model guarantee behaviour operator restart point restart get back current phase pod reused reflected result comparison algorithm however configuration updated actually restarted might reflected anymore comparison would based new configuration yet applied process pod would require change thats process still eventually restarted correct new configuration since annotated start phase pod longer requested reuse user changed mind reverted spec previous version middle restart process still restart process depending user reverted back spec compared pod current phase state machine new config yet applied process still restarted current config new config already applied process starting well wait restart process pod reused old configuration restarted depending pod reuse choice might end reverting original configuration different pod eventually thing get back expected state naming restart annotation name elasticsearchkselasticcorestartphase restart phase schedule schedulerolling schedulecoordinated represents work preparation done operator stop stopcoordinated process process stopped start startcoordinated process process started nothing nothing done process restart extension case tbd worth implementing dont rolling restarts license switch seems easy implement reconciliation loop algorithm cover case could catch restartphase schedulerolling set user elasticsearch resource apply pod cluster would allow user request cluster restart user also apply annotation pod directly operator restart api applying annotation mechanism something stop true could allow user stop particular node misbehaves scope possible adapt reconciliation loop algorithm replace pod reuse persistent volume reuse pod eligible reuse end comparison also eligible persistent volume reuse case wed stop entire pod instead stopping process new pod would created next reconciliation iteration new config would reuse one available persistent volume choice pod reuse reuse could specified resource spec outcome chosen thats one positive consequence handle pod cluster restart rolling coordinated allows human trigger restart annotation safe cache inconsistency operator restart reconciliation retries volume propagation negative consequence implemented additional complexity extra careful chaining step right order make idempotent restart scheduled completion user modifies setting well wait current restart done link httpsgithubcomelasticcloudonksissues full cluster restart issue httpsgithubcomelasticcloudonksissues basic license support issue httpswwwelasticcoguideenelasticsearchreferencerestartupgradehtml elasticsearch full cluster restart upgrade httpswwwelasticcoguideenelasticsearchreferencerollingupgradeshtml elasticsearch rolling cluster restart upgrade