model assembler hateoas response deciders quantil enpro team problem statement spring hateoas includes several class encapsulate domain object adding support link constructing object well adding desired link common operation requires entityspecific boilerplate code duplicate code nearly controller method avoided driver avoid duplicate code create hateoas model decouple link creation normal entity logic considered make link part entity object inheritance separate model assembler class outcome separate model assembler chosen former would require deep coupling hateoas type dto class due assembler class initially link reside linkassembler package pro con make link part entity object inheritance good easy implement bad deep coupling spring hateoas internals type separate model assembler class good clear separation concern bad complex implementation especially call site kept short