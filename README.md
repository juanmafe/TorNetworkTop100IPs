# Tor Network Top 100 IPs
Tool to get the top 100 fastest nodes in the Tor network.
Based on <a href="https://github.com/Kirzahk/">Kirzahk</a> tool.

Just run <b>top100ipstor.py</b> to get the list of the fastest ones. The script will read the file <i>'/var/lib/tor/cached-microdesc-consensus'</i> and get the 100 fastest IPs. In the following executions, the script will take the previously collected IPs to perform an overall measurement. Only works on Linux.
