from conans import python_requires, tools
import os

common = python_requires('CastleConanRecipes/[>=0.0.22-0, include_prerelease=True]@BoseCorp/master')


"""
This file is used specifically for testing on the spitfire platform
It must be located in a Tests folder
The way to run this file is by running the following commands
    1) First build the main component from the conanfile at the top level (conan install && conan build)
    2) Then export the package by running conan export-pkg
    3) Run the test command providing THIS conanfile and the full package reference of what was just created
       conan test -u <path to this conanfile> <full package reference>
       A full package reference looks something like SpitfireConanTemplate/0.0.1@user/channel
       This can also be run on a package thats already in artifactory by simply providing the package reference to that package

    ALSO NOTE: you can simply run your tests scripts by manually calling pytest when testing locally, simply run pytest <path to tests>
"""

class SpitfireTestTemplate(common.SpitfirePackage):
    def build(self):
        pass

    def requirements(self):
        pass

    def test(self):
        # Test_ids is a dictionary with three primary values
        # pr: The test plan ID from test rail, used on PRs for this component
        # integration: The test plan ID from test rail, used on INTEGRATION testing for this component. 
        #              Integration testing gets run as part of the code promotion flow via the SpitfireMetaBuild
        # system: Currently unused, but eventually may be used for even longer term testing for spitfire
        test_ids = { 'pr': 0, 'integration': 0, 'system': 0}
        
        # We need to change the directory to the on above, since in test rail paths will be from the top level
        # we do that with this line below
        with tools.chdir(os.path.join(os.path.dirname(__file__), "..")):
            # run_tests reference:
            # testrail_ids: described above
            # deploy_elf_file: Only used for local testing, typically overriden on the test server by providing the environment variable
            #                  DEPLOY_XUV_FILE=C:\xxyzz
            # create_image_script the same create image script used for the run_cmake function in the build file
            if(0): # DISABLE running this on build server, REMOVE before use in your component
                self.run_tests(testrail_ids=test_ids,
                               deploy_elf_file="TEMPLATE.elf",
                               create_image_script=os.path.join(self.python_requires["CastleConanRecipes"].exports_folder, 'Spitfire', 'SpitfireCreateFlashImage.py'))

