architecture record new rest client httptransport open source rest client across multiple team bbc called flashheart time accumulated wide range feature become difficult maintain receive request increased capability also noticeable internally extending functionality becoming problem due nature existing codebase set design new library shared across multiple team easily maintainable extended without making change coupling core project come build new library extensibility mind term code supporting featurechange request open source perspective addition trying decouple underlying http client implementation previously request built lightweight client agnostic underlying http implementation instead building feature directly core client decided abstract functionality via middlewares consequence client feature set underlying http client longer coupled core client resulted extensible flexible client example implement request collapsing without bloating client middleware system http client abstraction allowed flexible open source project number project maintain increased increase complexity release process particuarly breaking change example method signiture change httptransport would also require update callback adapter potentially simplify release process bundling middlewares default httptransport example http error conversion middleware would longer separare project