layout page title removeproducedestination deprecate ultimately remove destination deciders lewin chan aaron mcgrath paul higginson sebastien belin matt warman problem statement consider something like jmstopicproducer configure produce destination contains topic traditionally wanted metadata driven destination would done via metadatadestination messagemetadatakey expression language would configuredproducedestination everywhere however isnt necessarily obvious user additionally cannot destination isnt string producer mandatory piece information would considered destination instance aws kinesis producer requires streamname partitionkey kind requirement doesnt lend well producedestination cant make destination return delimited string since value essentially arbitrary either completely ignore producedestination destination stream name something else entirely partition key already producer ignore destination entirely sap idoc producer jetty response producer two immediately spring mind isnt mandatory edit proposal also remove consumedestination well producedestination driver confusion new user clean configuration take advantage new feature make thing predictable considered quo always deprecate producedestination introduce alternative implementation producedestination outcome deprecate remove quo army consequence good there work apart new producer dont fit existing producedestination paradigm bad arent simplifying object model configuration deprecate destination deprecate destination deprecate destination member producer consumer adaptrismessageworker well ensure producer consumer provide alternative method specifying destination fsconsumer might directoryname string messagedirectory ditto fsproducer might different producerconsumer type deprecate producerequest method main producer interface default null make sure notnull mean longer display destination create new producer configured present deprecated warning jmsreplytodestination finally special jmsreplytodestination object metadata derive javaxjmsdestination handled specially jms producer impls change jms producer implementation object metadata exists usejmsreplytoifavailabletrue jmsreplyto value deprecate jmsreplytodestination consequence neutral crossover period style valid message change existing user without massive kerfuffle good ultimately simplifies configuration leaving work configbean translation good allows producer define configuration fact nonstring based destination neutralbad change producerequest contract adaptrismessageproducer additional producedestination implementation kinesis produce could introduce new kinesisproducedestination contains additional getpartitionkey method make generic add getqualifier method consequence good arent modifying object model bad cast producedestination bad still support situation user configured configuredproducedestination similar