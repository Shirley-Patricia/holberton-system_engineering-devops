<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/XnVjFM8a1W4RfRu4TCPY-g" title="The <code>for</code> loop&quot; target=&ldquo;_blank&rdquo;>The <code>for</code> loop</a> </li>
<li><a href="/rltoken/TKpmMkXbW4dgKxdKt51fZA" title="The <code>while</code> loop&quot; target=&ldquo;_blank&rdquo;>The <code>while</code> loop</a> </li>
<li><a href="/rltoken/6MzdEyyTpW9R1k0hbKFUbQ" title="The <code>until</code> loop&quot; target=&ldquo;_blank&rdquo;>The <code>until</code> loop</a> </li>
<li><a href="/rltoken/zOH3mQvvHyO_ITinhKSV6Q" title="Loops sample" target="_blank">Loops sample</a> </li>
<li><a href="/rltoken/IM0Gv6VPzwAmqzlJxETZkw" title="Variable assignment and arithmetic" target="_blank">Variable assignment and arithmetic</a> </li>
<li><a href="/rltoken/K3E6xI9-goDM-93vsjCpPA" title="Comparison operators" target="_blank">Comparison operators</a> </li>
<li><a href="/rltoken/0OZLLDT28KrRZdid-l6hwg" title="File test operators" target="_blank">File test operators</a> </li>
<li><a href="/rltoken/Dyrnap2UC-LrzrmCOJRx8A" title="Make your scripts portable" target="_blank">Make your scripts portable</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>env</code></li>
<li><code>cut</code></li>
<li><code>for</code></li>
<li><code>while</code></li>
<li><code>until</code></li>
<li><code>if</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/AVktLDpuzzD92vXnfuqeWg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create SSH keys</li>
<li>What is the advantage of using  <code>#!/usr/bin/env bash</code> over <code>#!/bin/bash</code></li>
<li>How to use <code>while</code>, <code>until</code> and <code>for</code> loops</li>
<li>How to use <code>if</code>, <code>else</code>, <code>elif</code> and <code>case</code> condition statements</li>
<li>How to use the <code>cut</code> command</li>
<li>What are files and other comparison operators, and how to use them</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>You are not allowed to use <code>awk</code></li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.7.0</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

 <h2 class="gap">Tasks</h2>

 <h3>0. Create a SSH RSA key pair</h3>

  <p>Read for this task:</p>

<ul>
<li><a href="/rltoken/_11FMUABmTFrUaQvTr8rbw" title="Linux and Mac OS users" target="_blank">Linux and Mac OS users</a></li>
<li><a href="/rltoken/_JMRDGehQWRXzce3EVRdWA" title="Windows users" target="_blank">Windows users</a></li>
</ul>

<p>man: <code>ssh-keygen</code></p>

<p>You will soon have to manage your own <strong>servers</strong> concept page hosted on remote <a href="/rltoken/e4-Q5Ebz_iidUZAkvrPyEA" title="data centers" target="_blank">data centers</a>. We need to set them up with your RSA public key so that you can access them via SSH.</p>

<p>Create a RSA key pair.</p>

<h3 class="panel-title">
      1. For Best School loop
    </h3>

 <p>Write a Bash script that displays <code>Best School</code> 10 times.</p>

<p>Requirement:</p>

<ul>
<li>You must use the <code>for</code> loop (<code>while</code> and <code>until</code> are forbidden)</li>
</ul>

<h3 class="panel-title">
      2. While Best School loop
    </h3>
<p>Write a Bash script that displays <code>Best School</code> 10 times.</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul>

<h3 class="panel-title">
      3. Until Best School loop
    </h3>

<p>Write a Bash script that displays <code>Best School</code> 10 times.</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>until</code> loop (<code>for</code> and <code>while</code> are forbidden)</li>
</ul>

<h3 class="panel-title">
      4. If 9, say Hi!
    </h3>
 <p>Write a Bash script that displays <code>Best School</code> 10 times, but for the 9th iteration, displays <code>Best School</code> <em>and then</em> <code>Hi</code> on a new line.</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>if</code> statement</li>
</ul>

 <h3 class="panel-title">
      5. 4 bad luck, 8 is your chance
    </h3>
<p>Write a Bash script that loops from 1 to 10 and:</p>

<ul>
<li>displays <code>bad luck</code> for the 4th loop iteration</li>
<li>displays <code>good luck</code> for the 8th loop iteration</li>
<li>displays <code>Best School</code> for the other iterations</li>
</ul>

<h3 class="panel-title">
      6. Superstitious numbers
    </h3>
<p>Write a Bash script that displays numbers from 1 to 20 and:</p>

<ul>
<li>displays <code>4</code> <em>and then</em> <code>bad luck from China</code> for the 4th loop iteration</li>
<li>displays <code>9</code> <em>and then</em> <code>bad luck from Japan</code> for the 9th loop iteration</li>
<li>displays <code>17</code> <em>and then</em> <code>bad luck from Italy</code> for the 17th loop iteration</li>
</ul>

<h3 class="panel-title">
      7. Clock
    </h3>

 <p>Write a Bash script that displays the time for 12 hours and 59 minutes:</p>

<ul>
<li>display hours from 0 to 12</li>
<li>display minutes from 1 to 59</li>
</ul>

<h3 class="panel-title">
      8. For ls
    </h3>
<p>Write a Bash script that displays:</p>

<ul>
<li>The content of the current directory</li>
<li>In a list format</li>
<li>Where only the part of the name after the first dash is displayed (refer to the example)</li>
</ul>

 <h3 class="panel-title">
      9. To file, or not to file
    </h3>

	<p>Write a Bash script that gives you information about the <code>school</code> file.</p>

<p>Requirements:</p>

<ul>
<li>You must use <code>if</code> and, <code>else</code> (<code>case</code> is forbidden)</li>
<li>Your Bash script should check if the file exists and print:

<ul>
<li>if the file exists: <code>school file exists</code></li>
<li>if the file does not exist: <code>school file does not exist</code></li>
</ul></li>
<li>If the file exists, print:

<ul>
<li>if the file is empty: <code>school file is empty</code></li>
<li>if the file is not empty: <code>school file is not empty</code></li>
<li>if the file is a regular file: <code>school is a regular file</code></li>
<li>if the file is not a regular file: (nothing)</li>
</ul></li>
</ul>