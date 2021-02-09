#!/usr/bin/env groovy

@Library(['JenkinsSharedLibrary']) _

import JenkinsConan
def conan = new JenkinsConan(this)

//PARAMS
String[] profiles = ["spitfire"]
String compile_label = "spitfire-container" 
String buildTimeout = '120'
String remote = 'spitfire'

Map config = [
    profiles: profiles
]

conanBuildPipelineMapParams( conan, compile_label, config, buildTimeout, remote)
