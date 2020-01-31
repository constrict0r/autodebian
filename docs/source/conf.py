# Configuration file for the Sphinx documentation builder.

import os
import sys

project = "autodebian"
copyright = "2019, constrict0r"
author = "constrict0r"
version = "0.0.1"
release = "0.0.1"

sys.path.insert(0, os.path.abspath("../.."))

extensions = [
    "sphinxcontrib.restbuilder",
    "sphinxcontrib.globalsubs",
    "sphinx-prompt",
    "sphinx_substitution_extensions"
]

templates_path = ["_templates"]

exclude_patterns = []

html_static_path = ["_static"]

html_theme = "sphinx_rtd_theme"

master_doc = "index"

master_doc = "index"

img_base_url = "https://gitlab.com/" + author + "/img/raw/master/"
img_url = img_base_url + project + "/"

author_img = ".. image:: " + img_url + "author.png\n   :alt: author"
author_slogan = "The travelling vaudeville villain."

github_base_url = "https://github.com/"
github_url = github_base_url + author + "/" + project
github_link = "`Github <" + github_url + ">`_."

gitlab_base_url = "https://gitlab.com/"
gitlab_url = gitlab_base_url + author + "/" + project
gitlab_badge = gitlab_url + "/badges/master/pipeline.svg\n   :alt: pipeline"
gitlab_ci_url = gitlab_url + "/pipelines"
gitlab_ci_link = "`Gitlab CI <" + gitlab_ci_url + ">`_."
gitlab_link = "`Gitlab <" + gitlab_url + ">`_."

travis_base_url = "https://travis-ci.com/"
travis_url = travis_base_url + author + "/" + project
travis_badge = ".. image:: " + travis_url + ".svg\n   :alt: travis"
travis_ci_url = travis_url
travis_link = "`Travis CI <" + travis_url + ">`_."

readthedocs_url = "https://" + project + ".readthedocs.io"
readthedocs_badge = "/projects/" + project + "/badge\n   :alt: readthedocs"
readthedocs_link = "`Readthedocs <" + readthedocs_url + ">`_."

global_substitutions = {
    "AUTHOR_IMG": author_img,
    "AUTHOR_SLOGAN": author_slogan,
    "AVATAR_IMG": ".. image:: " + img_url + project + ".png\n   :alt: "
    + project,
    "DEPLOYMENT_IMG": ".. image:: " + img_url +
    "/deployment.png\n   :alt: deployment",
    "DOOMBOTS_IMG": ".. image:: " + img_url +
    "/doombots.png\n   :alt: doombots",
    "ENJOY_IMG": ".. image:: " + img_url + "/enjoy.png\n   :alt: enjoy",
    "GITHUB_LINK":  github_link,
    "GITLAB_LINK":  gitlab_link,
    "INGREDIENTS_IMG": ".. image:: " + img_url +
    "/ingredients.png\n   :alt: ingredients",
    "PROJECT": project,
    "READTHEDOCS_BADGE": ".. image:: https://rtfd.io" + readthedocs_badge,
    "READTHEDOCS_LINK": readthedocs_link,
    "APTITUDE_IMG": ".. image:: " + img_url +
    "/aptitude.png\n   :alt: aptitude",
    "BASIK_IMG": ".. image:: " + img_url +
    "/basik.png\n   :alt: basik",
    "CONSTRUCTOR_IMG": ".. image:: " + img_url +
    "/constructor.png\n   :alt: basik",
    "DESKTOP_IMG": ".. image:: " + img_url +
    "/desktop.png\n   :alt: desktop",
    "DEVELBASE_IMG": ".. image:: " + img_url +
    "/develbase.png\n   :alt: develbase",
    "DEVELMICRO_IMG": ".. image:: " + img_url +
    "/develmicro.png\n   :alt: develmicro",
    "DEVELPY_IMG": ".. image:: " + img_url +
    "/develpy.png\n   :alt: develpy",
    "DEVELS_IMG": ".. image:: " + img_url +
    "/devels.png\n   :alt: devels",
    "DEVELVIRT_IMG": ".. image:: " + img_url +
    "/develvirt.png\n   :alt: develvirt",
    "GROUPS_IMG": ".. image:: " + img_url +
    "/groups.png\n   :alt: groups",
    "HOME_IMG": ".. image:: " + img_url +
    "/home.png\n   :alt: home",
    "ISO_IMG": ".. image:: " + img_url +
    "/iso.png\n   :alt: iso",
    "JSNODE_IMG": ".. image:: " + img_url +
    "/jsnode.png\n   :alt: jsnode",
    "KICK_IMG": ".. image:: " + img_url +
    "/kick.png\n   :alt: kick",
    "LATVERIA_IMG": ".. image:: " + img_url +
    "/latveria.png\n   :alt: latveria",
    "MADVILLAIN_IMG": ".. image:: " + img_url +
    "/madvillain.png\n   :alt: madvillain",
    "PYP_IMG": ".. image:: " + img_url +
    "/pyp.png\n   :alt: pyp",
    "SERVICEZ_IMG": ".. image:: " + img_url +
    "/servicez.png\n   :alt: servicez",
    "SOURCEZ_IMG": ".. image:: " + img_url +
    "/sourcez.png\n   :alt: sourcez",
    "SYSCONFIG_IMG": ".. image:: " + img_url +
    "/sysconfig.png\n   :alt: sysconfig",
    "TASK_IMG": ".. image:: " + img_url +
    "/task.png\n   :alt: task",
    "UNIFY_IMG": ".. image:: " + img_url +
    "/unify.png\n   :alt: unify",
    "UPGRADE_IMG": ".. image:: " + img_url +
    "/upgrade.png\n   :alt: upgrade",
    "USERCONFIG_IMG": ".. image:: " + img_url +
    "/userconfig.png\n   :alt: userconfig",
    "USERS_IMG": ".. image:: " + img_url +
    "/users.png\n   :alt: users"
}

substitutions = [
    ("|AUTHOR|", author),
    ("|PROJECT|", project)
]
