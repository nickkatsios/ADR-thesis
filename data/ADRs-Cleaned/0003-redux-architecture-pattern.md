redux architecture pattern rewrite holochain code show many implicit dependency different module stateful object conjunction complexity network agent lead level overall complexity feel much manage clean fitting architecture rust rebuild needed single global state within agent feel appropriate even balancing distributed nature network agent new holochain architecture follow redux architecture order agent one global state apply nested state object represent state tree sub state module reference counting smart pointer sub state possible module reducer decide sub state mutated reused consequence holochain refactor must fit new model state object action object module holochain agent depend state module help decoupling thus reduces code dependency also make easy timemachine debugging capability storing old state easy logging remote monitoring agent sending serialized state object monitor client processing reduxlike action module reducer might cause constant performance overhead