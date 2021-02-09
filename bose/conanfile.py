from conans import python_requires, tools
import os

common = python_requires('CastleConanRecipes/[>=0.0.22-0, include_prerelease=True]@BoseCorp/master')


class SpitfireMbedtls(common.SpitfirePackage):
    name = "SpitfireMbedtls"
    version = common.get_version_git_tag()
    print(f'SpitfireMbedtls version: {version}')
    scm = {
        "type": "git",
        "url": "git@github.com:BoseCorp/mbedtls.git",
        "revision": "auto"
    }

    def set_version(self):
        print('calling set_version')
        library_version = '2.16.3'
        git_hash = tools.Git().run("rev-parse --short HEAD")
        git_count = tools.Git().run("rev-list --all --count")
        self.version = "%s-%s+%s" % (library_version, git_count, git_hash)

    def init(self):
        super().init()
        # This is required so that depends.json is found
        self.setget_paths(os.path.abspath(os.path.dirname(__file__)))
        # self.paths = self.setget_paths(os.path.join(self.build_folder, 'bose'))
        # Not worry about HAL
        self.hal_required = False
        self.generate_components = False
        self.generate_subscription = False
        self.generate_version = False


    def build(self):
        print("build libmbedtls.a!!!")
        print("paths %s" %self.paths)
        # self.paths = self.setget_paths(os.path.join(self.build_folder, 'bose'))
        # print("paths %s" %self.paths)
        self.run_build(input_file='libmbedtls.a', build_xuv=False, run_stage=False, build_fs=False)


    def package_info(self):
        super().package_info()
        self.cpp_info.defines = []
