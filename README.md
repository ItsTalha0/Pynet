<h1> A python script for monitering internet downtime </h1>
<p>
This is a simple script using requests that checks a connection to google to
check whether the internet is down or not.</p><p> You are free to add changes.This script dosnt use the icmp protocol which is a little bit complex to undrstand when just getting started.The script also stores the result in a file in a csv format named log.csv.</p><p> The script will create the log file if it is not present on the system and if it present then it will simple keep logging in it.
</p>
<p>
    This script uses a hard coded list of websites. For now it just pings google.com. But if you want to expand on that you can either manually add the names of website to  the list or add a function that reads an external file either in csv file or json file. </p>




