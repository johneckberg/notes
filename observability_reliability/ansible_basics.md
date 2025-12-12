# Ansible Basics

## What is Ansible?

Ansible is an open-source automation tool used for IT tasks like configuration management, application deployment, and orchestration. Ansible allows users to define automation tasks in a human-readable format (YAML) called playbooks, which can be executed across multiple systems.

## Definitions in context

Playbooks contain Plays; the terms ‘playbook’ and ‘play’ are sports analogies. Playbooks are expressed in YAML format. Each play executes part of the overall goal of the playbook, running one or more tasks. Plays map hosts to tasks. Each task calls an Ansible module. A module is a plugin/script that follows certain Ansible input/output specs. Ansible modules should follow idempotency principles, which means that consecutive runs of the same module should have the same effect if nothing else changes. Modules return data structures in JSON data.

## Playbook example

A playbook runs in order from top to bottom. Within each play, tasks also run in order from top to bottom. Playbooks with multiple plays can orchestrate multimachine deployments, running one play on your webservers, another play on your database servers, and a third play on your network infrastructure. In the following example (taken from red hat), the first play targets the web servers and the second play targets the database servers.
~~~
- name: Update web servers
  hosts: webservers
  remote_user: root

  tasks:
  - name: Ensure apache is at the latest version
    ansible.builtin.yum:
      name: httpd
      state: latest

  - name: Write the apache config file
    ansible.builtin.template:
      src: /srv/httpd.j2
      dest: /etc/httpd.conf

- name: Update db servers
  hosts: databases
  remote_user: root

  tasks:
  - name: Ensure postgresql is at the latest version
    ansible.builtin.yum:
      name: postgresql
      state: latest

  - name: Ensure that postgresql is started
    ansible.builtin.service:
      name: postgresql
      state: started`
~~~

Note that playbooks can include more than just a hosts line and tasks. For example, the playbook above sets a remote_user for each play. The remote_user is the user account for the SSH connection.