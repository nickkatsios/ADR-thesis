support amqp protocol phpamqplib consume message nonblocking way esb former driver phps native driver didnt support functionality former driver also ignored signal due inability acknowledge waiting message possible solution find way implement nonblocking consume function native driver amqp library offer support functionality like phpamqplib native driver pro faster library due native extension written already implemented application con offer support consume message nonblocking way cannot listen posix signal consuming phpamqplib pro rabbitmqs recommended library offer possibility consume message nonblocking way signal dispatched worker even consuming message offer like heartbeat channel multiple host con difficult implement correctly without bypassing interface different approach demand time learn implement decided phpamqplib initial investigation done force previous driver listen signal consuming proved impossible consume function phps native driver block execution nothing else done message arrives consumer decided worth adapt library framework greatly impacted structure consumer queue driver class designed sync protocol mind stomp case didnt fit asynchronous nature amqp prompting significant redesign interface abstraction involved ultimately drove break backwards compatibility think version framework consequence driver consume rabbitmq without blocking phps execution posix signal delivered acknowledged worker matter driver phpamqplib development dependency bundle reponse time lower amqp driver queuedriverinterface broken two accomodate different sync async driver full list change see upgrademd document metadata author brunosouza andresrey davidcamprubi people involved arthurthevenet measurement benchmark available docsarchitecturebenchmarks