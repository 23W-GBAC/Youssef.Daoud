# Exploring possible solutions for the issue:

Over the course of the past couple of weeks, I've been trying to look for an optimal and fuss-free solution to this little problem of mine and decided on many different ideas before settling on the final and, to me at least, the best solution out of all the following. Here are the ones I tried before, and why they didn't stick with me.

## Doing the whole process manually:
The very first thing that came to mind was just writing down when I'd last edited any of the files by hand or by using a note-keeping app, and while that might have been easy enough to make due with for 4 blog posts, having to maybe deal with a lot more eventually is definitely not an assuring prospect for this method, and the amount of times I've forgotten to do this is better left unkown... so I had to start looking elsewhere.
Pros:
- Easy enough to do, no need for any prior coding experience, just needed to remind myself to write down the last date and time I edited a page/post at
Cons:
- Not very accurate, easily forgettable, not very efficent when there's a lot of posts written at different times, not very time-efficent either

## Using Git through the command line:
Another approach that I thought of and tried is using git in a command line environment. It involved using Git commands and scripting to fetch information about the last modification date of the markdown files on my blog. I decided on using Python too to write the script that would automate the process because of my familiarity with the language. 
The whole process left me a bit fumbled and confused, mostly because I couldn't get to run the python script that's on my machine to read the log data on the repo properly. I also didn't feel comfortable using git through a terminal because I wasn't accustomed to it in the first place so I decided against this as well.
Pros:
- Not limited to GitHub per se and can be applied to any sort of Git repository. Lots of customization allowed due to the freedom using the command line entails, provided whoever's doing the coding knows what they're doing.
Cons:
- Like I said, lots of experience and know-how required to actually get anything done with it. Would not recommend for total beginners or people with little to no extra time on their hands.

## Using GitHub's GraphQL API:
GitHub provides an API called GraphQL that allows people using it to query specific information about their repositories and whatnot, including details about files and their last modification date, so I decided to try creatine a GraphQL query to retrieve the information that I want to get from the log files. The process went fairly smoothly but I also found it too complicated so I decided against it, at least for now.
Pros:
- Precision: GraphQL queries can be tailored to retrieve only the required information, reducing unnecessary data transfer and improving performance. Consistency since the GraphQL API provides a consistent interface that remains stable across different versions, reducing the likelihood of breaking changes.
Cons:
- Accessing the GitHub GraphQL API requires authentication, which involves generating and managing access tokens and they can be pretty fussy to deal with. Rate Limits are also a thing; the API imposes rate limits which essentially means it limits network traffic to conserve bandwith and whatnot, potentially affecting the speed of the automation process, especially in cases of frequent queries which can cause trouble later down the road.

## Using GitHub Actions:
The final approach that I've decided to try out. It involved uploading the automation script that I wrote in python onto the repository and linking it with a workflow file that automatically checks the logs of the markdown files periodically every 1 minute or so, and whenever a push is done onto the repo too. The dates can then be checked by going to the checks section and checking the result of the script or by using a terminal to check the results of the python script.

This approach also took me a while to get running but it turned out to be the easiest of them all for me, all things considered. I managed to actually get the whole thing running in less than a day and it's been quite helpful so far though are still some obstacles facing me with getting it to run exactly like I want it to but all in all this is as good as it got for me. I'll explain more about its inner workings and how the python script works in the following post/article. 

## Conclusion:
Automating the whole ordeal seemed like it would be going nowhere to me at first because almost every aspect of the previous approaches (sans the first approach obviously) seemed hard to understand and do at first but as time went and I got more comfortable with GitHub as a whole I've managed to find my way around this, ending up with a solution that, while not optimal, is close enough to what I need. GitHub Actions provides a rather seamless integration with the rest of GitHub so that's why I really ended up using it, due to the minimal amounts of fuss required to set it up and getting it running.
Of course, it should go without saying that the choice of the most suitable solution for doing the automation depends on a lot of different factors that others may have differently than I do, such as the level of customization required, and the familiarity of the user with the respective user interfaces/technologies. 





