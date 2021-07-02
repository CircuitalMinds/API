from python_resources import libs, utils


class HandlerResources:
    repositories_path = '../'
    libs = utils.get_info_resources(
        path='./python_resources/info.json', lib_names=list(libs.keys()), save_file=True
    )

    def git_app(self, function_name):
        git = libs['github_lib'].git(self.repositories_path)
        return dict(
            commit=git.commit,
            push=git.push,
            info=git.repositories
        )[function_name]

    def video_app(self):
        return libs['video_lib'].__dict__['video_containers'](path='../music_containers')

    @staticmethod
    def math_tools(name):
        tools = libs['math_lib'].__dict__[name]()
        return dict(
            plotter=tools.grapchic_lab,
            numerical_approximations=tools.fourier_analysis,
            simulations=tools.fractal_simulations
        )
handler = HandlerResources()
git = handler.git_app(function_name='info')
video_containers = handler.video_app()
get_sizes = video_containers.get_file_sizes

for repo in git.keys():
    if 'music_' in repo:
        print(repo)
        print(get_sizes(id=repo.split('_')[-1]))
