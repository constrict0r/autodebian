Ansible role to use as a wrapper for npm to install nodejs packages.

This role performs the following actions:

- Ensure the requirements are installed.

- Ensure the current user can obtain administrative (root) permissions.

- If not already added, add the nodejs repository to the apt sources.

- If not installed, install nodejs.

- If the **packages_npm** variable is defined, install the npm packages listed
  on it.

- If the **configuration** variable is defined, install the npm packages listed
  on it.
