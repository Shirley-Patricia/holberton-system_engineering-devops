<h1>0x0D. Web stack debugging #0</h1>
<h2>Background Context</h2>

<p>The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that&rsquo;s the &ldquo;fun&rdquo; part of the job!).</p>

<p>Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.</p>

<p>In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.</p>

<p>Let&rsquo;s start with a very simple example. My server must: </p>

<ul>
<li>have a copy of the <code>/etc/passwd</code> file in <code>/tmp</code></li>
<li>have a file named <code>/tmp/isworking</code> containing the string <code>OK</code></li>
</ul>

<p>Let&rsquo;s pretend that without these 2 elements, my web application cannot work.</p>

<p>Let&rsquo;s go through this example and fix the server.</p>

<pre><code>vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
Unable to find image &#39;ubuntu:14.04&#39; locally
14.04: Pulling from library/ubuntu
34667c7e4631: Already exists
d18d76a881a4: Already exists
119c7358fbfc: Already exists
2aaf13f3eff0: Already exists
Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
Status: Downloaded newer image for ubuntu:14.04
76f44c0da25e1fdf6bcd4fbc49f4d7b658aba89684080ea5d6e8a0d832be9ff9
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
76f44c0da25e        ubuntu:14.04        &quot;/bin/bash&quot;         13 seconds ago      Up 12 seconds                           infallible_bhabha
vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
root@76f44c0da25e:/# ls /tmp/
root@76f44c0da25e:/# cp /etc/passwd /tmp/
root@76f44c0da25e:/# echo OK &gt; /tmp/isworking
root@76f44c0da25e:/# ls /tmp/
isworking  passwd
root@76f44c0da25e:/#
vagrant@vagrant:~$
</code></pre>

<p>Then my answer file would contain:</p>

<pre><code>sylvain@ubuntu:~$ cat answerfile
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK &gt; /tmp/isworking
sylvain@ubuntu:~$
</code></pre>

<p>Note that as you cannot use interactive software such as <code>emacs</code> or <code>vi</code> in your Bash script, everything needs to be done from the command line (including file edition).</p>

<h2>Resources</h2>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>curl</code></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash scripts must pass <code>Shellcheck</code> without any error</li>
<li>Your Bash scripts must run without error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<h2>Task</h2>

<h3 class="panel-title">
      0. Give me a page!
    </h3>

<p>In this first debugging project, you will need to get <a href="/rltoken/B4vOap4dPNKxdZzBbepK7Q" title="Apache" target="_blank">Apache</a> to run on the container and to return a page containing <code>Hello Holberton</code> when querying the root of it.</p>

<p>Example:</p>

<pre><code>vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   &quot;/bin/bash&quot;         3 seconds ago       Up 2 seconds        0.0.0.0:8080-&gt;80/tcp   vigilant_tesla
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
vagrant@vagrant:~$
</code></pre>

<p>Here we can see that after starting my Docker container, I <code>curl</code> the port <code>8080</code> mapped to the Docker container port <code>80</code>, it does not return a page but an error message. Note that you might also get the error message <code>curl: (52) Empty reply from server</code>.</p>

<pre><code>vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$
</code></pre>

<p>After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains <code>Hello Holberton</code>.
Paste the command(s) you used to fix the issue in your answer file.</p>
