<h1>Tasks</h1>

<h2>0. Run software as another user</h2>
<p>The user <code>root</code> is, on Linux, the &ldquo;superuser&rdquo;. It can do anything it wants, that&rsquo;s a good and bad thing. A good practice is that one should never be logged in the <code>root</code> user, as if you fat finger a command and for example run <code>rm -rf /</code>, there is no comeback. That&rsquo;s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the <code>root</code> user can do, just need to use a specific command that you need to discover.</p>

<p>For the containers that you are given in this project as well as the checker, everything is run under the <code>root</code> user, which has the ability to run anything as another user.</p>

<p>Requirements:</p>

<ul>
<li>write a Bash script that accepts one argument</li>
<li>the script should run the <code>whoami</code> command under the user passed as an argument</li>
<li>make sure to try your script by passing different users</li>
</ul>

<p>Example:</p>

<pre><code>root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
</code></pre>

<h2>Run Nginx as Nginx</h2>

<p>The <code>root</code> user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as <code>root</code>. With this in mind, it&rsquo;s a good practice not to run your web servers as <code>root</code> (which is the default for most configurations) and instead run the process as the less privileged <code>nginx</code> user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the <code>nginx</code> user.</p>

<p>Fix this container so that Nginx is running as the <code>nginx</code> user.</p>

<p>Requirements:</p>

<ul>
<li><code>nginx</code> must be running as <code>nginx</code> user</li>
<li><code>nginx</code> must be listening on all active IPs on port <code>8080</code></li>
<li>You cannot use <code>apt-get remove</code></li>
<li>Write a Bash script that configures the container to fit the above requirements</li>
</ul>
