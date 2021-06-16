from . import (
    jupyter_lib, math_lib, templates_lib, video_lib, github_lib, utils
)


libs = {
    key: value for key, value in (
        ['jupyter_lib', jupyter_lib],
        ['math_lib', math_lib],
        ['templates_lib', templates_lib],
        ['video_lib', video_lib],
        ['github_lib', github_lib]
    )
}
