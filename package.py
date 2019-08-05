late = locals()["late"]
name = "bleed"
version = "1.0.16"
build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

_requires = [
    "~blender==2.80.0",
    "~maya==2015.0.0|2016.0.2|2017.0.4|2018.0.6|2019.0.3",

    "python-3",
    "pyqt5-5.8",
    "pyblish_qml",
    "pyblish_base-1.5.3",

    "pymongo-3.4+",
    "avalon_colorbleed-1",
    "avalon_core-5.2+",
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

                # Provided by the Allzpark demo packages
                "mgear",
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

    if os.name == "nt":
        env["PYBLISH_QML_PYTHON_EXECUTABLE"] = "{env.REZ_PYTHON_ROOT}/app/python.exe"
        env["PYBLISH_QML_PYQT5"] = "{env.REZ_PYQT5_ROOT}/python"

    if "maya" in request:
        env["PYTHONPATH"].append("{root}/maya")  # userSetup.py

    # We'll need to make these non-required
    env["AVALON_ASSET"] = "hero"
    env["AVALON_SILO"] = "asset"
    env["AVALON_WORKDIR"] = tempfile.gettempdir()
    env["AVALON_TASK"] = "modeling"
