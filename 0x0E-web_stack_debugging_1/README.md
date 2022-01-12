<h1>Project: 0x0E. Web stack debugging #1</h1>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash scripts must pass <code>Shellcheck</code> without any error</li>
<li>Your Bash scripts must run without error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
<li>You are not allowed to use <code>wget</code></li>
</ul>

     <h2 class="gap">Tasks</h2>

    <div data-role="task1446" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-1446">
  <span id="user_id" data-id="3513"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Nginx likes port 80
    </h3>

<div>
	<span class="label label-info">
		mandatory
	</span>
</div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3513"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Using your debugging skills, find out what&rsquo;s keeping your Ubuntu container&rsquo;s Nginx installation from listening on port <code>80</code>. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.</p>

<p>Requirements:</p>

<ul>
<li>Nginx must be running, and listening on port <code>80</code> of all the server&rsquo;s active IPv4 IPs </li>
<li>Write a Bash script that configures a server to the above requirements</li>
</ul>

<pre><code>root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# ./0-nginx_likes_port_80 &gt; /dev/null 2&amp;&gt;1
root@966c5664b21f:/#
root@966c5664b21f:/# curl 0:80
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;Welcome to nginx!&lt;/title&gt;
&lt;style&gt;
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Welcome to nginx!&lt;/h1&gt;
&lt;p&gt;If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.&lt;/p&gt;

&lt;p&gt;For online documentation and support please refer to
&lt;a href=&quot;http://nginx.org/&quot;&gt;nginx.org&lt;/a&gt;.&lt;br/&gt;
Commercial support is available at
&lt;a href=&quot;http://nginx.com/&quot;&gt;nginx.com&lt;/a&gt;.&lt;/p&gt;

&lt;p&gt;&lt;em&gt;Thank you for using nginx.&lt;/em&gt;&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
root@966c5664b21f:/#
</code></pre>

  </div>
