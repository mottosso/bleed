late = locals()["late"]
name = "bleed"
version = "1.0.14"
build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

_requires = [
    "global",

    "~blender==2.80.0",
    "~maya==2015.0.0|2016.0.2|2017.0.4|2018.0.6",

    "python-3",
    "pyqt5-5.8",
    "pymongo-3.4+",
    "colorbleed-1",
    "avalon-5.2+",
]


@late()
def requires():
    global this
    global request
    global in_context

    requires = this._requires

    # Add request-specific requirements
    if in_context():
        if "maya" in request:
            requires += [
                "ffmpeg",
            ]

    return requires


def commands():
    import os
    import tempfile

    global env
    global this
    global request

    # Better suited for a global/studio package
    projects = r"p:\projects" if os.name == "nt" else "~/projects"

    env["AVALON_PROJECTS"] = projects
    env["AVALON_CONFIG"] = "colorbleed"
    env["AVALON_PROJECT"] = this.name
    env["AVALON_EARLY_ADOPTER"] = "yes"

    if "maya" in request:
        env["PYTHONPATH"].append("{root}/maya")  # userSetup.py

    # We'll need to make these non-required
    env["AVALON_ASSET"] = "hero"
    env["AVALON_SILO"] = "asset"
    env["AVALON_WORKDIR"] = tempfile.gettempdir()
    env["AVALON_TASK"] = "modeling"
