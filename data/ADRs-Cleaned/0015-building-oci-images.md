building oci image part technical story evaluate knative build related adr sourcetoimage workflow problem statement want build oci image based dockerfiles inside kubernetes cluster driver must run completely userspace privileged right required must runable kubernetes must controlled automatic manner cicd compatible knative build considered docker docker docker docker buildkit img jib buildah kaniko outcome chosen kaniko designed case work kubernetes build oci image without daemon without privileged right pro con docker docker good docker daemon already running kubernetes cluster bad would interfere kuberentes scheduling bad requires privileged mode order function significant security concern bad compatible knative build docker docker good well known approach bad requires privileged mode order function significant security concern still better docker docker bad generally incurs performance penalty quite slow bad compatible knative build buildkit github buildkit good created docker moby next generation docker build good already successfully openfaas cloud good run kubernetes without privileged right good official knative build template exists bad deamon img github img good buildkit daemonless bad special linux capability rawproc create nested container bad currently official knative build template exists nevertheless could created ourself jib github jib good fast daemonless good official knative build template exists bad designed java application buildah github buildah good popular tool creating oci container image maintained red hat also included default rhel good daemonless good official knative build template exists bad requires privileged right docker daemon rootless mode planned kaniko github kaniko good popular open source project created google good well documented easy readymade executor image gcriokanikoprojectexecutor exists good designed work kubernetes good daemonless good privileged right however requires run root inside build container good official knative build template exists bad security concern malicious dockerfiles due lack isolation issue