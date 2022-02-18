<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>Libraries imported in your Python files must be organized in alphabetical order</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>You must use the Requests module for sending HTTP requests to the Reddit API</li>
</ul>

<h1>Tasks</h1>
<h2>0. How many subs?</h2>
<p>Write a function that queries the <a href="https://www.reddit.com/dev/api/" title="Reddit API" target="_blank">Reddit API</a> and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.</p>

<p>Hint: No authentication is necessary for most features of the Reddit API. If you&rsquo;re getting errors related to Too Many Requests, ensure you&rsquo;re setting a custom User-Agent.</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def number_of_subscribers(subreddit)</code></li>
<li>If not a valid subreddit, return 0.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>

<h2>1. Top Ten</h2>
<p>Write a function that queries the <a href="https://www.reddit.com/dev/api/" title="Reddit API" target="_blank">Reddit API</a> and prints the titles of the first 10 hot posts listed for a given subreddit.</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def top_ten(subreddit)</code></li>
<li>If not a valid subreddit, print None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>
