split inventory perproject file lot different way manage inventory ansible consistent way match pattern want make projectspecific inventory easy manage find various development group also want make easy run infrastructure update across class vms stagingproductionqa machine possibly apachenginxdrupal machine want make maintenance management easier inventory alphabetization helpful clue built finally want make harder run playbook many wrong vms mistake reducing host delete flat host file create inventory directory directory contain multiple subdirectory including allprojects directory containing separate file project file must include necessary inventory group example figgyproduction figgyworkers figgywebproduction file directory match subdirectory groupvars directory byenvironment directory containing file environment production staging file contain group made child group projectspecific file directory allow different method grouping inventory web server type example nginx apache note allprojects directory must first directory listed word alphabetically linuxascii alphabetization must come first ansible load inventory ascii order must child group file allprojects loaded create parent group byenvironment consequence make finding group vms inventory easier lot inventory file appear multiple group existing group still work stop risky host playbook