## Final Project Blog Post


I worked on my final project with two other classmates: John Gadomski and Nate Gomez. Our journey on the project was not linear. We started out wanting to analyze the texts of romance novels and see if male characters were described differently by male authors than they were by female authors. We thought about how to find the romance novels we would pick and decided to find an award list. We wanted to find an award that focuses solely on romance novels (rather than an award with different categories for different genres). We found the Romantic Novelists' Association's Award. The award had been given out for several decades, which was great because then, we could even analyze language's change over time! However, when we looked for full texts online, we could not find them without having to buy them. This actually taught me a lesson. I wish we had done more work before submitting our initial proposal. We realized a little late that our initial question would not work for us and because of that, we lost some valuable time when we changed directions. We instead decided to investigate how people discussed the books on Twitter. We chose Twitter because we had all heard of others scraping Twitter (and it was free). We also decided to see if the amount of buzz a novel had on Twitter (number of tweets, retweets, and likes) correlated to the timing of the award and the novel's revenue. We thought there would be three options. One would be that older novels that won the award earlier would have higher revenues since there was more time for them to sell. Two would be that the more the Twitter buzz, the more revenue the novel would have earned. Three would be that there was no correlation and many readers simply do not pay attention to awards or Twitter. However, we had another setback there. We learned that books do not have public revenues like movies often do. Due to how they are sold and how bookstores operate, the process to find out a book's revenue is complicated and sometimes impossible for the public to know. 


When searching for an alternative, I stumbled upon Amazon's Best Sellers Rank. This is a ranking system that assigns a score to products based on both the product's recent sales and historical sales data. There are categories within this overall ranking system, so all the novels' ranks in our data come from the book subcategory. The reason we chose this system as a revenue substitute is because unfortunately, Amazon is one of the biggest sources of books for many people out there, so its rankings are an adequate indicator of a book's success in comparison to other books. Additionally, Amazon was created before Twitter. Since its book sales data predates Twitter, the ranks have enough historical data too. We largely just looked at books that received an award after 2005, since Twitter was established in 2006 and we did not want any book to receive an unfair advantage. Once we figured out where we would be getting our data from, we started gathering it. From the Romantic Novelists' Associations website, I scraped all the novel titles, years, and authors. I put that into a CSV file so we could utilize it for visualizations later.  
 

![csv file making](https://github.com/dracoeye/is310groupproject/blob/main/Picture1.png)
![csv file making cont](https://github.com/dracoeye/is310groupproject/blob/main/Picture2.png)


Unfortunately, I ran into problems when trying to web scrape Amazon. Even just trying to get the HTML from a product's page on Amazon gave me errors that said to contact Amazon. When I looked into the problem online, I saw that others would have similar issues. I tried different solutions, but I could not find a solution that worked. Since I had to find less than 100 ranks, I just went in manually and added a column to the CSV file I created earlier and copied and pasted in the ranks. Many of them were quite large (over a million) and some others (especially older ones) did not exist on Amazon. Luckily, only one novel did not have a rank after 2005--which makes sense since more modern books were more likely to be found on the site.  


![csv file](https://github.com/dracoeye/is310groupproject/blob/main/Picture3.png)


Once we had all the metadata about the novels, we worked on visualizing it. We used Seaborn, a Python library that is based on Matplotlib, which we have used in class. We chose Seaborn because we were familiar with Matplotlib and Seaborn had some useful functions we liked the look of. We also used Matplotlib and Excel as well for some graphs. 


![making graphs](https://github.com/dracoeye/is310groupproject/blob/main/Picture4.png)
![making graphs 2](https://github.com/dracoeye/is310groupproject/blob/main/Picture5.png)
![making graphs 3](https://github.com/dracoeye/is310groupproject/blob/main/Picture6.png)
 

We wanted to compare the ranks over time for the novels, which is shown above. It appears there is no correlation between the year a novel won the award and its rank for novels after 2006, but there is a trend for the entire list of novels tending to have lower ranks the older they are, as you can see below.


![year and bsr](https://github.com/dracoeye/is310groupproject/blob/main/Picture7.png)


For the Twitter side of things, John and Nate focused on finding the data. They utilized Twint, a Twitter scraping tool that was written for Python. There were some issues with installing it correctly, but eventually, it all worked out. It was useful and allowed them to search keywords (which would be the novels and authors) and see the results as well as see the buzz. They could even filter through the results by language and time. Here is a code example of when “Struck” by Joss Stirling was searched for.


![twint](https://github.com/dracoeye/is310groupproject/blob/main/Picture8.png)


One drawback of using this method was that the novel’s title had to be searched with the novel's author. If only the author was used, sometimes people would be discussing other books the author wrote. Many of the book titles could have also been common phrases or words as well, so to find tweets specifically about the novels we were looking into, both the title and the author needed to be searched together. There were some interesting results. "Stars" were one such result. These tweets often rate a book out of 5 stars. For example,   


![tweet ex](https://github.com/dracoeye/is310groupproject/blob/main/Picture9.png)


We actually ended up comparing the average star rating for the top three reviewed novels on Twitter with their Amazon ranks.  


![visualizations](https://github.com/dracoeye/is310groupproject/blob/main/Picture10.png)


This comparison was actually quite helpful and revealed that the higher the average rating on Twitter of a novel, the more it sold on Amazon. We also compared the frequency of how often novels received 5 stars (not many from the award list received them). 


![visualizations](https://github.com/dracoeye/is310groupproject/blob/main/Picture11.png)


Additionally, we compared a novel's Twitter buzz with its Best Sellers Rank. Nate counted the novel's buzz before and after it received its award and then we saw that the buzz increased after it received the award (for 2 out of 3 awards), which gives some weight to the award affecting readership. However, Love Song, which was the 2018 (and last) novel that won the award, had a dramatic decrease in buzz after it won the award. Further research is required to find why Love Song was different from other novels.
 

![visualizations](https://github.com/dracoeye/is310groupproject/blob/main/Picture12.png)


Once we had all our data and visualizations together, I created and organized a slide deck where we can share our results--which was used in our project presentation. Our results showed that a novel's time since it won its award does correlate with the novel's Best Sellers Rank on Amazon if we look at all the novels. There is a correlation between Twitter buzz and the award since the buzz about a novel increased after it won the award. There is also a correlation between a novel's rank and its average star rating on Twitter. Due to our setbacks, we had to decrease our work goals. We wanted to include an analysis of the publishers as well, but we ran out of time to do that. Ideally, we would like to continue our research in the future by comparing the novels that won this award with another list of romance novels. We would pick romance novels that are at the top of the Amazon Best Sellers List as well as novels from another award list. We also may want to investigate the publishers and see if there is a pattern of which publishers seem to appear on these lists often.  


Working on this project has taught me more about computing in the humanities and the digital humanities. Our group originally took inspiration from Erin Davis' "What physical traits are most tied to gender in literature? Eye roll: Women are all soft thighs and red lips” (Davis, 2020). Reading that reminded me of my own experiences of reading a novel and just knowing the author was a man. I realized then that I did not know how to articulate how I knew what I knew. However, when trying to explain that to others (especially other men in this instance), they often ask for more evidence than just knowing. My experience also ties into the description of humanities research by Miriam Posner: "We can know something to be true without being able to point to a dataset, as it’s traditionally understood. We can know, to take just one example, that early silent film relied on the conventions of melodrama to create legible narratives, not because we have a spreadsheet somewhere, but because we’ve immersed ourselves so deeply in our source material that we’re attuned to its nuances" (Posner, 2015) I haven't necessarily done research to the depth that she is talking about, but I have read enough to just be able to predict some things without having "a spreadsheet somewhere" (Posner, 2015). That reading along with the research my group and I conducted this semester taught me the importance of having evidence to support claims we make or information we may just know. 
However, Matthew Lincoln’s “Confabulation in the humanities” ties into having evidence to support claims from another angle. Lincoln discusses the issue people may have “differentiating what, in retrospect, sounds *reasonable*, from what we actually *already knew*” (Lincoln, 2015). This reading helped caution me against just blindly following my own instinct and creating explanations without evidence. Although there are things that we can know without a spreadsheet, everyone is fallible and having evidence to back up our claims makes it easier not just to convince others that we are right, but also to reassure ourselves that we are not simply creating explanations that seem reasonable but are not true. 
Davis' work showed me there was a way of getting concrete data on such a topic. Our group wanted to see if we could do something similar, except concentrated on male characters in romance novels. We also took inspiration from Hanah Anderson's and Matt Daniels' *The Pudding* article about film dialogue, gender, and age. That article specifically included films' box office revenues and we thought adding in book revenues would be a great addition to our research as it would provide another angle to analyze (Anderson & Daniels, 2016). 

References


Anderson, H., & Daniels, M. (2016, April). *Film Dialogue from 2000 screenplays, Broken Down by Gender and Age*. The Pudding. Retrieved from https://pudding.cool/2017/03/film-dialogue/ 

Davis, E. (2020). *What physical traits are most tied to gender in literature? Eye roll: Women are all soft thighs and red lips*. The Pudding. Retrieved from https://pudding.cool/2020/07/gendered-descriptions/ 

Lincoln, M. (2015, March 21). *Confabulation in the humanities*. Home - Matthew Lincoln, PhD. Retrieved from https://matthewlincoln.net/2015/03/21/confabulation-in-the-humanities.html 

Posner, M. (2015, June 25). *Humanities Data: A Necessary Contradiction*. Miriam Posner's Blog. Retrieved from https://miriamposner.com/blog/humanities-data-a-necessary-contradiction/ 


