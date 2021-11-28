<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><strong>Network basics</strong> concept page</li>
<li><strong>Server</strong> concept page</li>
<li><strong>Web server</strong> concept page</li>
<li><strong>DNS</strong> concept page</li>
<li><strong>Load balancer</strong> concept page</li>
<li><strong>Monitoring</strong> concept page</li>
<li><a href="/rltoken/ZbnRbvp1926PRxMG3_8fZA" title="What is a database" target="_blank">What is a database</a> </li>
<li><a href="/rltoken/Nb8B47Y2D8SLqQMOKVoQyQ" title="What&#39;s the difference between a web server and an app server?" target="_blank">What&rsquo;s the difference between a web server and an app server?</a></li>
<li><a href="/rltoken/ojwHUACZEtIWfI9M6i7c3g" title="DNS record types" target="_blank">DNS record types</a> </li>
<li><a href="/rltoken/wYpewVpIp9PSqqL27RPafg" title="Single point of failure" target="_blank">Single point of failure</a> </li>
<li><a href="/rltoken/Mlvynt0OgLQXrxjrC5Wlnw" title="How to avoid downtime when deploying new code" target="_blank">How to avoid downtime when deploying new code</a> </li>
<li><a href="/rltoken/POX3jE0S6TChQHSYQraYeQ" title="High availability cluster (active-active/active-passive)" target="_blank">High availability cluster (active-active/active-passive)</a> </li>
<li><a href="/rltoken/N4BwU4wYDNW02kdzMiekFw" title="What is HTTPS" target="_blank">What is HTTPS</a> </li>
<li><a href="/rltoken/ZFTutaKN4wWzmL4fWhQmeg" title="What is a firewall" target="_blank">What is a firewall</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/Dvn7v5U404zIccrJ_jDevg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects</li>
<li>You must be able to explain what each component is doing</li>
<li>You must be able to explain system redundancy</li>
<li>Know all the mentioned acronyms: LAMP, SPOF, QPS</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram</li>
<li>This project will be manually reviewed:</li>
<li>As each task is completed, the name of that task will turn green</li>
<li>Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use <a href="/rltoken/QorG0rvw1PzqWBVrqWW6Sg" title="imgur" target="_blank">imgur</a> but feel free to use anything you want). </li>
<li>For the following tasks, insert the link from of your screenshot into the answer file </li>
<li>After pushing your answer file to GitHub, insert the GitHub file link into the URL box</li>
<li>You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session</li>
<li>Focus on what you are being asked: </li>
<li>Cover what the requirements mention, we will explore details in a later project</li>
<li>Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements</li>
<li>Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you</li>
<li>In this project, again, avoid going in details if not asked</li>
</ul>

</div>

<h2>Task</h2>

<h3>0. Simple web stack </h3>
<p> A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.<br>

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start your explanation by having a user wanting to access your website.</p> 

<h3>1. Distributed web infrastructure </h3>
<p> On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com
<p>Requirements:</p>

<ul>
<li> You must add:

<ul>
<li>2 servers</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 load-balancer (HAproxy)</li>
<li>1 set of application files (your code base)</li>
<li>1 database (MySQL)</li>
</ul></li>

<h3>2. Secured and monitored web infrastructure</h3>
<p>On a whiteboard, design a three server web infrastructure that hosts the website <code>www.foobar.com</code>, it must be secured, serve encrypted traffic, and be monitored.</p>

<p>Requirements:</p>

<ul>
<li> You must add:

<ul>
<li>3 firewalls </li>
<li>1 SSL certificate to serve <code>www.foobar.com</code> over HTTPS</li>
<li>3 monitoring clients (data collector for Sumologic or other monitoring services)</li>
</ul></li>