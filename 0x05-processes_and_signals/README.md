  <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/FcpEdqz8hau7eEB0Pi8Ong" title="Linux PID" target="_blank">Linux PID</a> </li>
<li><a href="/rltoken/hX_t2YK0erLPbdTq0-uKwQ" title="Linux process" target="_blank">Linux process</a> </li>
<li><a href="/rltoken/SojW4zvL8j1yaoa7_NM6rA" title="Linux signal" target="_blank">Linux signal</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>ps</code></li>
<li><code>pgrep</code></li>
<li><code>pkill</code></li>
<li><code>kill</code></li>
<li><code>exit</code></li>
<li><code>trap</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/lg0QA0Ewi3RfiD5UUUNUXw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a PID</li>
<li>What is a process</li>
<li>How to find a process&rsquo; PID</li>
<li>How to kill a process</li>
<li>What is a signal</li>
<li>What are the 2 signals that cannot be ignored</li>
</ul>

<h2 class="gap">Tasks</h2>

<h2> 0. What is my PID </h2>
<p>Write a Bash script that displays its own PID.</p>

<h2> 1. List your processes </h2>

<p>Write a Bash script that displays a list of currently running processes.</p>

<p>Requirements:</p>

<ul>
<li>Must show all processes, for all users, including those which might not have a TTY</li>
<li>Display in a user-oriented format</li>
<li>Show process hierarchy</li>
</ul>

<h2> 2. Show your Bash PID </h2>

<p>Using your previous exercise command, write a Bash script that displays lines containing the <code>bash</code> word, thus allowing you to easily get the PID of your Bash process.</p>

<h2> 3. Show your Bash PID made easy </h2>
<h2> 4. To infinity and beyond </h2>
Write a Bash script that displays To infinity and beyond indefinitely.
<h2> 5. Don't stop me now! </h2>
We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that stops 4-to_infinity_and_beyond process.


<h2> 6. Stop me if you can </h2>
Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements: You cannot use kill or killall

<h2> 7. Highlander </h2>
Write a Bash script that displays:

To infinity and beyond indefinitely.

With a sleep 2 in between each iteration.

I am invincible!!! when receiving a SIGTERM signal.

<h2> 8. Beheaded process </h2>
Write a Bash script that kills the process 7-highlander
