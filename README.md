# infrastructure-deploy

The idea of the project is to create full-stack exampleproject to share with community knowledge and vision how can be CI infrastructure be developt (from scratch) for medium/big size open/closed/hybrid source projects.

Our vision of good CI-infrastructure or the values of our project:
- Invest now to have provit in the long-term
- Infrastructure as a service
- Flexibility to change
- Easy to support
- Modularity of infrastructure. Each part of our CI-project can be changed with another "block" with no ir minimal investment.
- Python as one and only language
- Maximum re-use of public supported tools and frameworks


## Table of analyzed and used software

<table class="tg">
<tbody>
<tr>
<th class="tg-0pky">Domain</th>
<th class="tg-0pky">Product</th>
<th class="tg-0pky">Pros</th>
<th class="tg-0pky">Cons</th>
<th class="tg-0pky">Comment</th>
</tr>
<tr>
<td class="tg-0pky" rowspan="4">CI</td>
<td class="tg-fymr"><strong>Buildbot</strong></td>
<td class="tg-0pky">More freedom and power<br />No UI to configure</td>
<td class="tg-0pky">Higher costs at the start<br />No sub-service to collect artifacts</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">TeamCity</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">Jenkins</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">Travis CI</td>
<td class="tg-0pky">Free for Open Source<br />Is a service<br /><br /></td>
<td class="tg-0pky">&nbsp;Only for Github</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky" rowspan="7">Virtualization</td>
<td class="tg-fymr"><strong>QEMU</strong></td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">Docker</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">VMWare</td>
<td class="tg-0pky">Easy to use</td>
<td class="tg-0pky">High cost</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">Open VZ</td>
<td class="tg-0pky">
<p>Effective resource management</p>
</td>
<td class="tg-0pky">Only for linux</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">KVM</td>
<td class="tg-0pky">
<p>Win/Lin</p>
<p>Effective and usefull</p>
</td>
<td class="tg-0pky">Need knowledge about Unix systems</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">Xen</td>
<td class="tg-0pky">
<p>Win/Lin</p>
<p>Good optimization</p>
<p>Open source</p>
</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">LXC</td>
<td class="tg-0pky">
<p>Linux</p>
<p>Very effective in small builds</p>
</td>
<td class="tg-0pky">Not for Windows</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky" rowspan="2">Provisioning</td>
<td class="tg-fymr"><strong>Ansible</strong></td>
<td class="tg-0pky">does not require installation of agents on managed nodes; ow threshold of entry; Modules can be written in almost any language;The web interface allows you to customize users, teams and equipment, use scripts; script language is pretty simple;Installing Python version 2.4 or higher; good documentation;</td>
<td class="tg-0pky">Lacked client support for Windows
The web interface is not automatically linked to an existing Ansible installation;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">?</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky" rowspan="4">"Frontend"<br />(repository, issues tracker,<br />communication, review,<br />collaboration)</td>
<td class="tg-fymr"><strong>GitHub</strong></td>
<td class="tg-0pky">Standart de-facto</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">Gitlab</td>
<td class="tg-0pky">More features as in Github</td>
<td class="tg-0pky">On Windows does not use pure Windows env (Cygwin)</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">Gerrit + Jira</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">?</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky" rowspan="2">Web Server</td>
<td class="tg-fymr"><strong>Nginx</strong></td>
<td class="tg-0pky">Documentation and support<br />Modularity<br />Centralized configuration<br />Administrators are responsible for security<br />Has proxy server</td>
<td class="tg-0pky">Processes only static content</td>
<td class="tg-0pky">Will be used for artifacts sharing. Link: https://stackshare.io/stackups/apache-httpd-vs-microsoft-iis-vs-nginx</td>
</tr>
<tr>
<td class="tg-0pky">Apache</td>
<td class="tg-0pky">Documentation and support<br />Modularity<br />Distributed configuration<br />Processes dynamic and static content</td>
<td class="tg-0pky">Distributed configuration<br />Users are responsible for security </td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky" rowspan="2">Monitoring</td>
<td class="tg-fymr"><strong>Zabbix</strong></td>
<td class="tg-0pky">
<p>Community supported</p>
<p>Easy to understand</p>
<p>SNMP</p>
<p>Agents</p>
</td>
<td class="tg-0pky">
<p>1 database</p>
<p>Web UI can not be expanded</p>
</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">Icinga 2</td>
<td class="tg-0pky">compatible with Nagios, easy to integrate, parallel processes.</td>
<td class="tg-0pky">have to develope modules, hard to understand, complex for small systems.</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">Build System</td>
<td class="tg-0pky">?</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky" rowspan="3">Test System</td>
<td class="tg-fymr">Robot Framework</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0pky">Self-written</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
<td class="tg-0pky">&nbsp;</td>
</tr>
<tr>
<td class="tg-0lax">?</td>
<td class="tg-0lax">&nbsp;</td>
<td class="tg-0lax">&nbsp;</td>
<td class="tg-0lax">&nbsp;</td>
</tr>
</tbody>
</table>


## On host OS (Ubuntu 18.04)
- Install host OS manually on your machine
```
sudo apt-get install openssh-server mc net-tools nginx screen
sudo apt install python3-pip

sudo nano /etc/nginx/nginx.conf
service nginx restart

# Add new user
sudo adduser infra-deploy #without adding to sudoers
users #check list of users
```
- Install QEMU which will be used for virtualization
```
sudo apt-get install qemu-kvm qemu virt-manager virt-viewer libvirt-bin
```

## On virtual machines
```
# Buildbot packages
# On master
sudo pip3 install buildbot==1.5 buildbot-console-view==1.5 buildbot-www==1.5

# On worker
sudo pip3 install buildbot-worker==1.5
sudo pip3 install gitpython==2.1.5 tenacity==4.5.0 txrequests txgithub service_identity
```

## Credits
Big thanks for the ideas, support and inspiration to:
- Alexander Zhogov
- Oleg Makarov
- Eugeny Ponomarev
- Dmitry Lobanov
