monorepo directory layout following want follow tenet screaming architecture stating first level directory application source tree represent case feature application however cannot define domain module inside application directory domain cannot mapped application feature since domain independent application practical term mean could happen two different feature domain module domain module defined feature feature requires domain concept well feature know feature even make sense far semantic feature concerned additionally cannot define adapter infrastructure code inside feature directory either application cannot know adapter often adapter target multiple feature like web adapter target different feature primary port even secondary adapter could target different feature act like mediator example command event currently one source code repository dont want hassle maintaining multiple repository yet project structure still actively changed top want support plugin architecture multiple different kind application built assembling together plugins exactly purpose clean architecture maybe difference typical example clean architecture web application there one application supporting different feature well different application possibly built component however deploying detail avoid dealing multiple source code repository well monorepo approach meaning keeping everything inside single source code repository far directory structure concerned project bit unusual since many different application well built assembling different plugins instead one possible application mean cannot really display application case first level directory tree application plugins located instead slothmachineframework domain smf slothmachinearchitecture domain sma virtualmachine application architectureloader application arcl programloader application localarchitectureloader adapter larcl fileprogramloader adapter fpl slothmachine adapter slothmachineframework slothmachinearchitecture virtualmachine architectureloader programloader localarchitectureloader fileprogramloader argue directory layout still quite screaming displaying feature application better say toolkit since multiple application virtual machine assembler compiler debugger etc state clearly whats purpose system interesting point additionally two different kind plugins first one belong plugins added development application theyre necessary structure like slothmachinecore feature one second kind plugins instead contains mod added already deployed application example dropping specific directory enhance functionality virtual machine without necessary structure example virtual machine support many different architecture end user virtual machine application installed system could add new architecture dropping appropriate plugin archive correct folder application pick new architecture startup handy dont want require building releasing new version application add new architecture new supported assembler compiler reference httpsblogcleancodercomunclebobthecleanarchitecturehtml httpsblogcleancodercomunclebobscreamingarchitecturehtml httpstrunkbaseddevelopmentcommonorepos httpwwwplainionistnetimplementingcleanarchitecturescream httpsnewsycombinatorcomitemid httpsmediumcommattkleinmonorepospleasedonteabeb httpsmediumcomadamhjkmonorepopleasedoeab proposed consequence application clearly state intent listing feature case application module still clearly categorized layer thus abstraction level build system must able support dependency located different directory instead everything located single lib vendor